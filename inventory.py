from db_conection import set_connection
from db_setup import DATABASE

connection = set_connection(DATABASE)
cur = connection.cursor()


def get_item(identifier):
    cur.execute(
        """SELECT * FROM items WHERE name = ? OR item_id = ?""",
        (identifier, identifier),
    )
    fetched_items = cur.fetchone()
    if fetched_items is None:
        return None
    return {
        "item_id": fetched_items[0],
        "name": fetched_items[1],
        "stock": fetched_items[2],
        "price": fetched_items[3],
    }


def add_items(name, stock, price):
    if get_item(name):
        raise ValueError(f"Item {name} already exist.")
    if stock < 0:
        raise ValueError("Stock cannot be negative.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    cur.execute(
        """
                INSERT INTO items (name, stock, price) VALUES (?,?,?)
                """,
        (name, stock, price),
    )
    connection.commit()


def add_stock(identifier, stock):
    item = get_item(identifier)
    if item is None:
        raise ValueError(f"Item '{identifier}' does not exist")
    if stock <= 0:
        raise ValueError("Quantity must be positive")
    new_stock = item["stock"] + stock
    cur.execute("UPDATE items SET stock = ? WHERE item_id = ?", (new_stock, item["item_id"]))
    connection.commit()


def get_all_items():
    cur.execute("""SELECT * FROM items""")
    items = cur.fetchall()
    return [
        {"item_id": item[0], "name": item[1], "stock": item[2], "price": item[3]}
        for item in items
    ]


def remove_stock(identifier, stock):
    item = get_item(identifier)
    if item is None:
        raise ValueError(f"Item '{identifier}' does not exist")
    if stock <= 0:
        raise ValueError("Quantity must be positive")
    if stock > item["stock"]:
        raise ValueError("Insufficient stock")
    new_stock = item["stock"] - stock
    cur.execute("UPDATE items SET stock = ? WHERE item_id = ?", (new_stock, item["item_id"]))
    connection.commit()


def get_low_stock_report(threshold):
    cur.execute("SELECT * FROM items WHERE stock < ?", (threshold,))
    items = cur.fetchall()
    return [
        {"item_id": item[0], "name": item[1], "stock": item[2], "price": item[3]}
        for item in items
    ]


def place_order(name, quantity):
    item = get_item(name)
    if item is None:
        raise ValueError(f"Item '{name}' does not exist")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if quantity > item["stock"]:
        raise ValueError("There is not enough stock available")

    new_stock = item["stock"] - quantity
    total_price = quantity * item["price"]

    cur.execute(
        "UPDATE items SET stock = ? WHERE item_id = ?", (new_stock, item["item_id"])
    )
    cur.execute(
        "INSERT INTO orders (item_id, quantity, total_price) VALUES (?, ?, ?)",
        (item["item_id"], quantity, total_price),
    )
    connection.commit()

    return {
        "item_id": item["item_id"],
        "name": item["name"],
        "quantity": quantity,
        "total_price": total_price,
    }


def get_order(order_id):
    cur.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    row = cur.fetchone()
    if row is None:
        return None
    return {
        "order_id": row[0],
        "item_id": row[1],
        "quantity": row[2],
        "total_price": row[3],
        "order_date": row[4],
    }


def cancel_order(order_id):
    order = get_order(order_id)
    if order is None:
        raise ValueError(f"Order {order_id} does not exist")

    cur.execute(
        "UPDATE items SET stock = stock + ? WHERE item_id = ?",
        (order["quantity"], order["item_id"]),
    )
    cur.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
    connection.commit()

    return order


def get_most_ordered_items():
    cur.execute("""
        SELECT items.item_id, items.name, SUM(orders.quantity) AS total_ordered
        FROM orders
        JOIN items ON orders.item_id = items.item_id
        GROUP BY orders.item_id
        ORDER BY total_ordered DESC
    """)
    rows = cur.fetchall()
    return [{"item_id": r[0], "name": r[1], "total_ordered": r[2]} for r in rows]
