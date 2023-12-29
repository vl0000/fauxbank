from pydantic import BaseModel
from database.config import CONN, CURSOR

class Account(BaseModel):
    full_name: str | None = None
    balance: float | None = None
    agency: int | None = None
    account_number: int | None = None
    email: str | None = None

    #TODO Turn create into a class model for a base DB class inheriting from BaseModel.
    def create(self):
        tp = tuple(self.model_dump().values())
        # This is here because it will become a class method for all database models(pydantic)
        table = __class__.__name__.lower()

        try:
            CURSOR.execute(f"INSERT INTO {table} VALUES (NULL, ?, ?, ?, ?, ?)", tp)
        except Exception as e:
            print(e)
            CONN.rollback()
        finally:
            CONN.commit()