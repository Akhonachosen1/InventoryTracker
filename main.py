import os
import tkinter as tk
from tkinter import messagebox

# Load inventory data from file
def load_inventory(file_name="inventory_data.txt"):
    inventory = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                name, quantity, price = line.strip().split(",")
                inventory.append({"name": name, "quantity": int(quantity), "price": float(price)})
    return inventory

# Save inventory data to file
def save_inventory(inventory, file_name="inventory_data.txt"):
    with open(file_name, "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['quantity']},{item['price']}\n")

# Add new item to inventory
def add_item():
    name = name_entry.get().strip()
    try:
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for quantity and price.")
        return
    
    inventory.append({"name": name, "quantity": quantity, "price": price})
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    update_inventory_display()
    messagebox.showinfo("Success", f"Item {name} added to inventory.")

# Update item quantity in inventory
def update_item():
    name = update_name_entry.get().strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            try:
                new_quantity = int(update_quantity_entry.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for quantity.")
                return
            item['quantity'] = new_quantity
            update_quantity_entry.delete(0, tk.END)
            update_inventory_display()
            messagebox.showinfo("Success", f"Updated {name} to {new_quantity} units.")
            return
    messagebox.showerror("Item Not Found", f"Item {name} not found in inventory.")

# Display inventory in the UI
def update_inventory_display():
    inventory_listbox.delete(0, tk.END)
    for item in inventory:
        inventory_listbox.insert(tk.END, f"{item['name']} | Quantity: {item['quantity']} | Price: ${item['price']:.2f}")

# Save and exit the program
def save_and_exit():
    save_inventory(inventory)
    root.quit()

# Load existing inventory
inventory = load_inventory()

# Create the main window
root = tk.Tk()
root.title("Inventory Manager")

# UI Elements for Adding Items
name_label = tk.Label(root, text="Item Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=5)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=2, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# UI Elements for Updating Items
update_name_label = tk.Label(root, text="Item Name to Update:")
update_name_label.grid(row=4, column=0, padx=10, pady=5)
update_name_entry = tk.Entry(root)
update_name_entry.grid(row=4, column=1, padx=10, pady=5)

update_quantity_label = tk.Label(root, text="New Quantity:")
update_quantity_label.grid(row=5, column=0, padx=10, pady=5)
update_quantity_entry = tk.Entry(root)
update_quantity_entry.grid(row=5, column=1, padx=10, pady=5)

update_button = tk.Button(root, text="Update Item", command=update_item)
update_button.grid(row=6, column=0, columnspan=2, pady=10)

# Inventory Listbox and Display
inventory_listbox = tk.Listbox(root, width=50, height=10)
inventory_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Buttons for saving and quitting
save_exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)
save_exit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Populate the display with existing inventory
update_inventory_display()

# Start the main event loop
root.mainloop()
