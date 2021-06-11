import sqlite3


def list_messages(contact):
    """
    list a set of messages by contact or logged in user
    :param contact: string/name of user
    :return: list of messages
    """
    conn = sqlite3.connect("Database/social.db")
    cur = conn.cursor()
    cur.execute(f"SELECT message FROM messages WHERE received = '{contact}' or via = '{contact}'")
    rows = cur.fetchall()
    conn.close()
    return rows

def test_list():
    return ["here's some text for a first message",
            "really? wow.",
            "I know right. lol :)"]
