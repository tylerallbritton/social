import sqlite3


def list_messages(contact):
    """
    list a set of messages by contact or logged in user
    :param contact: string/name of user
    :return: list of messages
    """
    conn = sqlite3.connect("Database/social.db")
    cur = conn.cursor()
    cur.execute(f"SELECT via, received, message FROM messages WHERE received = '{contact}' or via = '{contact}'")
    rows = cur.fetchall()
    conn.close()
    # google search "python cursor fetch rows into list example"
    # string_list = []
    # for message in rows:
    #     string_list.append(f"{message[0]}: {message[2]}")
    return rows


def list_contacts():
    conn = sqlite3.connect("Database/social.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name as contact FROM contacts")
    rows = cur.fetchall()
    conn.close()
    return rows


def send_message(contact_from, contact_to, message):
    conn = sqlite3.connect("Database/social.db")
    cur = conn.cursor()
    sql = f"INSERT INTO messages (received, via, message) VALUES ('{contact_to}','{contact_from}','{message}')"
    cur.execute(sql)
    conn.commit()
    conn.close()
