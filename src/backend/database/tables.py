from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey, DateTime,Date, Index, create_engine

engine = create_engine("sqlite+pysqlite:///db.sqlite")


meta = MetaData()

accounts = Table(
    "accounts",
    meta,
    Column("name", String(32), nullable=False),
    Column("number", Integer, unique=True, nullable=False, primary_key=True),
    Column("email", String(128), unique=True, nullable=False),
    # 60 characters is the maximum due to this column being intended for bcrypt
    Column("password", String(60), nullable=False),
    Column("salt", String(21), nullable=False)
)

transactions = Table(
    "transactions",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("payer", Integer, ForeignKey("accounts.number", ondelete="SET NULL")),
    Column("payee", Integer, ForeignKey("accounts.number", ondelete="SET NULL")),
    Column("amount", Float, nullable=False, default=0.0),
    Column("date", DateTime(timezone=True)),
    Index("idx_datetime", "date")
)

cards = Table(
    "cards",
    meta,
    Column("number", Integer, primary_key=True),
    Column("holder", ForeignKey("accounts.number", ondelete="CASCADE"), nullable=False),
    Column("cvv", Integer, nullable=False),
    Column("expiration", Date, nullable=False),
    Index("idx_expiration", "expiration")
)