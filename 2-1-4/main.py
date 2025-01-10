import tkinter as tk
from tkinter import font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("300x200")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

# create empty frame (new window for components in roots)
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")

# Defining font
standard_font = tkFont.Font(family="Helvetica", size=13, weight="bold")

# Defining functions
def login():
    frame_auth.tkraise()

# widgets for frame_login
# Username lbl
lbl_username = tk.Label(frame_login, text='Username:', font=standard_font)
lbl_username.pack()

# Textbox for usernames
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=50)

# Same as above 2 for password
lbl_password = tk.Label(frame_login, text='Password:', font=standard_font)
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(padx=50)

# Login button
button_login = tk.Button(frame_login, text='Login', command=login, font=standard_font)
button_login.pack(padx=50, pady=10)

# widgets for frame_auth
lbl_auth = tk.Label(frame_auth, text='Authorized', font=standard_font)
lbl_auth.pack()


frame_login.tkraise()
root.mainloop()