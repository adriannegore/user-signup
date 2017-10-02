from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/" methods=['POST'])
def index():

    #if all the info is correct,
    #redirect ("/welcome.html")

    return render_template('index.html')

@app.route("/welcome")
def welcome():
    
    #add tag/placeholder for username

    return render_template("welcome.html")

app.run()