from os import environ
from sqlalchemy import MetaData, Table, Column, BigInteger, String, Float, ForeignKey, DateTime, Index, create_engine

engine = create_engine(environ["POSTGRES_URL"], connect_args={"ssl_context": True})


meta = MetaData()

accounts = Table(
    "accounts",
    meta,
    Column("name", String(32), nullable=False),
    Column("number", BigInteger, unique=True, nullable=False, primary_key=True),
    Column("email", String(128), unique=True, nullable=False),
    # 60 characters is the maximum due to this column being intended for bcrypt
    Column("password", String(60), nullable=False),
    Column("salt", String(24), nullable=False)
)

transactions = Table(
    "transactions",
    meta,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("payer", BigInteger, ForeignKey("accounts.number", ondelete="SET NULL")),
    Column("payee", BigInteger, ForeignKey("accounts.number", ondelete="SET NULL")),
    Column("amount", Float, nullable=False, default=0.0),
    Column("date", DateTime(timezone=True)),
    Index("idx_datetime", "date")
)