# Importing  packages
import json
import os  # For writing directory
import secrets
import string
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import webbrowser


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
	pwsy_entry.delete(0, END)
	pwsy_entry.insert(0, password)
	pyperclip.copy(password)
	return password


# ---------------------------- SAVE PASSWORD ------------------------------- #


# Ensure directory called 'panty' is present , if not create
os.makedirs('panty', exist_ok=True)


def save():
	website = website_entry.get()
	email = email_entry.get()
	pwsy = pwsy_entry.get()
	current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# current_datetime_utc = datetime.now(timezone.utc)  # get current data and time UTCTZ
	new_data = {
		website: {
			"email": email,
			"pasy": pwsy,
			"date": current_datetime
		}

	}

	if len(website) == 0 or len(pwsy) == 0:
		messagebox.showinfo(title="😡FUKR", message="NoEmpty")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"""
			Details Entered:
			website: {website}
			Email:{email}
			Password: {pwsy}
			---
			Good ?
		""")

		# --- Validation
		if is_ok:
			fil_pa = 'panty/sniff.json'
			try:
				with open(fil_pa, "r") as data_file:
					data = json.load(data_file)
			except FileNotFoundError:
				with open(fil_pa, "w") as data_file:
					json.dump(new_data, data_file, indent=4)
			else:
				data.update(new_data)
				with open(fil_pa, "w") as data_file:
					json.dump(data, data_file, indent=4)
				print(data)
			finally:
				website_entry.delete(0, END)
				pwsy_entry.delete(0, END)
				window.quit()  # Stops the main event loop
				window.destroy()  # Destroys the main window

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_pass():
	pass

# ---------------------------- OpenWebsite ------------------------------- #


def open_website():
	TARGET_WEBSITE = "http://s2.clipff.com:8001/s11pornfd/videos/44000/44552/44552_720p.mp4"
	webbrowser.open(TARGET_WEBSITE)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Panty Manager')
window.configure(bg=MAINBG, padx=100, pady=100)

# --- Setup Canvas


canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="n.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1, pady=20)

# --- Labels ---

# Label Styles object
label_style = {
	'bg': MAINBG,
	'fg': TEXTFG,
	'font': ('Arial', 20)
}

haader_label = Label(text="App stores pwd in json\nfile and \nperform search", pady=30,font=('Courier', 20), bg="black", fg="red")
haader_label.grid(row=0, column=1)

website_label = Label(text="Website  ", **label_style)
website_label.grid(row=2, column=0)
email_label = Label(text="Email/Username  ", **label_style)
email_label.grid(row=3, column=0)
password_label = Label(text="Pwsy  ", **label_style)
password_label.grid(row=4, column=0)

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
website_entry.grid(row=2, column=1, pady=5, columnspan=2, ipady=10)
email_entry = Entry(**entry_style)
email_entry.grid(row=3, column=1, pady=5, columnspan=2, ipady=10)
email_entry.insert(0, 'booty@sniff.com')
pwsy_entry = Entry(**entry_style)
pwsy_entry.grid(row=4, column=1, ipady=10)
pwd = generate_password()
pwsy_entry.delete(0, END)
pwsy_entry.insert(0, pwd)

# --- Buttons ---
open_website_button = Button(text="SniffHer", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, command=open_website)
open_website_button.grid(row=1, column=2)
search_button = Button(text="Search", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, command=find_pass)
search_button.grid(row=2, column=3)
generate_password_button = Button(text="GENPWD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, command=generate_password)
generate_password_button.grid(row=4, column=3)
add_button = Button(text="ADD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, width=46, command=save)
add_button.grid(row=5, column=1, pady=20, columnspan=2)

# -- Window Setup ---
window.mainloop()
