from ntpath import join
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    pass_input.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    pass_word_list = []
    # for i in range(0, nr_letters):
    #     pass_word_list.append(random.choice(letters))
    # for i in range(0, nr_symbols):
    #     pass_word_list.append(random.choice(symbols))
    # for i in range(0, nr_numbers):
    #     pass_word_list.append(random.choice(numbers))

    pass_word_letter = [choice(letters) for i in range(nr_letters)]
    pass_word_number = [choice(numbers) for i in range(nr_numbers)]
    pass_word_symbol = [choice(symbols) for i in range(nr_symbols)]

    pass_word_list = pass_word_letter + pass_word_number + pass_word_symbol
    shuffle(pass_word_list)
    password = ''.join(pass_word_list)
    # for i in pass_word_list:
    #     password += i
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_name = web_input.get()
    email_name = email_input.get()
    password = pass_input.get()
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(
            title='opps', message="Please don't leave any fields empty")
    else:
        is_it_ok = messagebox.askokcancel(
            title=website_name, message=f"These are the details entered: \nEmail: {email_name}"f"\nPassword: {password} \nIs it ok to save?")
        if is_it_ok:
            with open('password_saver.txt', 'a') as file:
                file.write(f"{website_name } | { email_name} | { password}\n")
                web_input.delete(0, 'end')
                pass_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=200)
# tomato_image = PhotoImage(file='tomato.png')
# canvas.create_image(100, 100, password_image)
# canvas.grid(column=2, row=2)
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file='passward.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# row2

web_lebal = Label(text="website: ")
web_lebal.grid(column=0, row=1)


web_input = Entry(width=45)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
# row3
email_lebal = Label(text="Email/Username: ")
email_lebal.grid(column=0, row=2)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "sharmaritik896@gmail.com")

# row4
pass_lebal = Label(text="Password: ")
pass_lebal.grid(column=0, row=3)


pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

generate_btn = Button(text='Generate Password', command=password_generator)
generate_btn.grid(column=2, row=3)
# generate_btn.config(highlightthickness=None, borderwidth=None  )
# row5

add_input = Button(text='Add', width=36, command=save_password)
add_input.grid(column=1, row=4, columnspan=2)

window.mainloop()
