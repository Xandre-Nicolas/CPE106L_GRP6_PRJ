
import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login form")
window.geometry('500x500')
window.configure(bg='#333333')

def login():
    username = "Group6"
    password = "lesgo"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')