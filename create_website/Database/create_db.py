import sqlite3


def create_messages_table():
    conn = sqlite3.connect("social.db")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS messages (received TEXT, via TEXT, message TEXT)")
    conn.commit()
    conn.close()


def create_contacts_table():
    conn = sqlite3.connect("social.db")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS contacts (id TEXT, name TEXT)")
    conn.commit()
    conn.close()


create_messages_table()
create_contacts_table()
