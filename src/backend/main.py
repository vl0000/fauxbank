from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import account, payments

app = FastAPI()

app.include_router(account.router)
app.include_router(payments.router)

# Temporary and for TESTING PURPOSES ONLY!!!!
# TODO Fix this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
