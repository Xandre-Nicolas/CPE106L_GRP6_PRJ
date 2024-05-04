import sqlite3
def itemlist_db():
    con=sqlite3.connect(database="GRP6PRJ.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS lost_items(ItemNo INTEGER PRIMARY KEY AUTOINCREMENT, Reciever text, Type text, Brand text, Color text, Model text, Material text, OtherDescription text, LastSeen text, DateLost text)")
    con.commit()

itemlist_db()


