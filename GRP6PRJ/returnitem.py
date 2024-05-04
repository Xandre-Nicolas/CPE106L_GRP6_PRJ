import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class ReturnItemClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Lost Item Tracker")
        self.root.geometry("1000x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title=Label(self.root, text="Return Item to Owner", font=("goudy old style", 20, "bold"), bg="#C40C0C", fg="white").place(x=10, y=15, width=1000, height=30) 
        
        # Variables
        self.var_ReceiverName=StringVar()
        self.var_TypeofItem=StringVar()
        self.var_BrandofItem=StringVar()
        self.var_ColorofItem=StringVar()
        self.var_ModelofItem=StringVar()
        self.var_MaterialofItem=StringVar()
        self.var_OtherDescription=StringVar()
        self.var_LastSeen=StringVar()
        self.var_DateLost=StringVar()

        # Widgets
        lbl_ReceiverName=Label(self.root,text="Receiver:", font=("gouldy old style", 15), bg="white").place(x=10, y=60)
        lbl_TypeofItem=Label(self.root,text="Type of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=100)
        lbl_BrandofItem=Label(self.root,text="Brand of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=140)
        lbl_ColorofItem=Label(self.root,text="Color of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=180)
        lbl_ModelofItem=Label(self.root,text="Model of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=220)
        lbl_MaterialofItem=Label(self.root,text="Material of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=260)
        lbl_OtherDescription=Label(self.root,text="Other Description:", font=("gouldy old style", 15), bg="white").place(x=10, y=300)
        lbl_LastSeen=Label(self.root,text="Place Last Seen:", font=("gouldy old style", 15), bg="white").place(x=10, y=340)
        lbl_DateLost=Label(self.root,text="Date Lost:", font=("gouldy old style", 15), bg="white").place(x=10, y=380)

        # Entry Fields
        self.txt_ReceiverName=Entry(self.root, textvariable=self.var_ReceiverName, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_ReceiverName.place(x=175, y=65, width=200)

        self.txt_TypeofItem=Entry(self.root, textvariable=self.var_TypeofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_TypeofItem.place(x=175, y=105, width=200)

        self.txt_BrandofItem=Entry(self.root, textvariable=self.var_BrandofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_BrandofItem.place(x=175, y=145, width=200)

        self.txt_ColorofItem=Entry(self.root, textvariable=self.var_ColorofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_ColorofItem.place(x=175, y=185, width=200)

        self.txt_ModelofItem=Entry(self.root, textvariable=self.var_ModelofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_ModelofItem.place(x=175, y=225, width=200)
        
        self.txt_MaterialofItem=Entry(self.root, textvariable=self.var_MaterialofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_MaterialofItem.place(x=175, y=265, width=200)

        self.txt_OtherDescription=Entry(self.root, textvariable=self.var_OtherDescription, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_OtherDescription.place(x=175, y=305, width=200)

        self.txt_LastSeen=Entry(self.root, textvariable=self.var_LastSeen, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_LastSeen.place(x=175, y=345, width=200)

        self.txt_DateLost=Entry(self.root, textvariable=self.var_DateLost, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_DateLost.place(x=175, y=385, width=200)

        # Buttons
        self.btn_returnitem=Button(self.root, text="Return Item", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.returnitem)
        self.btn_returnitem.place(x=10, y=430, width=100, height=40)

        # Search Panel
        self.var_search=StringVar()
        lbl_seach_TypeofItem=Label(self.root,text="Search Item:", font=("gouldy old style", 15), bg="white").place(x=550, y=60)
        txt_search_TypeofItem=Entry(self.root, textvariable=self.var_search, font=("gouldy old style", 12), bg="#FDFFC2").place(x=675, y=65, width=200)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.search).place(x=890, y=60, width=90, height=30)

        # Content
        self.C_Frame=Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=550, y=100, width=430, height=320)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.ItemTable=ttk.Treeview(self.C_Frame, columns=("ItemNo","Type", "Brand", "Color", "Model", "Material", "OtherDescription", "LastSeen", "DateLost" ),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ItemTable.xview)
        scrolly.config(command=self.ItemTable.yview)
        self.ItemTable.heading("ItemNo", text="Item No:")
        self.ItemTable.heading("Type", text="Type:")
        self.ItemTable.heading("Brand", text="Brand:")
        self.ItemTable.heading("Color", text="Color:")
        self.ItemTable.heading("Model", text="Model:")
        self.ItemTable.heading("Material", text="Material:")
        self.ItemTable.heading("OtherDescription", text="Other Description:")
        self.ItemTable.heading("LastSeen", text="Last Seen:")
        self.ItemTable.heading("DateLost", text="Date Lost:")
        self.ItemTable["show"]='headings'
        self.ItemTable.column("ItemNo",width=55)
        self.ItemTable.column("Type",width=70)
        self.ItemTable.column("Brand",width=70)
        self.ItemTable.column("Color",width=80)
        self.ItemTable.column("Model",width=100)
        self.ItemTable.column("Material",width=130)
        self.ItemTable.column("OtherDescription",width=130)
        self.ItemTable.column("LastSeen",width=110)
        self.ItemTable.column("DateLost",width=70)
        self.ItemTable.pack(fill=BOTH, expand=1)
        self.ItemTable.bind("<ButtonRelease-1>", lambda event: self.get_data())
        self.show()

    def get_data(self):
        self.txt_TypeofItem.config(state='readonly')
        r=self.ItemTable.focus()
        content=self.ItemTable.item(r)
        row=content["values"]
        self.var_TypeofItem.set(row[1])
        self.var_BrandofItem.set(row[2])
        self.var_ColorofItem.set(row[3])
        self.var_ModelofItem.set(row[4])
        self.var_MaterialofItem.set(row[5])
        self.var_OtherDescription.set(row[6])
        self.var_LastSeen.set(row[7])
        self.var_DateLost.set(row[8])

    def returnitem(self):
        # Check if a specific item is selected in the table
        if not self.ItemTable.focus():
            self.show_message("Error", "Select the item to Return.")
            return

        # Fetch details of the selected item
        r = self.ItemTable.focus()
        content = self.ItemTable.item(r)
        row = content["values"]

        # Insert returned item data into return_items table
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            # Insert into return_items table
            cur.execute("INSERT INTO return_items (Receiver, Type, Brand, Color, Model, Material, OtherDescription, LastSeen, DateLost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (self.var_ReceiverName.get(), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            con.commit()

            # Delete the returned item from the lost_items table using a combination of attributes
            cur.execute("DELETE FROM lost_items WHERE Type=? AND Brand=? AND Color=? AND Model=? AND Material=? AND OtherDescription=? AND LastSeen=? AND DateLost=?",
                        (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            con.commit()

            self.show_message("Success", "Item Returned Successfully")
            # Refresh the display
            self.show()
        except Exception as ex:
            self.show_message("Error", f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()

    def show_message(self, title, message):
        popup = Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x100")

        # Calculate the position to center the popup
        window_width = popup.winfo_reqwidth()
        window_height = popup.winfo_reqheight()
        position_right = int(popup.winfo_screenwidth()/2 - window_width/2)
        position_down = int(popup.winfo_screenheight()/2 - window_height/2)

        popup.geometry("+{}+{}".format(position_right, position_down))
        popup.resizable(False, False)

        label = Label(popup, text=message, font=("Helvetica", 12), pady=10)
        label.pack()
        ok_button = Button(popup, text="OK", command=popup.destroy)
        ok_button.pack()


    def insert_returned_item(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM lost_items WHERE Type=?", (self.var_TypeofItem.get(),))
            row = cur.fetchone()
            if row:
                receiver = self.var_ReceiverName.get()
                cur.execute("INSERT INTO return_items (Receiver, Type, Brand, Color, Model, Material, OtherDescription, LastSeen, DateLost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (receiver, *row[1:]))
                # Remove the returned item from lost_items table
                cur.execute("DELETE FROM lost_items WHERE Type=?", (self.var_TypeofItem.get(),))
                con.commit()
        except Exception as ex:
            self.show_message("Error",f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()

    def show(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM lost_items")
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert("", END, values=row)
        except Exception as ex:
            self.show_message("Error", f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()

    def search(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            search_text = self.var_search.get().lower()
            query = f"SELECT * FROM lost_items WHERE LOWER(Type) LIKE '%{search_text}%'"
            cur.execute(query)
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert("", END, values=row)
        except Exception as ex:
            self.show_message("Error", f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()
        
        self.var_search.set("")


if __name__=="__main__":
    root=Tk()
    root.resizable(False, False)
    obj=ReturnItemClass(root)
    root.mainloop()
