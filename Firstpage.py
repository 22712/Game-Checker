from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk
import subprocess
import webbrowser

def return_to_main():
    pass

def return_to_previous():
    pass

def open_new_script(script_name):
    subprocess.Popen(["python", script_name])

def create_new_window(title):
    new_window = Toplevel(root)
    new_window.title(title)
    new_window.geometry("400x300")
    Label(new_window, text=f"This is the content of {title}").pack()

def change_theme_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)
        game_icons_frame.configure(bg=color)

root = Tk()
root.geometry("800x600")
root.title("Game Checker")
root.configure(bg="white")

def create_menus():
    mainmenu = Menu(root)

    mainmenu.add_command(label="Check list", command=lambda: open_new_script("checklist.py"))

    more_menu = Menu(mainmenu, tearoff=0)
    more_menu.add_command(label="Support", command=lambda: webbrowser.open("support.html"))
    more_menu.add_command(label="Contact", command=lambda: open_new_script("contact.py"))
    more_menu.add_command(label="QwQ", command=lambda: open_new_script("QwQ.py"))
    mainmenu.add_cascade(label="More", menu=more_menu)

    mainmenu.add_command(label="Change Theme Color", command=change_theme_color)

    root.config(menu=mainmenu)

def create_game_icons():
    global game_icons_frame
    game_icons_frame = Frame(root)
    game_icons_frame.pack(expand=True, fill=BOTH)
    game_icons_frame.configure(bg="white")

    image_size = (100, 100)

    game1_image = Image.open("Image/R.png").resize(image_size)
    game1_photo = ImageTk.PhotoImage(game1_image)
    game1_button = Button(game_icons_frame, image=game1_photo, text="APEX", compound=TOP, command=lambda: create_new_window("Game 1"))
    game1_button.image = game1_photo
    game1_button.grid(row=0, column=0, padx=10, pady=10)

    game1_image = Image.open("Image/mihuyou.png").resize(image_size)
    game1_photo = ImageTk.PhotoImage(game1_image)
    game1_button = Button(game_icons_frame, image=game1_photo, text="Genshen", compound=TOP, command=lambda: create_new_window("Game 1"))
    game1_button.image = game1_photo
    game1_button.grid(row=0, column=1, padx=10, pady=10)

    game2_image = Image.open("Image/TM.png").resize(image_size)
    game2_photo = ImageTk.PhotoImage(game2_image)
    game2_button = Button(game_icons_frame, image=game2_photo, text="To", compound=TOP, command=lambda: create_new_window("Game 2"))
    game2_button.image = game2_photo
    game2_button.grid(row=0, column=2, padx=10, pady=10)

    game3_image = Image.open("Image/Mincecraft.png").resize(image_size)
    game3_photo = ImageTk.PhotoImage(game3_image)
    game3_button = Button(game_icons_frame, image=game3_photo, text="Minecraft", compound=TOP, command=lambda: create_new_window("Game 3"))
    game3_button.image = game3_photo
    game3_button.grid(row=0, column=3, padx=10, pady=10)

    game2_image = Image.open("Image/OIP.png").resize(image_size)
    game2_photo = ImageTk.PhotoImage(game2_image)
    game2_button = Button(game_icons_frame, image=game2_photo, text="COD", compound=TOP, command=lambda: create_new_window("Game 2"))
    game2_button.image = game2_photo
    game2_button.grid(row=0, column=4, padx=10, pady=10)

create_menus()
create_game_icons()

root.mainloop()
