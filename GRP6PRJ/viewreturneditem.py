import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class ViewReturnItemClass:
    
    def __init__(self, root):
        self.root = root
        self.root.title("View Returned Items")
        self.root.geometry("800x600")

        # Content
        C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        C_Frame.place(x=10, y=10, width=780, height=580)

        scrolly = Scrollbar(C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(C_Frame, orient=HORIZONTAL)
        ReturnedItemTable = ttk.Treeview(C_Frame, columns=("ID", "Receiver", "Type", "Brand", "Color", "Model", "Material", "OtherDescription"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=ReturnedItemTable.xview)
        scrolly.config(command=ReturnedItemTable.yview)
        ReturnedItemTable.heading("ID", text="ID")
        ReturnedItemTable.heading("Receiver", text="Receiver")
        ReturnedItemTable.heading("Type", text="Type")
        ReturnedItemTable.heading("Brand", text="Brand")
        ReturnedItemTable.heading("Color", text="Color")
        ReturnedItemTable.heading("Model", text="Model")
        ReturnedItemTable.heading("Material", text="Material")
        ReturnedItemTable.heading("OtherDescription", text="Other Description")
        ReturnedItemTable["show"] = 'headings'
        ReturnedItemTable.column("ID", width=30)
        ReturnedItemTable.column("Receiver", width=100)
        ReturnedItemTable.column("Type", width=70)
        ReturnedItemTable.column("Brand", width=70)
        ReturnedItemTable.column("Color", width=90)
        ReturnedItemTable.column("Model", width=150)
        ReturnedItemTable.column("Material", width=130)
        ReturnedItemTable.column("OtherDescription", width=130)
        ReturnedItemTable.pack(fill=BOTH, expand=1)

        # Fetch and display data from the database
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM return_items")
            rows = cur.fetchall()
            for row in rows:
                ReturnedItemTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()

    def view_returned_items(self):
        self.root.mainloop()

def delete_selected_row(self, event):
    # Get the selected item's ID
    selected_item = self.ReturnedItemTable.selection()[0]
    item_id = self.ReturnedItemTable.item(selected_item, "values")[0]

    # Confirm deletion with the user
    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this item?")

    if confirm:
        # Delete the item from the database
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM return_items WHERE ID=?", (item_id,))
            con.commit()
            # Remove the item from the Treeview
            self.ReturnedItemTable.delete(selected_item)
            messagebox.showinfo("Success", "Item deleted successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            cur.close()
            con.close()

def __init__(self, root):
    # Existing code...

    # Bind the delete function to the Treeview
    ReturnedItemTable.bind("<Delete>", self.delete_selected_row) # type: ignore
        

if __name__=="__main__":
    root = Tk()
    root.resizable(False, False)
    obj = ViewReturnItemClass(root)
    obj.view_returned_items()
