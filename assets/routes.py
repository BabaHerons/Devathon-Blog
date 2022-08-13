from flask import render_template, redirect, url_for, request
from assets import app, db
from assets.models import User, Posts, Comments, LikedPosts


@app.route('/')
def home():
    return render_template('home.html')         # here need to send signedIn = true or false as a string value.

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return render_template('home.html', signedIn = 'true', user = user)
    return render_template('signuporlogin.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        dp = request.files['dp']
        mob = request.form.get('mob')
        user = User.query.filter_by(username=username, password=password).first()
        if not user:
            user = User(username=username, password=password, email=email, fullname=fullname, dp=dp.read(), mob=mob)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('signuporlogin.html', signup = 'true')


