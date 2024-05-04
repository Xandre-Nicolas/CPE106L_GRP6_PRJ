from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from lostitems import LostItemClass
from returnitem import ReturnItemClass
from viewreturneditem import ViewReturnItemClass


class GRP6PRJ: 
    def __init__(self, root):
        self.root = root
        self.root.title("Lost Item Tracker")
        self.root.geometry("850x700+0+0")
        self.root.config(bg="white")

        window_width = 850
        window_height = 800
        position_right = int(self.root.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.root.winfo_screenheight()/2 - window_height/2)

        self.root.geometry("+{}+{}".format(position_right, position_down))
        # Title
        title = Label(self.root, text="LOST ITEM TRACKER", font=("Times new Roman", 25, "bold"), bg="#C40C0C", fg="white").place(x=0, y=0, relwidth=1, height=50)
        
        # Menu
        M_Frame = LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=830, height=80)

        btn_LostItems = Button(M_Frame, text="LOST ITEMS", font=("goudy old style", 9, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.add_lostitems).place(x=20, y=5, width=155, height=40)
        btn_ReturnItems = Button(M_Frame, text="RETURN ITEMS", font=("goudy old style", 9, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.add_returnitem).place(x=180, y=5, width=155, height=40)
        btn_VreturnedItems = Button(M_Frame, text="VIEW RETURNED ITEMS", font=("goudy old style", 9, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.add_viewreturnitem).place(x=340, y=5, width=155, height=40)
        btn_Logout = Button(M_Frame, text="LOGOUT", font=("goudy old style", 9, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.logout).place(x=500, y=5, width=155, height=40)
        btn_Exit = Button(M_Frame, text="EXIT", font=("goudy old style", 9, "bold"), bg="#EEE4B1", fg="black", cursor="hand2", command=self.exitprogram).place(x=660, y=5, width=155, height=40)
       
        # Content window
        self.bg_img = Image.open("Images/bg.jpg")
        self.bg_img = self.bg_img.resize((920,340))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=55, y=180, width=740, height=340)    

        # Update label for lost items count
        self.lbl_lostItems = Label(self.root, text="Total Lost Item\n [ 0 ]", font=("goudy old style", 15), bd=10, relief=RIDGE, bg="#EEE4B1")
        self.lbl_lostItems.place(x=55, y=530, width=365, height=100)
        self.update_lost_items_count() 

        # Label for returned items count
        self.lbl_returnedItems = Label(self.root, text="Total Returned/Claimed Items\n [ 0 ]", font=("goudy old style", 15), bd=10, relief=RIDGE, bg="#EEE4B1")
        self.lbl_returnedItems.place(x=430, y=530, width=365, height=100)
        self.update_return_items_count()

        # Footer
        footer = Label(self.root, text="Developed By Group 6\nContact Us for your Lost Items: 8157-2313", font=("goudy old style", 12), bg="#C40C0C", fg="white").pack(side=BOTTOM, fill="x")

        # Schedule automatic updates every 5 seconds
        self.root.after(5000, self.update_counts_periodically)
        
    def add_lostitems(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = LostItemClass(self.new_win)

    def add_returnitem(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReturnItemClass(self.new_win)

    def add_viewreturnitem(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ViewReturnItemClass(self.new_win)

    def exitprogram(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def update_lost_items_count(self):
        conn = sqlite3.connect('GRP6PRJ.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM lost_items")
        lost_items_count = cursor.fetchone()[0]
        self.lbl_lostItems.config(text=f"TOTAL LOST ITEMS\n [ {lost_items_count} ]")
        conn.close()

    def update_return_items_count(self):
        conn = sqlite3.connect('GRP6PRJ.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM return_items")
        return_items_count = cursor.fetchone()[0]
        self.lbl_returnedItems.config(text=f"TOTAL RETURNED ITEMS\n [ {return_items_count} ]")
        conn.close()

    def update_counts_periodically(self):
        self.update_lost_items_count()
        self.update_return_items_count()
        # Schedule the next update
        self.root.after(5000, self.update_counts_periodically)

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.root.destroy()  
            import os
            os.system('python login.py')



if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    obj = GRP6PRJ(root)
    root.mainloop()
