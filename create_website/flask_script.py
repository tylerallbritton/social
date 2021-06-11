from flask import Flask, render_template

# your get_values is in the same directory so you don't need to add a path
from get_values import list_messages, test_list
app = Flask(__name__)
# searched on "flask template call function example" to see that this next line is needed for custom functions
# you have to declare the functions you use in the template
# mine... test_list() is a test function I added to get_values.py
# you'll have to add your function
app.jinja_env.globals.update(test_list=test_list)

@app.route('/')
def home():
    return render_template("homepage.html", title="ChaseChat!", message="Welcome to my messaging website")


@app.route('/contacts/')
def contacts():
    return render_template("contacts.html", message="Contacts")


@app.route('/message/')
def messages():
    return render_template("messages.html", message="Messages")


if __name__ == "__main__":
    app.run(debug=True)
