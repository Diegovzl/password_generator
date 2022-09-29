from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    #Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range (randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint (2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    #insert generated password into entry password.
    password_entry.delete( first=0,last='end')
    password_entry.insert(0, password) 
    #copy password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(email)== 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please complete all the info.")
    else:
        #Dialog box that ask if the info is correct.
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                                f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            user = f"{website} | {email} | {password}\n"
            with open('Your path/users.txt', 'a') as f:
                f.write(user)

            #Clear fields
            website_entry.delete( first=0,last='end')
            email_entry.delete( first=0,last='end')
            password_entry.delete( first=0,last='end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

#Lock image
canvas = Canvas (width=200, height=200)
logo_img = PhotoImage(file="Your path/logo.png")
canvas.create_image (100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
#Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)

#User label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=E)

#Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)

#Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan= 2, sticky=W)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan= 2, sticky=W)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3, sticky=W)

#Buttons

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=49, command=save)
add_button.grid(column=1, row=4, columnspan= 2, sticky=W)

window.mainloop()