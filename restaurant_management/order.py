# order.py
from database import get_menu

def take_order():
    order = []
    items = {item[0]: {"name": item[1], "price": item[2]} for item in get_menu()}
    while True:
        try:
            item_id = int(input("Enter item number (0 to finish): "))
            if item_id == 0:
                break
            if item_id in items:
                quantity = int(input(f"Enter quantity for {items[item_id]['name']}: "))
                order.append((item_id, quantity))
            else:
                print("Item not found in menu.")
        except ValueError:
            print("Please enter a valid number.")
    return order
