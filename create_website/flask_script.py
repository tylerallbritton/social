from flask import Flask, render_template, request

# your get_values is in the same directory so you don't need to add a path
from get_values import list_messages, list_contacts, send_message

app = Flask(__name__)
# searched on "flask template call function example" to see that this next line is needed for custom functions
# you have to declare the functions you use in the template
# mine... test_list() is a test function I added to get_values.py
# you'll have to add your function
app.jinja_env.globals.update(list_messages=list_messages)
app.jinja_env.globals.update(list_contacts=list_contacts)


@app.route('/')
def home():
    return render_template("homepage.html", title="ChaseChat!", message="Welcome to my messaging website")


@app.route('/contacts/')
def contacts():
    return render_template("contacts.html", message="Contacts")


@app.route('/messages/', methods=['POST', 'GET'])
def messages():
    if request.method == 'GET':
        return render_template("messages.html", message="Messages")
    if request.method == 'POST':
        form_data = request.form
        send_message("Chase", "Dad", form_data['message'])
        return render_template("messages.html", message="Messages")


if __name__ == "__main__":
    app.run(debug=True)
