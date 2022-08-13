from flask import render_template, redirect, url_for, request, session
from assets import app, db
from assets.models import User, Posts, Comments, LikedPosts


@app.route('/')
def home():
    posts = Posts.query.all()
    posts.reverse()
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
    else:
        user = ''
    return render_template('home.html', posts = posts, user=user)         # here need to send signedIn = true or false as a string value.

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('signuporlogin.html')

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('home'))

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

@app.route('/create-post', methods = ['GET', 'POST'])
def create_post():
    user = User.query.filter_by(username = session['username']).first()
    if request.method == 'POST':
        heading = request.form.get('heading')
        post = request.form.get('post')
        
        if not Posts.query.filter_by(post=post).first():
            postObject = Posts(post=post, userid=user.id, post_heading=heading, post_userfullname=user.fullname)
            db.session.add(postObject)
            db.session.commit()
            return redirect(url_for('home'))
    return redirect(url_for('home'))

