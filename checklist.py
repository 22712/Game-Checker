import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "list_data.json"

class Item:
    def __init__(self, name, quantity, collected=False):
        self.name = name
        self.quantity = quantity
        self.collected = collected

    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity, "collected": self.collected}

    @staticmethod
    def from_dict(data):
        return Item(data["name"], data["quantity"], data["collected"])

class MemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Check list")
        self.categories = self.load_data()
        if not self.categories:
            self.categories = {"Default": []}
        self.current_category = tk.StringVar(value=list(self.categories.keys())[0])

        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side='left', fill='y', padx=10)

        tk.Label(left_frame, text="Category").pack()
        self.category_menu = tk.OptionMenu(left_frame, self.current_category, *self.categories.keys(), command=self.display_items)
        self.category_menu.pack()

        self.new_category_entry = tk.Entry(left_frame)
        self.new_category_entry.pack()
        tk.Button(left_frame, text="Add Category", command=self.add_category).pack(pady=10)
        tk.Button(left_frame, text="Delete Category", command=self.delete_category).pack(pady=10)

        tk.Label(left_frame, text="Item Name").pack()
        self.name_entry = tk.Entry(left_frame)
        self.name_entry.pack()

        tk.Label(left_frame, text="Quantity").pack()
        self.quantity_entry = tk.Entry(left_frame)
        self.quantity_entry.pack()
        tk.Button(left_frame, text="Add Item", command=self.add_item).pack(pady=10)

        self.items_frame = tk.Frame(main_frame)
        self.items_frame.pack(side='right', fill='both', expand=True)

        self.display_items()

    def add_category(self):
        new_category = self.new_category_entry.get().strip()
        if not new_category:
            messagebox.showerror("Input Error", "Category name cannot be empty.")
            return
        if new_category in self.categories:
            messagebox.showerror("Input Error", "Category already exists.")
            return

        self.categories[new_category] = []
        self.current_category.set(new_category)
        self.update_category_menu()
        self.new_category_entry.delete(0, tk.END)
        self.save_data()

    def delete_category(self):
        current_category = self.current_category.get()
        if current_category == "Default":
            messagebox.showerror("Delete Error", "Cannot delete the default category.")
            return

        del self.categories[current_category]
        self.current_category.set(list(self.categories.keys())[0])
        self.update_category_menu()
        self.save_data()

    def update_category_menu(self):
        menu = self.category_menu["menu"]
        menu.delete(0, "end")
        for category in self.categories:
            menu.add_command(label=category, command=lambda c=category: self.current_category.set(c) or self.display_items())

    def add_item(self):
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not name or not quantity:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number")
            return

        item = Item(name, quantity)
        self.categories[self.current_category.get()].append(item)
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.display_items()
        self.save_data()

    def delete_item(self, item):
        self.categories[self.current_category.get()].remove(item)
        self.display_items()
        self.save_data()

    def display_items(self, *args):
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        current_items = self.categories.get(self.current_category.get(), [])
        for item in current_items:
            item_frame = tk.Frame(self.items_frame)
            item_frame.pack(fill='x', pady=2)

            item_label = tk.Label(item_frame, text=f"{item.name} (Quantity: {item.quantity})", anchor="w")
            item_label.pack(side="left", fill="x", expand=True)

            collected_var = tk.BooleanVar(value=item.collected)
            tk.Checkbutton(item_frame, text="Collected", variable=collected_var,
                           command=lambda i=item, v=collected_var: self.toggle_collected(i, v)).pack(side="right")

            tk.Button(item_frame, text="Delete", command=lambda i=item: self.delete_item(i)).pack(side="right")

    def toggle_collected(self, item, var):
        item.collected = var.get()
        self.save_data()

    def save_data(self):
        data = {category: [item.to_dict() for item in items] for category, items in self.categories.items()}
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                return {category: [Item.from_dict(item) for item in items] for category, items in data.items()}
        return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoApp(root)
    root.mainloop()