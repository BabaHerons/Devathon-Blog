from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

assetsFolder = os.path.abspath(os.path.dirname(__file__))
databasePath = 'sqlite:///' + os.path.join(assetsFolder, 'blog_database.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databasePath
db = SQLAlchemy(app)


from assets import routes