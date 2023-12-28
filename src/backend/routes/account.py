from typing import Annotated

from database.models import Account

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

# TEMPORARY!!
# TODO REMOVE THIS. After a db is made
acc = Account(
    full_name= "Fulano Fulanildo",
    balance= 345.97,
    agency= 1,
    account_number= 1234
)

router = APIRouter()

@router.get("/api/account/{id}")
def get_account(id: int | None, query: Annotated[list[str], Query()] = None):
    response = dict()
    if query:
        for q in query:
            response[q] = acc.model_dump()[q]
    else:
        response = acc.model_dump()
    
    return JSONResponse(content=response, headers={"Access-Control-Allow-Origin": "same-origin"})