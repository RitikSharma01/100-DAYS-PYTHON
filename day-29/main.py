# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

from pyparsing import col

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# canvas = Canvas(width=200, height=200)
# tomato_image = PhotoImage(file='tomato.png')
# canvas.create_image(100, 100, password_image)
# canvas.grid(column=2, row=2)
canvas = Canvas(width=200, height=224)
password_image = PhotoImage(file='passward.png')
canvas.create_image(135, 112, image=password_image)
canvas.grid(column=2, row=2)


window.mainloop()
