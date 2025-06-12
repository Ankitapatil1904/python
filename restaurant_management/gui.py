import tkinter as tk
from tkinter import messagebox
from database import get_menu  

class RestaurantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME  TO MEADOWS ")
        self.root.configure(bg="#fdf6e3")

        self.menu_items = get_menu()
        self.order = {}

        self.build_menu()

 
        tk.Button(
            self.root,
            text="Generate Bill",
            command=self.generate_bill,
            bg="#8B4513",
            fg="white",
            font=('Arial', 12, 'bold'),
            padx=10,
            pady=5
        ).pack(pady=10)

    def build_menu(self):
        tk.Label(
            self.root,
            text="Select Items",
            font=('Arial', 14, 'bold'),
            bg="#fdf6e3"
        ).pack(pady=(10, 5))

        for item_id, name, price in self.menu_items:
            frame = tk.Frame(self.root, bg="#fdf6e3")
            frame.pack(anchor='w', padx=10, pady=2)

            var = tk.IntVar()
            check = tk.Checkbutton(
                frame,
                text=f"{name} - ₹{price:.2f}",
                variable=var,
                bg="#fdf6e3"
            )
            check.pack(side='left')

            qty = tk.Entry(frame, width=5)
            qty.insert(0, "0")
            qty.pack(side='left', padx=10)

            self.order[item_id] = {
                "selected": var,
                "quantity_entry": qty,
                "name": name,
                "price": price
            }

    def generate_bill(self):
        total = 0
        bill_details = "Item\tQty\tPrice\n" + "-"*30 + "\n"

        for item in self.order.values():
            if item["selected"].get():
                try:
                    qty = int(item["quantity_entry"].get())
                    if qty > 0:
                        item_total = qty * item["price"]
                        total += item_total
                        bill_details += f"{item['name']}\t{qty}\t₹{item_total:.2f}\n"
                except ValueError:
                    messagebox.showerror("Invalid Input", f"Please enter a valid quantity for {item['name']}.")

        bill_details += "-"*30 + f"\nTotal: ₹{total:.2f}"

        # Display bill
        messagebox.showinfo("Bill", bill_details)
