import sqlite3

def admin_db():
    con = sqlite3.connect(database="GRP6PRJ.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS admin_users (ID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL, Email TEXT NOT NULL, ContactNo INTEGER NOT NULL)")
    con.commit()
    con.close()

def check_credentials(username, password):
    con = sqlite3.connect(database="GRP6PRJ.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM admin_users WHERE Username = ? AND Password = ?", (username, password))
    user = cur.fetchone()
    con.close()
    return user is not None

admin_db()
