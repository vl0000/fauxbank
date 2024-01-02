import sqlite3

from os import environ

class Database:
    def __init__(self, DB_name) -> None:
        self.DB_name = DB_name
    
    def query(self, query: str, data: tuple = None) -> list[dict] | None:
        CONN = sqlite3.connect(self.DB_name)
        CURSOR = CONN.cursor()

        try:
            if data:
                CURSOR.execute(query, data)
            else:
                CURSOR.execute(query)
        except Exception as e:
            print(e)
            CONN.rollback()

        finally:
            result = CURSOR.fetchall()
            CONN.commit()
            CURSOR.close()
            CONN.close()
            if result:
                return result
    

DB = Database("db.sqlite")



