import inventory


def add_item_flow():
    name = input("Enter the name of the item::: ").strip()
    try:
        stock = int(input("Enter the quantity of the item::").strip())
        price = float(input("Enter the price of the item::").strip())
    except ValueError:
        print("Invalid stock or price!!!")
        return
    try:
        inventory.add_items(name, stock, price)
        print("Item added successfully.")

    except ValueError as e:
        print(f"Could not add item due to {e}")


def add_stock_flow():
    item = input("Enter the name or the id of the item::").strip()
    stock = input("Enter the stock you want to add::").strip()
    if stock.isdigit():
        stock = int(stock)
        inventory.add_stock(item, stock)
        print("Stock added successfully.")
    else:
        raise ValueError("Stock must be a number.")


def main():

    print("This is the Inventory management system.")
    user_input = input(
        "What would you like to do? Please press 1 to add the item and q to quit and 2 to edit item>>>>>"
    )
    if user_input == "1":
        add_item_flow()
    elif user_input == "2":
        add_stock_flow()
    elif user_input == "3":
        all_items = inventory.get_all_items()
        print(all_items)


if __name__ == "__main__":
    main()
