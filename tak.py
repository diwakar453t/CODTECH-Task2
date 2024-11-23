import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

users = {"admin": "pass@123"}
inventory = {}

def authenticate_user():
    username = simpledialog.askstring("Login", "Enter your username:")
    password = simpledialog.askstring("Login", "Enter your password:", show="*")

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password!")
        root.destroy()

def add_product():
    name = simpledialog.askstring("Add Product", "Enter product name:")
    if not name:
        messagebox.showerror("Error", "Product name cannot be empty!")
        return
    try:
        quantity = int(simpledialog.askstring("Add Product", "Enter product quantity:"))
        price = float(simpledialog.askstring("Add Product", "Enter product price:"))
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity or price!")
        return

    inventory[name] = {"quantity": quantity, "price": price}
    messagebox.showinfo("Success", f"Product '{name}' added successfully!")

def edit_product():
    name = simpledialog.askstring("Edit Product", "Enter product name to edit:")
    if name not in inventory:
        messagebox.showerror("Error", f"Product '{name}' not found!")
        return

    try:
        new_quantity = int(simpledialog.askstring("Edit Product", "Enter new quantity:"))
        new_price = float(simpledialog.askstring("Edit Product", "Enter new price:"))
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity or price!")
        return

    inventory[name]["quantity"] = new_quantity
    inventory[name]["price"] = new_price
    messagebox.showinfo("Success", f"Product '{name}' updated successfully!")

def delete_product():
    name = simpledialog.askstring("Delete Product", "Enter product name to delete:")
    if name in inventory:
        del inventory[name]
        messagebox.showinfo("Success", f"Product '{name}' deleted successfully!")
    else:
        messagebox.showerror("Error", f"Product '{name}' not found!")

def view_inventory():
    if not inventory:
        messagebox.showinfo("Inventory", "No products in inventory!")
        return

    inventory_details = "Inventory Details:\n"
    for name, details in inventory.items():
        inventory_details += f"{name} - Quantity: {details['quantity']}, Price: ${details['price']:.2f}\n"

    messagebox.showinfo("Inventory", inventory_details)

def generate_low_stock_report():
    low_stock_products = [name for name, details in inventory.items() if details["quantity"] < 5]
    if low_stock_products:
        messagebox.showinfo("Low Stock Report", "Low Stock Products:\n" + "\n".join(low_stock_products))
    else:
        messagebox.showinfo("Low Stock Report", "All products have sufficient stock!")

def main_menu():
    menu_window = tk.Tk()
    menu_window.title("Inventory Management System")

    tk.Label(menu_window, text="Inventory Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(menu_window, text="Add Product", command=add_product, width=20).pack(pady=5)
    tk.Button(menu_window, text="Edit Product", command=edit_product, width=20).pack(pady=5)
    tk.Button(menu_window, text="Delete Product", command=delete_product, width=20).pack(pady=5)
    tk.Button(menu_window, text="View Inventory", command=view_inventory, width=20).pack(pady=5)
    tk.Button(menu_window, text="Low Stock Report", command=generate_low_stock_report, width=20).pack(pady=5)
    tk.Button(menu_window, text="Exit", command=menu_window.destroy, width=20).pack(pady=5)

    menu_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    authenticate_user()
