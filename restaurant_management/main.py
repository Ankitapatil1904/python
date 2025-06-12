# main.py

from tkinter import Tk
from gui import RestaurantGUI
from database import create_tables, add_menu_item

def preload_menu():
   
    add_menu_item(1, "Pizza", 12.99)
    add_menu_item(2, "Burger", 8.99)
    add_menu_item(3, "Pasta", 10.99)
    add_menu_item(4, "Coke", 1.99)
    add_menu_item(5, "Salad", 5.99)

def main():
   
    create_tables()
    preload_menu()

   
    root = Tk()
    app = RestaurantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
