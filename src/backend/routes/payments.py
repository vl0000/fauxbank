from typing import Annotated

from database.models import Token, TransactionIn, AccountOut, Transaction
from fastapi import APIRouter, Depends, Body, Request, HTTPException

from .account import oauth2_scheme, get_current_user

router = APIRouter(prefix="/api")

@router.post("/payments")
async def transfer(user: Annotated[AccountOut, Depends(get_current_user)],payment: Annotated[TransactionIn, Body()], req: Request):
    transaction = payment.model_dump()
    transaction.update({"payer": user.number})
    transaction = Transaction(**transaction)
    try:
        transaction.create()
    except Exception as e:
        print(e)
        raise HTTPException(406)
    finally:
        return "success"


@router.get("/payments")
def get_transactions(user: Annotated[AccountOut, Depends(get_current_user)]) -> list[tuple]:
    return user.get_all_transactions()