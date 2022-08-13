from flask import render_template, redirect, url_for, request
from assets import app, db


@app.route('/')
def home():
    return render_template('home.html')         # here need to send signedIn = true or false as a string value.

@app.route('/login')
def login():
    return render_template('signuporlogin.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    return render_template('signuporlogin.html')


