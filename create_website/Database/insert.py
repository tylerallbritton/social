import sqlite3


def send_message(contact_from, contact_to, message):
    conn = sqlite3.connect("social.db")
    cur = conn.cursor()
    sql = f"INSERT INTO messages (received, via, message) VALUES ('{contact_to}','{contact_from}','{message}')"
    cur.execute(sql)
    conn.commit()
    conn.close()


def add_contact(id, name):
    conn = sqlite3.connect("social.db")
    cur = conn.cursor()
    sql = f"INSERT OR ignore INTO contacts (id, name) VALUES ('{id}','{name}')"
    cur.execute(sql)
    conn.commit()
    conn.close()


send_message("Chase", "Dad", "You are rad")
add_contact("Jen.k.allbritton", "Jen")
