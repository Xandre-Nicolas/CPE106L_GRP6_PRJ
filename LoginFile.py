
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('500x500')
window.configure(bg='#787777')

def login():
    username = "Group6"
    password = "lesgo"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#787777', fg="#FF3399", font=("Arial Bold", 32))
username_label = tkinter.Label(
    frame, text="Username", bg='#787777', fg="#FFFFFF", font=("Arial Bold", 17))
username_entry = tkinter.Entry(frame, font=("Times New Roman", 17))
password_entry = tkinter.Entry(frame, show="*", font=("Times New Roman", 17))
password_label = tkinter.Label(
    frame, text="Password", bg='#787777', fg="#FFFFFF", font=("Arial Bold", 17))
login_button = tkinter.Button(
    frame, text="Login", bg="#b5001b", fg="#FFFFFF", font=("Arial Bold", 17), command=login)
 
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
 
frame.pack()
 
window.mainloop()
