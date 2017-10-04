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
    password= request.form['password']

    username_error=''
    password_error=''

    if username =='':
        username_error='Please enter a username (3-20 charcters)'
    
    if password != verify:
        password_error="Passwords do not match!"

    return render_template('index.html', username_error=username_error, password_error=password_error)

@app.route("/welcome", methods=['POST'])
def welcome():
    name= request.form['username']
    #DONE! tag/placeholder for username

    return render_template("welcome.html", name=name)
#redirect example: take to a whole new page
#render example: reload the same template with error info 
app.run()