from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.html", message2="Welcome to my website")


@app.route('/contacts/')
def contacts():
    return render_template("contacts.html", message="Contacts", message2="Here are your contacts")


@app.route('/message/')
def messages():
    return render_template("message.html", message="Messages", message2="Your messages will appear here")


if __name__ == "__main__":
    app.run(debug=True)
