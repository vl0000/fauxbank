from pydantic import BaseModel
from database.config import CONN, CURSOR
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

        try:
            CURSOR.execute(f"INSERT INTO account VALUES (NULL, ?, ?, ?, ?, ?)", tp)
        except Exception as e:
            print(e)
            CONN.rollback()
        finally:
            CONN.commit()
            
    @classmethod
    def get_by_id(cls, id: int):
        try:
            CURSOR.execute(f"SELECT * FROM account WHERE id = ?", (id,))

        except Exception as e:
            print(e)

        finally:
            return CURSOR.fetchall()
    
    @classmethod
    def get_user(cls, email: str):
        try:
            CURSOR.execute(f"SELECT * FROM account WHERE email = ?", (email,))
        except Exception as e:
            print(e)
        finally:
            return CURSOR.fetchall()