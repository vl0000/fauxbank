import sqlite3
import threading

from queue import Queue

from os import environ

class ConnectionPool:
    def __init__(self, DB_name: str) -> None:
        self.DB_name = DB_name
        self.pool = Queue(maxsize=2)

        for _ in range(2):
            self.pool.put(
                sqlite3.connect(DB_name)
            )
    
    def get_connection(self) -> None:
        if not self.pool.empty():
            return self.pool.get(timeout=5.0)
        else:
            raise RuntimeError("The connection pool is empty")
    
    def disconnect(self, connection: sqlite3.Connection) -> None:
        self.pool.put(connection)


class Database:
    def __init__(self, pool: ConnectionPool) -> None:
        self.pool = pool
    
    def query(self, query: str, data: tuple = None) -> list[dict] | None:
        CONN = self.pool.get_connection()
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
            self.pool.disconnect(CONN)
            if result:
                return result
    

connection_pool = ConnectionPool("db.sqlite")

DB = Database(connection_pool)



