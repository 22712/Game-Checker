from tkinter import *
from PIL import Image, ImageTk
import subprocess

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

root = Tk()
root.geometry("800x600")
root.title("Game Checker")

def create_menus():
    mainmenu = Menu(root)

    mainmenu.add_command(label="Return to Main", command=return_to_main)
    mainmenu.add_command(label="Return to Previous", command=return_to_previous)
    
    more_menu = Menu(mainmenu, tearoff=0)
    more_menu.add_command(label="Support", command=lambda: open_new_script("support.py"))
    more_menu.add_command(label="Contact", command=lambda: open_new_script("contact.py"))
    more_menu.add_command(label="QwQ", command=lambda: open_new_script("QwQ.py"))
    mainmenu.add_cascade(label="More", menu=more_menu)

    root.config(menu=mainmenu)

def create_game_icons():
    game_icons_frame = Frame(root)
    game_icons_frame.pack(expand=True, fill=BOTH)

    image_size = (100, 100)

    game1_image = Image.open("Image\mihuyou.png").resize(image_size)
    game1_photo = ImageTk.PhotoImage(game1_image)
    game1_button = Button(game_icons_frame, image=game1_photo, text="Game 1", compound=TOP, command=lambda: create_new_window("Game 1"))
    game1_button.image = game1_photo
    game1_button.grid(row=0, column=0, padx=10, pady=10)

    game2_image = Image.open("Image\TM.png").resize(image_size)
    game2_photo = ImageTk.PhotoImage(game2_image)
    game2_button = Button(game_icons_frame, image=game2_photo, text="Game 2", compound=TOP, command=lambda: create_new_window("Game 2"))
    game2_button.image = game2_photo
    game2_button.grid(row=0, column=1, padx=10, pady=10)

    game3_image = Image.open("Image\Mincecraft.png").resize(image_size)
    game3_photo = ImageTk.PhotoImage(game3_image)
    game3_button = Button(game_icons_frame, image=game3_photo, text="Game 3", compound=TOP, command=lambda: create_new_window("Game 3"))
    game3_button.image = game3_photo
    game3_button.grid(row=0, column=2, padx=10, pady=10)

create_menus()
create_game_icons()

root.mainloop()
