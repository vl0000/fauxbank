from typing import Annotated

from database.models import Token, Transaction, AccountOut
from fastapi import APIRouter, Depends, Body

from .account import oauth2_scheme, get_current_user

router = APIRouter(prefix="/api")

@router.post("/payments")
def payments(user: Annotated[AccountOut, Depends(get_current_user)], transaction: Annotated[Transaction, Body()]):
    return transaction