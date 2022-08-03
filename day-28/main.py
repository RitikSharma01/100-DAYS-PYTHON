from cgitb import text
from textwrap import fill
from tkinter import *

from pyparsing import col
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodaro ')
# window.minsize(width=250, height=100)
window.config(background=YELLOW, padx=100, pady=50)


text_head = Label(text='Timer', font=(FONT_NAME, 40, 'bold'))
text_head.config(bg=YELLOW, fg=GREEN)
text_head.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(105, 130, text='00:00', font=(
    FONT_NAME, 33, 'bold'), fill='white')
canvas.grid(column=2, row=2)


start_btn = Button(text='Start', command=start_time)
start_btn.grid(column=1, row=3)

reset_btn = Button(text='Reset')
reset_btn.grid(column=3, row=3)

checkmark = Label(text='✔', fg=GREEN, bg=YELLOW)
checkmark.grid(column=2, row=3)
window.mainloop()
