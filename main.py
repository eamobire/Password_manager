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
    website_data = website_entry.get().lower()
    email_data = email_entry.get().lower()
    password_data = password_entry.get()

    saved_data = {
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
            try:
                with open("Login Credentials.json", "r") as data:
                    loaded_data = json.load(data)
                    loaded_data.update(saved_data)
            except FileNotFoundError:
                with open("Login Credentials.json", "w") as data:
                    json.dump(saved_data, data, indent=4)

            else:
                with open("Login Credentials.json", "w") as data:
                    json.dump(loaded_data, data, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get().lower()
    try:
        with open("Login Credentials.json", "r") as data:
            entries = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in entries:
            email = entries[website]["email"]
            password = entries[website]["password"]
            messagebox.showinfo(website.title(), f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website.title()} exists.")



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
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=2, row=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=3, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)
email_entry = Entry(width=35)
email_entry.insert(0, "abc@mail.com")
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
