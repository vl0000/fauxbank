from os import environ
from random import randint
from secrets import token_bytes
from datetime import datetime, timedelta

from pydantic import BaseModel
from database.config import DB

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
    full_name: str
    balance: float = 0.0
    agency: int = 1
    account_number: int = randint(1, 9999999999)

class AccountAuth(BaseModel):
    email: str
    password: str
    # If the salt isnt turned into a string, it cannot be appended to the password later
    salt: str = b64encode(token_bytes(16)).decode("utf-8")

    @classmethod
    def get_user(cls, email: str):
        return DB.query(f"SELECT * FROM account WHERE email = ?", (email,))

    @classmethod
    def authenticate(cls, email: str, password_in: str):
        usr = cls.get_user(email)[0]
        if not usr:
            raise LookupError("No user found")
        
        #The password is the 7th element in the tuple and the salt the 8th
        password_hash = usr[6]
        salt = usr[7]

        # TODO return an output model
        if bcrypt.verify(password_in + salt, password_hash):
            return usr
        else:
            return None

class AccountInDb(AccountAuth, AccountOut):

    #TODO Turn create into a class model for a base DB class inheriting from BaseModel.
    def create(self):
        temp_model = self.model_dump()
        temp_model['password'] = hash_password(temp_model['password'], temp_model['salt'])

        DB.query(f"INSERT INTO account VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", tuple(temp_model.values()))
    




    
 