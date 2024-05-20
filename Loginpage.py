from tkinter import *
from tkinter import messagebox
import subprocess

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        root.destroy()
        process = subprocess.Popen(["python", "Firstpage.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = Tk()
root.title("Login System")
root.geometry("300x200")

Label(root, text="Username").pack(pady=5)
username_entry = Entry(root)
username_entry.pack(pady=5)

Label(root, text="Password").pack(pady=5)
password_entry = Entry(root, show='*')
password_entry.pack(pady=5)

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
