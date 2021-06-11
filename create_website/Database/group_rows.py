import sqlite3

def get_row():
    conn = sqlite3.connect("social.db")
    cur = conn.cursor()
    cur.execute("SELECT GROUP_CONCAT(name) FROM contacts GROUP by id;")
    conn.commit()
    conn.close()

print(get_row())