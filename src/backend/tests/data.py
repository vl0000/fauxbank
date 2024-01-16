from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite+pysqlite:///:memory:")

fulano = {
    "name": "Fulano de Tal",
    "email": "fulanodetal@example.com.br",
    "password": "pindamonhangaba"
}
john = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "poughkeepsie"
}
payment = {
    "id": 1,
    "payer": 321,
    "payee": 1234,
    "amount": 100.0
}

def query(stmt):
    with engine.connect() as conn:
        res = conn.execute(stmt)
        if res:
            return res