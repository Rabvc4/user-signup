from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def submit():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if (password == "") or (" " in password):
        password_error = "That's not a valid password"
    elif ((len(password) < 3) or (len(password) > 20)):
        password_error = "That password is not the right length"
    if not (password == verify):
        verify_error = "Your passwords do not match"
    if (username == ""):
        username_error = "That's not a valid username"
    if (email == ""):
        email_error = ""
    elif not ("@." in email):
        email_error = "Not a valid email address"

    if (username_error or password_error or verify_error or email_error):
        return render_template('form.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

    new_username_escaped = cgi.escape(username, quote=True)

    return render_template('welcome.html', username=new_username_escaped)

@app.route("/")
def index():
    return render_template('form.html')

app.run()
