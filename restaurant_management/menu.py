# menu.py
from database import get_menu

def display_menu():
    items = get_menu()
    print("\n------ MENU ------")
    for item in items:
      print(f"{item[0]}. {item[1]} - ₹{item[2]:.2f}")

