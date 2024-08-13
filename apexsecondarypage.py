from tkinter import Tk, Label, Button, colorchooser

root = Tk()
root.title("Apex")
root.geometry("600x200")

email_label = Label(root, text="This is the APEX wiki test page.", font=("Arial", 12))
email_label.pack(pady=20)

root.mainloop()