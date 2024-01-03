from typing import Annotated

from database.models import AccountInDb, Token

from fastapi import APIRouter, Query, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(dependencies=[])

acc = {
    "full_name": "fulano"
}

@router.get("/api/account/{id}")
def get_account(id: int | None, token: Annotated[oauth2_scheme, Depends()], query: Annotated[list[str], Query()] = None):
    response = dict()
    if query:
        for q in query:
            response[q] = acc[q]
    else:
        response = acc
    
    return JSONResponse(content=response)

@router.post("/api/account/token", response_model=Token)
def login(formData: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print("here")
    user = AccountInDb.authenticate(formData.username, formData.password)
    print(user)
    if user:
        # The email is the 5th element in the returned tuple
        access_token = Token.generate_token(data={"sub": user[5]})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/api/signup")
def signup(full_name: Annotated[str, Form()],email: Annotated[str, Form()], password: Annotated[str, Form()]):

    #TODO Implement validation
    user = AccountInDb(full_name=full_name, email=email, password=password)
    user.create()
    return {"success" : True }
