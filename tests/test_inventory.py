import pytest

import inventory


def test_add_item_success(conn):
    inventory.add_items(conn, "Laptop", 10, 2000)
    item = inventory.get_item(conn, "Laptop")
    assert item is not None
    assert item["name"] == "Laptop"
    assert item["stock"] == 10
    assert item["price"] == 2000


def test_add_item_duplicate_raises_error(conn):
    inventory.add_items(conn, "Laptop", 10, 2000)
    with pytest.raises(ValueError):
        inventory.add_items(conn, "Laptop", 5, 3000)


def test_add_item_negative_stock_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.add_items(conn, "Macbook Pro", -1, 4000)


def test_add_item_negative_price_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.add_items(conn, "Macbook Pro", 5, -4000.56)


def test_get_item_returns_none_when_not_found(conn):
    result = inventory.get_item(conn, "AirPods")
    assert result is None


def test_get_item_by_name(conn):
    inventory.add_items(conn, "SmartWatch", 20, 400)
    item = inventory.get_item(conn, "SmartWatch")
    assert item["name"] == "SmartWatch"


def test_add_stock_success(conn):
    inventory.add_items(conn, "Keyboard", 10, 200)
    inventory.add_stock(conn, "Keyboard", 5)
    item = inventory.get_item(conn, "Keyboard")
    assert item["stock"] == 15


def test_add_stock_item_not_found_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.add_stock(conn, "Printer", 5)


def test_add_stock_zero_quantity_raises_error(conn):
    inventory.add_items(conn, "Keyboard", 10, 2.0)
    with pytest.raises(ValueError):
        inventory.add_stock(conn, "Keyboard", 0)


def test_remove_stock_success(conn):
    inventory.add_items(conn, "Mouse", 10, 1.0)
    inventory.remove_stock(conn, "Mouse", 3)
    item = inventory.get_item(conn, "Mouse")
    assert item["stock"] == 7


def test_remove_stock_item_not_found_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.remove_stock(conn, "Scanner", 5)


def test_remove_stock_more_than_available_raises_error(conn):
    inventory.add_items(conn, "Mouse", 5, 1.0)
    with pytest.raises(ValueError):
        inventory.remove_stock(conn, "Mouse", 20)


def test_remove_stock_zero_quantity_raises_error(conn):
    inventory.add_items(conn, "Mouse", 5, 1.0)
    with pytest.raises(ValueError):
        inventory.remove_stock(conn, "Mouse", 0)


def test_place_order_success(conn):
    inventory.add_items(conn, "MacBook Pro", 20, 1500)
    result = inventory.place_order(conn, "MacBook Pro", 3)
    assert result["quantity"] == 3
    assert result["total_price"] == 4500
    item = inventory.get_item(conn, "MacBook Pro")
    assert item["stock"] == 17


def test_place_order_item_not_found_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.place_order(conn, "NotFoundDevice", 1)


def test_place_order_zero_quantity_raises_error(conn):
    inventory.add_items(conn, "MacBook Pro", 20, 1500)
    with pytest.raises(ValueError):
        inventory.place_order(conn, "MacBook Pro", 0)


def test_place_order_insufficient_stock_raises_error(conn):
    inventory.add_items(conn, "MacBook Pro", 5, 1500)
    with pytest.raises(ValueError):
        inventory.place_order(conn, "MacBook Pro", 10)


def test_cancel_order_success(conn):
    inventory.add_items(conn, "iPad", 10, 800)
    inventory.place_order(conn, "iPad", 3)
    cur = conn.cursor()
    cur.execute("SELECT order_id FROM orders LIMIT 1")
    real_order_id = cur.fetchone()[0]
    inventory.cancel_order(conn, real_order_id)
    item = inventory.get_item(conn, "iPad")
    assert item["stock"] == 10


def test_cancel_order_not_found_raises_error(conn):
    with pytest.raises(ValueError):
        inventory.cancel_order(conn, 9999)

def test_get_low_stock_report(conn):
    inventory.add_items(conn, "USB Hub", 2, 30)
    inventory.add_items(conn, "Monitor", 50, 400)
    result = inventory.get_low_stock_report(conn, 10)
    assert len(result) == 1
    assert result[0]["name"] == "USB Hub"


def test_get_low_stock_report_empty_when_all_fine(conn):
    inventory.add_items(conn, "Monitor", 50, 400)
    result = inventory.get_low_stock_report(conn, 10)
    assert result == []

def test_get_most_ordered_items(conn):
    inventory.add_items(conn, "Headphones", 100, 150)
    inventory.add_items(conn, "Speaker", 100, 200)
    inventory.place_order(conn, "Headphones", 10)
    inventory.place_order(conn, "Speaker", 5)
    result = inventory.get_most_ordered_items(conn)
    assert result[0]["name"] == "Headphones"
    assert result[0]["total_ordered"] == 10


def test_get_most_ordered_items_empty_when_no_orders(conn):
    result = inventory.get_most_ordered_items(conn)
    assert result == []


def test_get_all_items_returns_all(conn):
    inventory.add_items(conn, "Drone", 5, 999)
    inventory.add_items(conn, "Tablet", 10, 600)
    result = inventory.get_all_items(conn)
    assert len(result) == 2


def test_get_all_items_empty_db(conn):
    result = inventory.get_all_items(conn)
    assert result == []
