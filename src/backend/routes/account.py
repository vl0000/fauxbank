from typing import Annotated

from database.models import AccountInDb

from fastapi import APIRouter, Query, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(dependencies=[Depends(oauth2_scheme)])

acc = {
    "full_name": "fulano"
}

@router.get("/api/account/{id}")
def get_account(id: int | None, query: Annotated[list[str], Query()] = None):
    response = dict()
    if query:
        for q in query:
            response[q] = acc[q]
    else:
        response = acc
    
    return JSONResponse(content=response)

@router.post("/api/account/token")
def login(formData: Annotated[OAuth2PasswordRequestForm, Depends()]):

    print(formData.username,formData.password)
    #TODO Actual login
    if formData and AccountInDb.get_user(email=formData.username):
        return { "success" : True }

@router.post("/api/signup")
def signup(full_name: Annotated[str, Form()],email: Annotated[str, Form()], password: Annotated[str, Form()]):

    #TODO Implement validation
    user = AccountInDb(full_name=full_name, email=email, password=password)
    user.create()
    return {"success" : True }
