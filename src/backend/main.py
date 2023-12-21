from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Account(BaseModel):
    full_name: str | None = None
    balance: float | None = None
    agency: int | None = None
    account_number: int | None = None

acc = Account(
    full_name= "Fulano Fulanildo",
    balance= 345.97,
    agency= 1,
    account_number= 1234
)

@app.get("/api/account/{id}")
def get_account(id: int | None, query: Annotated[list[str], Query()] = None):
    response = dict()
    if query:
        for q in query:
            response[q] = acc.model_dump()[q]

    return response