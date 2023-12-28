from pydantic import BaseModel

class Account(BaseModel):
    full_name: str | None = None
    balance: float | None = None
    agency: int | None = None
    account_number: int | None = None

