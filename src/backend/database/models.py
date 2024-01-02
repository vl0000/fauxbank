from pydantic import BaseModel
from database.config import DB
from random import randint
from secrets import token_bytes
from passlib.hash import bcrypt
from base64 import b64encode

def hash_password(password: str, salt: str):
    if not password:
        raise ValueError("Password cannot be null")
    else:
        return bcrypt.using(rounds=8).hash(password + salt)


class AccountInDb(BaseModel):
    full_name: str
    balance: float = 0.0
    agency: int = 1
    account_number: int = randint(1, 9999999999)
    email: str
    password: str
    # If the salt isnt turned into a string, it cannot be appended to the password later
    salt: str = b64encode(token_bytes(16)).decode("utf-8")

    #TODO Turn create into a class model for a base DB class inheriting from BaseModel.
    def create(self):
        temp_model = self.model_dump()
        temp_model['password'] = hash_password(temp_model['password'], temp_model['salt'])

        DB.query(f"INSERT INTO account VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", tuple(temp_model.values()))

    @classmethod
    def get_user(cls, email: str):
        return DB.query(f"SELECT * FROM account WHERE email = ?", (email,))
 