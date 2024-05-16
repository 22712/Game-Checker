from tkinter import Tk, Label

root = Tk()
root.title("Contact page")
root.geometry("600x100")

email_label = Label(root, text="If you need to contact us, please contact us at: 22712@student.macleans.school.nz", font=("Arial", 12))
email_label.pack(pady=20)

root.mainloop()