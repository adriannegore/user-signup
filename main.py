from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate_info():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']

    username_error=''
    password_error=''
    verify_error=''
    email_error=''

    if username =='':
        username_error='Please enter a username (3-20 charcters)'
    elif not 3 <= len(username) <= 20:
        username_error='Username must be 3-20 characters long.'
    elif ' ' in username:
        username_error='No spaces allowed.'

    
    if password=='':
        password_error='Please enter a password (3-20 characters)'
    elif not 3 <= len(password) <= 20:
        password_error='Password must be 3-20 characters long.'
    elif ' ' in password:
        password_error='No spaces allowed.'
    
    if verify=='':
        verify_error='Please verify your password'
    elif password != verify:
        verify_error="Passwords do not match!"
    
    if not email=='':
        if not 3 <= len(email) <= 20:
            email_error='Email must be 3-20 characters long'
        elif not email.count('@')== 1 or not email.count('.') == 1 or ' ' in email:
            email_error="Please enter a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', 
            username_error=username_error, password_error=password_error, 
            verify_error=verify_error, email_error=email_error, 
            username=username, email=email)

### I don't really need the app route 
# because no one would ever need to go directly to my welcome page.
#The welcome is just some html to display###
#@app.route("/welcome")
#def welcome():
    #username=request.args.get('username')
    return render_template("welcome.html", username=username)
#redirect example: take to a whole new page
#render example: reload the same template with error info 
app.run()