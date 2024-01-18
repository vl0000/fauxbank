from typing import Annotated, Union

from database.models import AccountInDb, Token, AccountOut

from fastapi import APIRouter, Query, Form, Depends, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/account/token")

router = APIRouter(prefix="/api/account")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> AccountOut:
    try:
        number = Token.decode(token).get("sub")
    except:
        raise HTTPException(401, "Expired token")

    user = AccountInDb.get_user_safe(number)
    return user

@router.get("/me")
def get_account(user: Annotated[AccountOut, Depends(get_current_user)]):
    response = user.model_dump()
    return JSONResponse(content=response)

@router.post("/token", response_model=Token)
def login(response: Response,formData: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = AccountInDb.authenticate(formData.username, formData.password)
    if user:
        # The email is the 5th element in the returned tuple
        access_token = Token.generate_token(data={"sub": f"{user['number']}"})
    else:
        raise HTTPException(status_code=404, detail="User not found")

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=Token)
def signup(full_name: Annotated[str, Form()],email: Annotated[str, Form()], password: Annotated[str, Form()]):

    #TODO Implement validation
    user = AccountInDb(full_name=full_name, email=email, password=password)
    user.create()

    access_token = Token.generate_token(data={"sub": f"{user['number']}"})
    return {"access_token": access_token, "token_type": "bearer"}
