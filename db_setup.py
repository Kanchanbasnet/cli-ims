
import os

from dotenv import load_dotenv

from db_conection import set_connection

load_dotenv()
DATABASE = os.getenv("MAIN_DB")


ITEMS_TABLE = """
CREATE TABLE IF NOT EXISTS items(
    item_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    price REAL NOT NULL,
    CHECK (stock >= 0),
    CHECK (price >=0)
    
)
"""

ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id TEXT,
    quantity INTEGER NOT NULL,
    total_price REAL,
    order_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
)
""" 

def run_migration(databases):
    connection = set_connection(databases)
    cur = connection.cursor()
    cur.execute(ITEMS_TABLE)
    cur.execute(ORDERS_TABLE)
    connection.commit()
    connection.close()
    print(f"Database {databases} is ready for connection.")
    
    
def main():
    run_migration(DATABASE)
        
    print("Setup completed!!!!")
    
if __name__ == "__main__":
    main()
