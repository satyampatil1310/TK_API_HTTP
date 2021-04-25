from tkinter import *
import pandas as pd
from tkinter import messagebox
import random
import json
from passwordgenerator import Password
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    password = ''

    alphabets = ['a', "A", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numericals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', "#", "$", "%", "&", "*", "(", ")", "_", "-"]

    length = random.randint(8, 13)
    count = 0
    while (1):
        x = random.randint(-1, 1)
        if x == -1:
            password = password + alphabets[random.randint(0, 26)]
            count += 1
        elif x == 0:
            password = password + symbols[random.randint(0, 10)]
            count += 1
        else:
            password = password + numericals[random.randint(0, 9)]
            count += 1
        if count == length:
            break
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    msg = messagebox.askokcancel(title="Warning", message="The information filled is correct?\nDo you want to save?")
    new_data = {website_entry.get():{
                            "email_username": email_username_entry.get(),
                            "password": password_entry.get()
                            }
                }
    with open('data.json', 'w') as file:
        json.dump(new_data, file, indent=4)
    website_entry.delete(0, 100)
    password_entry.delete(0, 100)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_file)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)


email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)


password = Label(text="Password:")
password.grid(row=3, column=0)


generate = Button(text="Generate Password", command=password_generator)
generate.grid(row=3, column=2)


website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2)
password_entry = Entry(width=35, show='*')
password_entry.grid(row=3, column=1)
email_username_entry = Entry(width=53)
email_username_entry.grid(row=2, column=1, columnspan=2)

add = Button(text="Add", width=35, command=add_data)
add.grid(row=4, column=1, columnspan=2)

website_entry.focus()
window.mainloop()
