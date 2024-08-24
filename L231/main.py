# Importing  packages
import os  # For writing directory
import secrets
import string
from datetime import datetime, timezone  # for getting current date and time
from tkinter import *
from tkinter import messagebox
import pyperclip

# -- Color Constants
MAINBG = "#020617"
TEXTFG = "#EEE4B1"
ENTRYBG = "black"
ENTRYFG = "#F97300"
BUTTONBG = "#180161"
INSERT_BACKGROUND = 'hotpink'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length=22):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(secrets.choice(characters) for _ in range(length))
	password_entry.delete(0, END)
	password_entry.insert(0, password)
	pyperclip.copy(password)
	return password


# ---------------------------- SAVE PASSWORD ------------------------------- #


# Ensure directory called 'panty' is present , if not create
os.makedirs('panty', exist_ok=True)


def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	current_datetime_utc = datetime.now(timezone.utc)  # get current data and time UTCTZ

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="😡FUKR", message="NoEmpty")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"""
		Details Entered:
		website: {website}
		Email:{email}
		Password: {password}
		---
		Good ? 	
	""")

	# --- Validation
	if is_ok:
		with open('panty/sniff.txt', "a") as data_file:
			data_file.write(f"""
	***************************
	UTC - {current_datetime_utc}
	---
	* Website  = {website}   
	* Email    = {email} 
	* Password = {password} 
	**************************
	""")
			website_entry.delete(0, END)
			password_entry.delete(0, END)
			window.quit()  # Stops the main event loop
			window.destroy()  # Destroys the main window


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Panty Manager')
window.configure(bg=MAINBG, padx=100, pady=100)

# --- Setup Canvas

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="n.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

# --- Labels ---

# Label Styles object
label_style = {
	'bg': MAINBG,
	'fg': TEXTFG,
	'font': ('Arial', 20)
}

website_label = Label(text="Website  ", **label_style)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username  ", **label_style)
email_label.grid(row=2, column=0)
password_label = Label(text="Password  ", **label_style)
password_label.grid(row=3, column=0)

# Entry styles made into an object that is then being called inside Entry
entry_style = {
	'width': 35,
	'bg': ENTRYBG,
	'fg': ENTRYFG,
	'font': ('Courier', 20),
	'insertbackground': INSERT_BACKGROUND,
	'justify': 'center',
	'highlightcolor': INSERT_BACKGROUND,
	'highlightthickness': 1
}

# --- Entry Boxes --
website_entry = Entry(**entry_style)
website_entry.focus()
website_entry.grid(row=1, column=1, pady=5, columnspan=2, ipady=10)
email_entry = Entry(**entry_style)
email_entry.grid(row=2, column=1, pady=5, columnspan=2, ipady=10)
email_entry.insert(0, 'booty@sniff.com')
password_entry = Entry(**entry_style)
password_entry.grid(row=3, column=1, pady=5, ipady=10)
pwd = generate_password()
password_entry.delete(0, END)
password_entry.insert(0, pwd)

# --- Buttons ---
generate_password_button = Button(text="GENPWD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="ADD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, width=46, command=save)
add_button.grid(row=4, column=1, pady=20, columnspan=2)

# -- Window Setup ---
window.mainloop()
