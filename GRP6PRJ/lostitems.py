from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class LostItemClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Lost Item Tracker")
        self.root.geometry("1000x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title=Label(self.root, text="List of Lost Items", font=("goudy old style", 20, "bold"), bg="#C40C0C", fg="white").place(x=10, y=15, width=1000, height=30) 
        
        # Variables
        self.var_TypeofItem=StringVar()
        self.var_BrandofItem=StringVar()
        self.var_ColorofItem=StringVar()
        self.var_ModelofItem=StringVar()
        self.var_MaterialofItem=StringVar()
        self.var_OtherDescription=StringVar()
        self.var_LastSeen=StringVar()
        self.var_DateLost=StringVar()

        # Widgets
        lbl_TypeofItem=Label(self.root,text="Type of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=60)
        lbl_BrandofItem=Label(self.root,text="Brand of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=100)
        lbl_ColorofItem=Label(self.root,text="Color of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=140)
        lbl_ModelofItem=Label(self.root,text="Model of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=180)
        lbl_MaterialofItem=Label(self.root,text="Material of Item:", font=("gouldy old style", 15), bg="white").place(x=10, y=220)
        lbl_OtherDescription=Label(self.root,text="Other Description:", font=("gouldy old style", 15), bg="white").place(x=10, y=260)
        lbl_LastSeen=Label(self.root,text="Place Last Seen:", font=("gouldy old style", 15), bg="white").place(x=10, y=300)
        lbl_DateLost=Label(self.root,text="Date Lost:", font=("gouldy old style", 15), bg="white").place(x=10, y=340)

        # Entry Fields
        self.txt_TypeofItem=Entry(self.root, textvariable=self.var_TypeofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_TypeofItem.place(x=175, y=65, width=200)

        self.txt_BrandofItem=Entry(self.root, textvariable=self.var_BrandofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_BrandofItem.place(x=175, y=105, width=200)

        self.txt_ColorofItem=Entry(self.root, textvariable=self.var_ColorofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_ColorofItem.place(x=175, y=145, width=200)

        self.txt_ModelofItem=Entry(self.root, textvariable=self.var_ModelofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_ModelofItem.place(x=175, y=185, width=200)
        
        self.txt_MaterialofItem=Entry(self.root, textvariable=self.var_MaterialofItem, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_MaterialofItem.place(x=175, y=225, width=200)

        self.txt_OtherDescription=Entry(self.root, textvariable=self.var_OtherDescription, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_OtherDescription.place(x=175, y=265, width=200)

        self.txt_LastSeen=Entry(self.root, textvariable=self.var_LastSeen, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_LastSeen.place(x=175, y=305, width=200)

        self.txt_DateLost=Entry(self.root, textvariable=self.var_DateLost, font=("gouldy old style", 12), bg="#FDFFC2")
        self.txt_DateLost.place(x=175, y=345, width=200)

        # Buttons
        self.btn_add=Button(self.root, text="Add Item", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=40, y=400, width=100, height=40)
        self.btn_update=Button(self.root, text="Update Item", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=150, y=400, width=100, height=40)
        self.btn_delete=Button(self.root, text="Delete Item", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=260, y=400, width=100, height=40)
        self.btn_clear=Button(self.root, text="Clear", font=("goudy old style", 10, "bold"), bg="#322C2B", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=370, y=400, width=100, height=40)

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
        self.ItemTable.column("Color",width=90)
        self.ItemTable.column("Model",width=90)
        self.ItemTable.column("Material",width=130)
        self.ItemTable.column("OtherDescription",width=130)
        self.ItemTable.column("LastSeen",width=110)
        self.ItemTable.column("DateLost",width=70)
        self.ItemTable.pack(fill=BOTH, expand=1)
        self.ItemTable.bind("<ButtonRelease-1>", lambda event: self.get_data())
        self.show()

    def clear(self):
         self.show()
         self.var_TypeofItem.set("")
         self.var_BrandofItem.set("")
         self.var_ColorofItem.set("")
         self.var_ModelofItem.set("")
         self.var_MaterialofItem.set("")
         self.var_OtherDescription.set("")
         self.var_LastSeen.set("")
         self.var_DateLost.set("")
         self.var_search.set("")
         self.txt_TypeofItem.config(state=NORMAL)
    
    def delete(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            selected_item = self.ItemTable.focus()
            item_id = self.ItemTable.item(selected_item, "values")[0]
            cur.execute("DELETE FROM lost_items WHERE ItemNo=?", (item_id,))
            con.commit()
            self.show()
        except Exception as ex:
            cur.close()
            con.close()


    def get_data(self):
         self.txt_TypeofItem.config(state='readonly')
         r=self.ItemTable.focus()
         content=self.ItemTable.item(r)
         row=content["values"]
         # print(row)
         self.var_TypeofItem.set(row[1])
         self.var_BrandofItem.set(row[2])
         self.var_ColorofItem.set(row[3])
         self.var_ModelofItem.set(row[4])
         self.var_MaterialofItem.set(row[5])
         self.var_OtherDescription.set(row[6])
         self.var_LastSeen.set(row[7])
         self.var_DateLost.set(row[8])

    def add(self):
        if (
            not self.var_TypeofItem.get()
            or not self.var_BrandofItem.get()
            or not self.var_ColorofItem.get()
            or not self.var_ModelofItem.get()
            or not self.var_MaterialofItem.get()
            or not self.var_OtherDescription.get()
            or not self.var_LastSeen.get()
            or not self.var_DateLost.get()
        ):
             self.show_message("Please Fill in All Fields", "error")
             return

        con=sqlite3.connect(database="GRP6PRJ.db")
        cur=con.cursor()
        try:
                cur.execute("insert into lost_items (Type, Brand, Color, Model, Material, OtherDescription, LastSeen, DateLost) values(?,?,?,?,?,?,?,?)",
                (
                    self.var_TypeofItem.get(),
                    self.var_BrandofItem.get(),
                    self.var_ColorofItem.get(),
                    self.var_ModelofItem.get(),
                    self.var_MaterialofItem.get(),
                    self.var_OtherDescription.get(),
                    self.var_LastSeen.get(),
                    self.var_DateLost.get(),
                ),
            )
                con.commit()
                self.show_message("Item Added Successfully", "info")
                self.show()
        except Exception as ex:
                self.show_message(f"Error due to {str(ex)}", "error")
        finally:
            cur.close()
            con.close()

    def update(self):
        if (
            not self.var_BrandofItem.get()
            or not self.var_ColorofItem.get()
            or not self.var_ModelofItem.get()
            or not self.var_MaterialofItem.get()
            or not self.var_OtherDescription.get()
            or not self.var_LastSeen.get()
            or not self.var_DateLost.get()
        ):
            self.show_message("Select Item to Update", "error")
            return

        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            selected_item = self.ItemTable.focus()
            if not selected_item:
                self.show_message("Please select an item to update.", "error")
                return
            item_id = self.ItemTable.item(selected_item, "values")[0]
            cur.execute(
                "UPDATE lost_items SET Brand=?, Color=?, Model=?, Material=?, OtherDescription=?, LastSeen=?, DateLost=? WHERE ItemNo=?",
                (
                    self.var_BrandofItem.get(),
                    self.var_ColorofItem.get(),
                    self.var_ModelofItem.get(),
                    self.var_MaterialofItem.get(),
                    self.var_OtherDescription.get(),
                    self.var_LastSeen.get(),
                    self.var_DateLost.get(),
                    item_id,
                ),
            )
            con.commit()
            self.show_message("Item Updated Successfully", "info")
            self.show()
        except Exception as ex:
            self.show_message(f"Error due to {str(ex)}", "error")
        finally:
            cur.close()
            con.close()


    def show(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            cur.execute("select * from lost_items")
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert("", END, values=row)
        except Exception as ex:
            self.show_message(f"Error due to {str(ex)}", "error")
        finally:
            cur.close()
            con.close()

    def search(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            search_text = self.var_search.get().lower()
            query = f"SELECT * FROM lost_items WHERE LOWER(Type) LIKE '%{search_text}%'"
            print("Search query:", query)  # Print the search query for debugging
            cur.execute(query)
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert("", END, values=row)
        except Exception as ex:
            self.show_message(f"Error due to {str(ex)}", "error")
        finally:
            cur.close()
            con.close()
        
        self.var_search.set("")

    def show_message(self, message, message_type):
        top = Toplevel(self.root)
        top.title(message_type.capitalize())
        top.geometry("300x150")
        top.focus_force()

        label = Label(top, text=message, font=("Arial", 12), wraplength=280, justify="center")
        label.pack(pady=20)

        ok_btn = Button(top, text="OK", command=top.destroy)
        ok_btn.pack(pady=10)

        # Center the window
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry(f"+{x}+{y}")


if __name__=="__main__":
    root=Tk()
    root.resizable(False, False)
    obj=LostItemClass(root)
    root.mainloop()
