from pydantic import BaseModel
from database.config import DB
from random import randint

class Account(BaseModel):
    full_name: str | None = None
    balance: float = 0.0
    agency: int | None = 1
    account_number: int = randint(1, 9999999999)
    email: str | None = None

    #TODO Turn create into a class model for a base DB class inheriting from BaseModel.
    def create(self):
        tp = tuple(self.model_dump().values())
        DB.query(f"INSERT INTO account VALUES (NULL, ?, ?, ?, ?, ?)", tp)


            
    @classmethod
    def get_user(cls, email: str):
        return DB.query(f"SELECT * FROM account WHERE email = ?", (email,))
 