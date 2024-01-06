from typing import Annotated

from database.models import AccountInDb, Token

from fastapi import APIRouter, Query, Form, Depends, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/account/token")

router = APIRouter(prefix="/api/account")

acc = {
    "full_name": "fulano"
}

# This is a security issure right now, but this route wont even exist in the future anyways.
# It is for testing purposes only
@router.get("/{id}")
def get_account(id: int | None, token: Annotated[oauth2_scheme, Depends()], query: Annotated[list[str], Query()] = None):
    response = dict()
    if query:
        for q in query:
            response[q] = acc[q]
    else:
        response = acc
    
    return JSONResponse(content=response)

@router.post("/token", response_model=Token)
def login(response: Response,formData: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = AccountInDb.authenticate(formData.username, formData.password)
    if user:
        # The email is the 5th element in the returned tuple
        access_token = Token.generate_token(data={"sub": user[5]})
    else:
        raise HTTPException(status_code=404, detail="User not found")

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=Token)
def signup(full_name: Annotated[str, Form()],email: Annotated[str, Form()], password: Annotated[str, Form()]):

    #TODO Implement validation
    user = AccountInDb(full_name=full_name, email=email, password=password)
    user.create()

    access_token = Token.generate_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
