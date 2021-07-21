from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bugingo1@localhost/xeneta'

db=SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello</p>"

@app.route("/rates/",methods=['GET'])
def hello_world():
    return "<p>Xeneta task</p>"