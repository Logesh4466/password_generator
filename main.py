from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
FONT = "Arial", 10, "normal"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list,)

    password = "". join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get()
    mail = email_entry.get()
    pas = password_entry.get()
    if web == "" or pas == "":
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered: \n Email: {mail}\n Password: {pas}\n is it ok save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {mail} | {pas}\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website:", font=(FONT))
website.grid(row=1,column=0)
email = Label(text="Email/Username:", font=(FONT))
email.grid(row=2, column=0)
password = Label(text="Password:", font=(FONT))
password.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "logesh4466@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1,columnspan=2)

# Buttons
generate_password = Button(text="Generate Password", command=password_generate)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()