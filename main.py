from tkinter import *
from tkinter import messagebox
from password_generator import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    save_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the details entered: \nEmail:{email_data} "
                                               f"\nPassword:{password_data} "
                                               f"\nIs it ok to save")
        if is_ok:
            with open("Login Credentials.json", "w") as data:
                json.dump(save_data,data)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)
email_entry = Entry(width=35)
email_entry.insert(0, "abc@email.com")
email_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)
password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=3, row=4)
add_button = Button(text="Add", width=36, command=add_button)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
