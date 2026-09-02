import inventory

MENU = """
1. Add Item
2. Add Stock
3. Remove Stock
4. Place Order
5. Cancel Order
6. View Low Stock Report
7. View Most Ordered Item
8. View All Items
9. Quit
"""

def check_integer(label):
    try:
        return int(input(label))
    except ValueError:
        print("Please enter a whole number:")
        return None
    
def check_float(label):
    try:
        return float(input(label))
    except ValueError:
        print("Please enter a number.")
        return None  


def add_item_flow(conn):
    name = input("Enter the name of the item:").strip()
    stock = check_integer("Enter the stock of the item:")
    price = check_float("Enter the price of the item:")
    if stock is None or price is None:
        return
    try:
        inventory.add_items(conn,name, stock, price)
        print("Item added successfully")
    except ValueError as e:
        print(f"Could not add an item due to {e}")
        
    
def add_stock_flow(conn):
    item = input("Enter the name or the id of the item::").strip()
    stock = check_integer("Enter the stock you want to add::")
    if stock is None:
        return
    try:
        inventory.add_stock(conn,item, stock)
        print("Stock Added successfully.")
    except ValueError as e:
        print(f"Could not add stock due to {e}")
        
def remove_stock_flow(conn):
    item = input("Enter the name or the id of the item::").strip()
    stock = check_integer("enter the stock you want to remove:::")
    if stock is None:
        return
    try:
        inventory.remove_stock(conn,item, stock)
        print("Stock removed successfully")
    except ValueError as e:
        print(f"Could not remove an item due to {e}")
        
def place_order_flow(conn):
    item = input("Enter the name of the item you want to order::").strip()
    quantity = check_integer("Enter the quantity of the item::")
    if quantity is None:
        return
    try:
        inventory.place_order(conn,item, quantity)
        print("Order placed Successfully.")
    except ValueError as e:
        print(f"Could not place an order due to {e}")
        
def cancel_order_flow(conn):
    order_id = input("Enter the order id you want to cancel::")
    try:
        inventory.cancel_order(conn,order_id)
        print("Order cancelled Successfully.")
    except ValueError as e:
        print(f"Order could not be cancelled due to {e}")
        
def get_low_stock_report_flow(conn):
    threshold = check_integer("Enter the threshold::")
    if threshold is None:
        return
    try:
        items = inventory.get_low_stock_report(conn,threshold)
        print("Low Stock Report Retrieved Successfully.")
        print(items)
    except ValueError as e:
        print(f"Could not get low stock report due to {e}")
        
def get_most_ordered_flow(conn):
    try:
        items = inventory.get_most_ordered_items(conn)
        print("The most ordered items retrieved successfully.")
        print(items)
    except ValueError as e:
        print(f"COuld not get the most ordered items due to {e}")
        
def get_all_items_flow(conn):
    try:
        items = inventory.get_all_items(conn)
        print("All Items retreived successfully.")
        print(items)
    except ValueError as e:
        print(f"Could not get all items due to {e}")
        
    
    


def ims_flow(conn):
    print("This is CLI Based Inventory Management system developed by Kanchan Basnet")
    while True:
        print(MENU)
        option=input("Please choose an option:").strip()
        if option == "1":
            add_item_flow(conn)
        elif option == "2":
            add_stock_flow(conn)
        elif option == "3":
            remove_stock_flow(conn)
        elif option == "4":
            place_order_flow(conn)
        elif option == "5":
            cancel_order_flow(conn)
        elif option == "6":
            get_low_stock_report_flow(conn)
        elif option == "7":
            get_most_ordered_flow(conn)
        elif option == "8":
            get_all_items_flow(conn)
        elif option == "9":
            print("Bye! Have a nice Day!")
            break
        else:
            print("Invalid option. Please try again!!!")
            continue
            



