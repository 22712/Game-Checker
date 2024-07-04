from tkinter import Tk, Label, Button, colorchooser

def change_theme_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)
        email_label.configure(bg=color)

root = Tk()
root.title("Contact Page")
root.geometry("600x200")

email_label = Label(root, text="If you need to contact us, please contact us at: 22712@student.macleans.school.nz", font=("Arial", 12))
email_label.pack(pady=20)

change_theme_button = Button(root, text="Change Theme Color", command=change_theme_color)
change_theme_button.pack(pady=20)

root.mainloop()
