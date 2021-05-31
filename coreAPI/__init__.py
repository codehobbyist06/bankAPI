from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from coreAPI.models import Post

app = Flask(__name__)
CORS(app)

user ='postgres'
pw ='1148'
dbase ='test'
host ='localhost'
port = '5432'


app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{pw}@{host}:{port}/{dbase}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from coreAPI import models, routes, queries