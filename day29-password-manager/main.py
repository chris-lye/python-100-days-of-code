from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)


    char_list= [random.choice(letters) for i in range(0,nr_letters)]
    symb_list= [random.choice(symbols) for i in range(0,nr_symbols)]
    numb_list= [random.choice(numbers) for i in range(0,nr_numbers)]
    password_list = char_list + symb_list + numb_list

    random.shuffle(password_list)
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
        "email":email,
        "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please make sure all fields are filled.")
    else:
        try:
        # is_ok = messagebox.askokcancel(title=website, message=f"Details: \nEmail: {email} \nPassword:{password} \nPress ok to save.")
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH   ------------------------------- #
def search():
    website = website_entry.get()
    try:    
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        messagebox.showinfo("Error", "data.json not found.")
    else:
        if website in data:
            info = data[website]
            email = info["email"]
            password = info["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}\n")
        else:
            messagebox.showinfo("Error", "Website not found in data.json")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

#buttons
generate_password_button = Button(text='Generate Password',command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()