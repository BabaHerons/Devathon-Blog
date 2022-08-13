from assets import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(11), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(30), nullable=False)
    fullname = db.Column(db.String(25), nullable=False)
    dp = db.Column(db.LargeBinary, nullable=True)
    mob = db.Column(db.String(10), nullable=True)

class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    post_heading = db.Column(db.String)
    post = db.Column(db.String(5000), nullable = False, unique = True)
    likes_count = db.Column(db.Integer(), nullable=True)
    dislikes_count = db.Column(db.Integer(), nullable=True)
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'))
    post_userfullname = db.Column(db.String(25), db.ForeignKey('user.fullname'))

class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    comment = db.Column(db.String(1000), nullable = False)
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'))
    postid = db.Column(db.Integer(), db.ForeignKey('posts.id'))

class LikedPosts(db.Model):
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key = True)
    postid = db.Column(db.Integer(), db.ForeignKey('posts.id'), primary_key = True)