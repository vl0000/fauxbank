from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import account, payments

app = FastAPI()

app.include_router(account.router)
app.include_router(payments.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=["Authorization"]
)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, log_level="info")