from cProfile import label
from cgitb import text
from tkinter import *

from setuptools import Command

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_click():
    new_text = input.get()
    my_label.config(text=new_text)


my_label = Label(text="Learning Python")
# my_label.pack()
my_label.grid(column=0, row=0)


my_button = Button(text='Click Me', command=button_click)
# my_button.pack()
my_button.grid(column=1, row=1)


new_button = Button(text='Click ME 2', command=button_click)
new_button.grid(column=3, row=0)

input = Entry(width=10)
# my_label.config(text=input.get())
# input.pack()
input.grid(column=4, row=3)

window.mainloop()
