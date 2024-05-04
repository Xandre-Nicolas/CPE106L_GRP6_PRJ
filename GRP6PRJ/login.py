from tkinter import *
from tkinter import messagebox
import admin_db
import signup
from dashboard import GRP6PRJ  # Importing the GRP6PRJ class from dashboard.py

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Lost Item Tracker")

        window_width = 400
        window_height = 200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="LOGIN FORM", font=("goudy old style", 15, "bold"), bg="#C40C0C", fg="white")
        title.place(relx=0.5, y=15, width=400, anchor="center")

        self.lbl_username = Label(self.root, text="Username:", font=("goudy old style", 15, "bold"), bg="white")
        self.lbl_username.place(x=50, y=55)
        self.entry_username = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2")
        self.entry_username.place(x=160, y=60)

        self.lbl_password = Label(self.root, text="Password:", font=("goudy old style", 15, "bold"), bg="white")
        self.lbl_password.place(x=50, y=95)
        self.entry_password = Entry(self.root, font=("Times new Roman", 12), bg="#FDFFC2", show="*")
        self.entry_password.place(x=160, y=100)

        btn_login = Button(self.root, text="LOGIN", font=("goudy old style", 10, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.login)
        btn_login.place(x=130, y=145, width=75)

        btn_signup = Button(self.root, text="SIGN UP", font=("goudy old style", 10, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.open_signup_window)
        btn_signup.place(x=220, y=145, width=75)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username.strip() == "" or password.strip() == "":
            messagebox.showinfo("Error", "Please enter both username and password")
            return
        
        if admin_db.check_credentials(username, password):
            self.open_dashboard_window()
        else:
            messagebox.showinfo("Error", "Invalid username or password")

    def open_dashboard_window(self):
        self.root.withdraw()  
        dashboard_window = Toplevel(self.root)
        dashboard_app = GRP6PRJ(dashboard_window)  

    def open_signup_window(self):
        self.root.withdraw()
        signup_window = Toplevel(self.root)
        signup_app = signup.SignupClass(signup_window)

    
if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    obj = LoginClass(root)
    root.mainloop()
