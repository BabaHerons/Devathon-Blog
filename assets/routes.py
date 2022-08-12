from flask import render_template, redirect, url_for, request
from assets import app, db

@app.route('/')
def home():
    return render_template('home.html')         # here need to send signedIn = true or false as a string value.


@app.route('/signup')
def signup():
    return 'signup page is working'

@app.route('/login')
def login():
    return 'login page is working'

