import psycopg2

DB_NAME = "dbname=bank2"


def drop():
    conn = psycopg2.connect(DB_NAME)
    cursor = conn.cursor()

    drop_clients = """
    DROP TABLE IF EXISTS clients
    """
    cursor.execute(drop_clients)
    conn.commit()

    conn.close()


def create():
    conn = psycopg2.connect(DB_NAME)
    cursor = conn.cursor()

    create_clients = """
    CREATE TABLE IF NOT EXISTS clients(
    id SERIAL PRIMARY KEY,
    username VARCHAR(128),
    password VARCHAR(128),
    balance REAL DEFAULT 0,
    message TEXT)
    """

    cursor.execute(create_clients)
    conn.commit()

    conn.close()
