import sqlite3

from contextlib import contextmanager
from queue import Queue

from os import environ

class ConnectionPool:
    def __init__(self, DB_name: str) -> None:
        self.DB_name = DB_name
        self.pool = Queue(maxsize=8)

        for _ in range(8):
            conn = sqlite3.connect(DB_name, check_same_thread=False)
            self.pool.put(conn)

    
    def _get_connection(self) -> sqlite3.Connection | None:

        try:
            return self.pool.get(timeout=12.0)
        except Exception as e:
            print(e)
    
    def _disconnect(self, connection: sqlite3.Connection) -> None:
        self.pool.put(connection)

    @contextmanager
    def connection(self):
        CONN = self._get_connection()
        try:
            yield CONN
        finally:
            self._disconnect(CONN)

class Database:
    def __init__(self, pool: ConnectionPool) -> None:
        self.pool = pool
    
    def query(self, query: str, data: tuple = None) -> list[dict] | None:
        with self.pool.connection() as CONN:
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
                if result:
                    return result
        

connection_pool = ConnectionPool("db.sqlite")

DB = Database(connection_pool)



