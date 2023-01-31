import psycopg2

class DBConnection:
    conn = None
    cur = None

    def __init__(self):
        pass

    @staticmethod
    def connect_db() -> None:
        conn = psycopg2.connect(
            'dbname=bajaj user=postgres password=unlockdb'
        )
        cur = conn.cursor()
        
    @staticmethod
    def insert_db(table: str, f1: str, f2: str, f3: str) -> None:
        DBConnection.cur.execute('insert into ' + table + ' ()')