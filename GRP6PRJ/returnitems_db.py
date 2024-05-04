import sqlite3

def returnitemlist_db():
    con = sqlite3.connect(database="GRP6PRJ.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE return_items (ID INTEGER PRIMARY KEY AUTOINCREMENT,Receiver TEXT NOT NULL, Type TEXT NOT NULL, Brand TEXT NOT NULL, Color TEXT NOT NULL, Model TEXT NOT NULL, Material TEXT NOT NULL,OtherDescription TEXT NOT NULL);")
    con.commit()

returnitemlist_db()
    