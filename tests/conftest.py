import os
import pytest
from dotenv import load_dotenv
from db_conection import set_connection
from db_setup import run_migration

load_dotenv()


TEST_DB = os.getenv("TEST_DB", "inventory_test.db")


@pytest.fixture
def conn():
    run_migration(TEST_DB)
    connection = set_connection(TEST_DB)
    cur = connection.cursor()
    cur.execute("DELETE FROM orders")
    cur.execute("DELETE FROM items")
    connection.commit()
    yield connection
    connection.close()
