import tkinter as tk
from tkinter import font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("300x200")

# create empty frame
frame_login = tk.Frame(root)

# create empty frame (new window for components in roots)
frame_login.grid()

# widgets for frame_login
standard_font = tkFont.Font(family="Helvetica", size=13, weight="bold")
lbl_username = tk.Label(frame_login, text='Username:', font=standard_font)
lbl_username.pack()

# Textbox for usernames
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=50)

# Same as above 2 for password
lbl_password = tk.Label(frame_login, text='Password:', font=standard_font)
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(padx=50)

root.mainloop()