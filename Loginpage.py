import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def initialize_db():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if not username or not password:
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful")
        reg_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()

def open_registration_window():
    global reg_window, reg_username_entry, reg_password_entry
    reg_window = Toplevel(root)
    reg_window.title("Register")
    reg_window.geometry("300x200")

    Label(reg_window, text="Username").pack(pady=5)
    reg_username_entry = Entry(reg_window)
    reg_username_entry.pack(pady=5)

    Label(reg_window, text="Password").pack(pady=5)
    reg_password_entry = Entry(reg_window, show='*')
    reg_password_entry.pack(pady=5)

    Button(reg_window, text="Register", command=register_user).pack(pady=20)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        root.destroy()
        subprocess.Popen(["python", "Firstpage.py"])
    else:
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            root.destroy()
            subprocess.Popen(["python", "Firstpage.py"])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

initialize_db()

root = Tk()
root.title("Login System")
root.geometry("300x250")
root.configure(bg="#3E4149")

Label(root, text="Username").pack(pady=5)
username_entry = Entry(root)
username_entry.pack(pady=5)

Label(root, text="Password").pack(pady=5)
password_entry = Entry(root, show='*')
password_entry.pack(pady=5)

Button(root, text="Login", command=login).pack(pady=20)
Button(root, text="Register", command=open_registration_window).pack(pady=5)

root.mainloop()
