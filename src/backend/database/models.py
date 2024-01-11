from os import environ
from secrets import token_bytes, randbelow
from datetime import datetime, timedelta

from pydantic import BaseModel
from database.tables import engine, accounts, cards, transactions
from sqlalchemy import insert, select

from jose import JWTError, jwt
from passlib.hash import bcrypt
from base64 import b64encode

SECRET_KEY = environ.get("SECRET_KEY")
ALGORITHM = environ.get("ALGO")

def hash_password(password: str, salt: str):
    if not password:
        raise ValueError("Password cannot be null")
    else:
        return bcrypt.using(rounds=8).hash(password + salt)


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
    agency: int = 1
    number: int = randbelow(1, 9999999999)

class AccountAuth(BaseModel):
    """
        Do not use for anything other than authentication. Not even output
    """
    email: str
    password: str
    # If the salt isnt turned into a string, it cannot be appended to the password later
    salt: str = b64encode(token_bytes(16)).decode("utf-8")

    @classmethod
    def _get_user(cls, email: str):
        """To be used by other methods ONLY and never send this to the user"""
        with engine.connect() as conn:
            stmt = select(accounts).where(accounts.c.email == email)
            res = conn.execute(stmt).fetchone()._asdict()
            return AccountInDb(**res)

    @classmethod
    def authenticate(cls, email: str, password_in: str):
        usr = cls._get_user(email)
        if not usr:
            raise LookupError("No user found")
        
        #The password is the 7th element in the tuple and the salt the 8th
        password_hash = usr.password
        salt = usr.salt

        # TODO return an output model
        if bcrypt.verify(password_in + salt, password_hash):
            return usr
        else:
            return None

class DbModel:
    @classmethod
    def _query(cls, stmt):
            with engine.connect() as conn:
                res = conn.execute(stmt)
                conn.commit()
                if res:
                    return res


class AccountInDb(AccountAuth, AccountOut, DbModel):
    """
        This class will contain all the necessary user information.
        Any database operations should be done through this class, regardless of
        whether or not the method is present in others. An exception can be made for the
        authenticate() method.
    """
    @classmethod
    def get_user_safe(cls, email: str) -> AccountOut:
        """ This is the method you want to use if youre going to send this data to users """
        # Only the data from the second to the fifth element is to be used
        usr = AccountOut(**cls._get_user())
        return usr

    def create(self):
        temp_model = self.model_dump()
        temp_model['password'] = hash_password(temp_model['password'], temp_model['salt'])
        stmt = insert(accounts).values(**temp_model)

        self._query(stmt)
    
    def get_card(self):
        stmt = select(cards).where(cards.c.holder == self.id)
        res = self._query(stmt)
        return res.fetchone()._asdict()
        
    
class Transaction(BaseModel,DbModel):
    id: int
    payer: int
    payee: int
    amount: float = 0.0
    date: datetime

    def _create(self):
        stmt = insert(transactions).values(**self.model_dump())

        self._query(stmt)
    
    def get_all(self):
        stmt = select(transactions)
        res = self._query(stmt)
        return res.fetchall()

class Card(BaseModel, DbModel):
    number: int
    holder: int
    cvv: int
    expiration: date

    def create(self):
        stmt = insert(cards).values(**self.model_dump())

        self._query(stmt)
