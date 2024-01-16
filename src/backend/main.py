from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import account, payments

app = FastAPI()

app.include_router(account.router)
app.include_router(payments.router)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["Options"],
    allow_headers=["Authorization"]
)
