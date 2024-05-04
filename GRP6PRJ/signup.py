from tkinter import *
from tkinter import messagebox
import sqlite3
import login

class SignupClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Lost Item Tracker")

        # Calculate the position to center the window on the screen
        window_width = 400
        window_height = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="SIGNUP FORM", font=("goudy old style", 15, "bold"), bg="#C40C0C", fg="white")
        title.place(x=5, y=10, width=400, height=30)

        # Name label and entry
        self.lbl_nameID = Label(self.root, text="Name:", font=("goudy old style", 15, "bold"), bg="white")
        self.lbl_nameID.place(x=50, y=70)
        self.entry_nameID = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2")
        self.entry_nameID.place(x=160, y=75)

        # Username label and entry
        self.lbl_username = Label(self.root, text="Username:", font=("goudy old style", 15), bg="white")
        self.lbl_username.place(x=50, y=110)
        self.entry_username = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2")
        self.entry_username.place(x=160, y=115)

        # Password label and entry
        self.lbl_password = Label(self.root, text="Password:", font=("goudy old style", 15), bg="white")
        self.lbl_password.place(x=50, y=150)
        self.entry_password = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2", show="*")
        self.entry_password.place(x=160, y=155)

        # Email label and entry
        self.lbl_email = Label(self.root, text="Email:", font=("goudy old style", 15), bg="white")
        self.lbl_email.place(x=50, y=190)
        self.entry_email = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2")
        self.entry_email.place(x=160, y=195)

        # Contact label and entry
        self.lbl_contact = Label(self.root, text="Contact No:", font=("goudy old style", 15), bg="white")
        self.lbl_contact.place(x=50, y=230)
        self.entry_contact = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2")
        self.entry_contact.place(x=160, y=235)
        self.entry_contact.config(validate="key", validatecommand=(self.root.register(self.validate_contact), "%P"))

        # Sign up button
        btn_signup = Button(self.root, text="SIGN UP", font=("goudy old style", 10, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.signup)
        btn_signup.place(x=125, y=280, width=75)

        # Clear button
        btn_clear = Button(self.root, text="CLEAR", font=("goudy old style", 10, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.clear_fields)
        btn_clear.place(x=215, y=280, width=75)

        # Call admin_db function to create table
        self.admin_db()

    def signup(self):
        nameID = self.entry_nameID.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()
        contact = self.entry_contact.get()

        if not (username and password and email and contact):
            messagebox.showerror("Error", "All fields are required!")
            return

        if len(username) < 8 or len(password) < 8:
            messagebox.showerror("Error", "Username and password must be at least 8 characters long!")
            return
        
        if len(contact) != 11:
            messagebox.showerror("Error", "Contact Must Contain 11 Digits" )
            return

        con = None  # Initialize the connection variable

        try:
            # Connect to the database
            con = sqlite3.connect("GRP6PRJ.db")
            cur = con.cursor()
            
            # Execute the SQL query to insert user information
            cur.execute("INSERT INTO admin_users (Name, Username, Password, Email, ContactNo) VALUES (?, ?, ?, ?, ?)", (nameID, username, password, email, contact))
            
            # Commit the changes
            con.commit()

            messagebox.showinfo("Success", "User registered successfully!")
            self.clear_fields()

            # Open the login window
            self.open_login_window()
            
            # Close the signup window
            self.root.destroy()
        
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

        finally:
            if con:
                con.close()  # Close the database connection

    def clear_fields(self):
        self.entry_nameID.delete(0, END)
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_contact.delete(0, END)

    def validate_contact(self, value):
        if value.isdigit() or value == "":
            return True
        return False

    def admin_db(self):
        try:
            with sqlite3.connect("GRP6PRJ.db") as con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS admin_users (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL, Email TEXT NOT NULL, ContactNo INTEGER NOT NULL)")
        except sqlite3.Error as e:
            print("Database error:", e)

    def open_login_window(self):
        login_window = Tk()
        login_app = login.LoginClass(login_window)

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    obj = SignupClass(root)
    root.mainloop()
