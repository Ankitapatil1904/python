# bill.py
from database import get_menu, save_order

def generate_bill(order):
    items = {item[0]: {"name": item[1], "price": item[2]} for item in get_menu()}
    total = 0
    print("\n----- BILL -----")
    for item_id, quantity in order:
        item = items[item_id]
        item_total = item['price'] * quantity
        total += item_total
        print(f"{item['name']} x{quantity} = ₹{item_total:.2f}")
        save_order(item_id, quantity, item_total)
    print("-----------------")
    print(f"Total Amount: ₹{total:.2f}")
    print("-----------------")
    return total
