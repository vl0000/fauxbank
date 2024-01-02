from .config import DB


DB.query("""CREATE TABLE IF NOT EXISTS account(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR(64),
               balance FLOAT,
               agency INT,
               number INT,
               email VARCHAR(128) UNIQUE,
                password VARCHAR(64),
                salt VARCHAR(24)
               )""")

    
