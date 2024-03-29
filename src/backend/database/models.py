from os import environ
from secrets import token_bytes, randbelow
from datetime import datetime, timedelta
from typing import Union

from pydantic import BaseModel
from database.tables import engine, accounts, transactions
from sqlalchemy import insert, select, or_

from jose import jwt
from passlib.hash import bcrypt
from base64 import b64encode

SECRET_KEY = environ.get("SECRET_KEY")
ALGORITHM = environ.get("ALGO")

def hash_password(password: str, salt: str):
    if not password:
        raise ValueError("Password cannot be null")
    else:
        return bcrypt.using(rounds=8).hash(password + salt)

def query(stmt):
        with engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()
            if res:
                return res


class Token(BaseModel):
    access_token: str
    token_type: str

    @classmethod
    def generate_token(cls, data: dict, expires: timedelta = 30):
        to_encode = data.copy()
        expiration = datetime.utcnow() + timedelta(minutes=expires)

        to_encode.update({"exp": expiration})
        
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    @classmethod
    def decode(cls, token):
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

class AccountOut(BaseModel):
    """
        This class is only meant to be used as output. DO NOT use for anything else!
        Use AccountInDB for any database operations.
    """
    name: str
    balance: float = 0.0
    number: int = randbelow(9999999999)

    def _get_transactions(self, incoming: bool = True):
        """
            If incoming is True, it will get all transactions where this account has received money.
            If false, it will get all the ones where this account sent money.
            It returns all the incoming ones by default
        """
        if incoming == False:
            stmt = select(transactions.c.amount).where(transactions.c.payer == self.number)
            return query(stmt).fetchall()
        else:
            stmt = select(transactions.c.amount).where(transactions.c.payee == self.number)
            return query(stmt).fetchall()
    
    def get_all_transactions(self) -> list[tuple]:
        condition = or_(transactions.c.payee == self.number, transactions.c.payer == self.number)
        stmt = select(transactions).where(condition)
        res = query(stmt).fetchall()
        return res

    def get_balance(self) -> float:
        # all incoming transactions
        incoming = self._get_transactions()
        # Unpack them into a list of values instead of tuples
        incoming = [x[0] for x in incoming]

        outgoing = self._get_transactions(incoming=False)
        outgoing = [x[0] for x in outgoing]

        return (sum(incoming) - sum(outgoing))

class AccountAuth(BaseModel):
    """
        Do not use for anything other than authentication. Not even output
    """
    # There is no email validation because it wont really be used for this project.
    # It's scope has been reduced in order to finish it quickly.
    # There will be no email confirmations anymore.
    email: str
    password: str
    # If the salt isnt turned into a string, it cannot be appended to the password later
    salt: str = b64encode(token_bytes(16)).decode("utf-8")

    @classmethod
    def _get_user(cls, number: int):
        """To be used by other methods ONLY and never send this to the user"""
        with engine.connect() as conn:
            stmt = select(accounts).where(accounts.c.number == number)
            res = conn.execute(stmt).fetchone()
            if not res:
                raise LookupError("User not found")
            return res._asdict()

    @classmethod
    def authenticate(cls, email: str, password_in: str):
        stmt = select(accounts).where(accounts.c.email == email)
        usr = query(stmt).fetchone()._asdict()
        if not usr:
            raise LookupError("No user found")

        
        #The password is the 7th element in the tuple and the salt the 8th
        password_hash = usr["password"]
        salt = usr["salt"]

        # TODO return an output model
        if bcrypt.verify(password_in + salt, password_hash):
            return usr
        else:
            return None


class AccountInDb(AccountAuth, AccountOut):
    """
        This class will contain all the necessary user information.
        Any database operations should be done through this class, regardless of
        whether or not the method is present in others. An exception can be made for the
        authenticate() method.
    """
    @classmethod
    def get_user_safe(cls, number: str) -> AccountOut:
        """ This is the method you want to use if youre going to send this data to users """
        # Only the data from the second to the fifth element is to be used
        usr = AccountOut(**cls._get_user(number))
        usr.balance = usr.get_balance()
        return usr

    def _secure_password(self):
        self.password = hash_password(self.password, self.salt)

    def _get_user_by_email(self, email):
        stmt = select(accounts).where(accounts.c.email == email)
        res = query(stmt)
        return res.fetchone()

    def create(self):
        self._secure_password()
        temp_model = self.model_dump()
        del temp_model['balance']
        stmt = insert(accounts).values(**temp_model)

        query(stmt)


class TransactionIn(BaseModel):
    payee: int
    amount: float
    
class Transaction(BaseModel):
    payer: int
    payee: int
    amount: float = 0.0
    date: Union[datetime, None] = datetime.utcnow()

    def create(self):
        if self.is_valid():
            stmt = insert(transactions).values(**self.model_dump())
            query(stmt)
        else:
            raise ValueError("Invalid Transaction")
    
    @classmethod
    def get_all(cls):
        stmt = select(transactions)
        res = query(stmt)
        return res.fetchall()
    
    def _get_account(self, who: int) -> AccountOut:
        """Gets the payer or payee """
        stmt = select(accounts).where(accounts.c.number == who)

        # if none are returned, this will raise an error
        res = query(stmt).fetchone()._asdict()
        return AccountOut(**res)
    
    def _get_payee(self) -> AccountOut:
        return self._get_account(self.payee)
    
    def _get_payer(self) -> AccountOut:
        return self._get_account(self.payer)
        
    def is_valid(self) -> bool:
        """
        This function will check 2 things:
        1- Whether or not the payer has sufficient funds to complete the transaction
        2- Whether or not the payee exists
        """
        # These functions will raise exceptions by themselves, in case one or neither exists
        payer = self._get_payer()
        payee = self._get_payee()

        if payer.get_balance() < self.amount:
            #TODO replace with an HTTP error
            raise ValueError("Not enough dosh")
        elif  payee == None or payer == None:
            raise LookupError("Missing a payer or payee")
        
        return True