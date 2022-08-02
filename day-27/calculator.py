from tkinter import *


window = Tk()

# window.minsize(height=200, width=400)
window.config(padx=20, pady=20)
window.title("Miles to KiloMeter")


#  Calculate Function
def calculate():
    x = float(my_input.get())

    answer.config(text=round(x*1.6))


# label
my_label = Label(text='is equal to', font=('Arabic', 20))
my_label.grid(column=1, row=2)


# input
my_input = Entry(width=15)
my_input.grid(column=2, row=1)
my_input.config(border=None)

# Miles label
my_miles = Label(text='miles', font=('Arabic', 20))
my_miles.grid(column=3, row=1)


# KM label
my_km = Label(text='km', font=('Arabic', 20))
my_km.grid(column=3, row=2)

# answer
answer = Label(text=0, font=('Arabic', 20))
answer.grid(column=2, row=2)

# button
my_button = Button(text='Calculate', font=('Arabic', 10), command=calculate)
my_button.grid(column=2, row=3)
my_button.config(width=15, padx=4, pady=4)


window.mainloop()
