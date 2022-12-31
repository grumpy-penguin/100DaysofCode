import secrets
import string
import tkinter
from tkinter import messagebox

BACKGROUND_COLOUR = "white"
WEBSITE = tkinter.StringVar
USERNAME = tkinter.StringVar
PASSWORD = tkinter.StringVar

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    passwd = "".join(secrets.choice(alphabet) for _ in range(12))
    password_input.delete(0, tkinter.END)
    password_input.insert(0, passwd)
    window.clipboard_append(passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showerror("Error", "Do not leave any options empty")
    else:
        answer = messagebox.askokcancel(
            title=website,
            message=f"These are the details your entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?",
        )

        if answer:
            with open("day29/data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")

            password_input.delete(0, tkinter.END)
            website_input.delete(0, tkinter.END)
            website_input.focus()

            messagebox.showinfo("Information", "Password Added to Database")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=20, pady=20, bg=BACKGROUND_COLOUR)
window.title("Password Manager")
# Create a canvas to add the assets to
canvas = tkinter.Canvas(
    width=200, height=200, highlightthickness=0, bg=BACKGROUND_COLOUR
)

# Add a logo image to the canvas
logo = tkinter.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

# Add a website label to the window
website_label = tkinter.Label(text="Website: ", bg=BACKGROUND_COLOUR)
website_label.grid(column=0, row=2)

# A a website entry to the window
website_input = tkinter.Entry(width=38, textvariable=WEBSITE)
website_input.grid(column=1, row=2, columnspan=2)
website_input.focus()

# Add a Email/Username to the window
username_label = tkinter.Label(text="Email/Username: ", bg=BACKGROUND_COLOUR)
username_label.grid(column=0, row=3)

# Add a Email/Username entry to the Windows
username_input = tkinter.Entry(width=38, textvariable=USERNAME)
username_input.grid(column=1, row=3, columnspan=2)
username_input.insert(0, "grumpy-penguin@example.com")

# Add a Password Label
password_label = tkinter.Label(text="Password: ", bg=BACKGROUND_COLOUR)
password_label.grid(column=0, row=4)

# Add a Password Entry
password_input = tkinter.Entry(width=21, textvariable=PASSWORD)
password_input.grid(column=1, row=4)


# Add a Password Generate Button
password_generate = tkinter.Button(
    text="Generate Password", bg=BACKGROUND_COLOUR, command=generate_password
)
password_generate.grid(column=2, row=4)

# Add an Add button
add_button = tkinter.Button(
    text="Add", width=36, bg=BACKGROUND_COLOUR, command=save_password
)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
