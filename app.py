
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Port,Region,Price
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bugingo1@localhost/xeneta2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
migrate = Migrate(app, db)

def sql(rawSql, sqlVars={}):
 "Execute raw sql, optionally with prepared query"
 assert type(rawSql)==str
 assert type(sqlVars)==dict
 res=db.session.execute(rawSql, sqlVars)
 db.session.commit()
 return res

@app.route("/")
def hello_world():
    return "<p>Hello</p>"

@app.route('/rates', methods = ['GET'])
def login():
    if request.method == 'GET':
        date_from=request.args.get('date_from')
        date_to=request.args.get('date_to')
        origin=request.args.get('origin')
        destination=request.args.get('destination')

        results=sql("SELECT * FROM animals;")
        
        for result in results:
             print (result)

        return "day : {}, average_price: {}".format(result.day,result.price)

 
 


@app.route("/details")
def get_port():
    port=request.args.get('port')
    slug=request.args.get('slug')
    return "Port : {}, Slug: {}".format(port,slug)


if __name__ == '__main__':
    app.run(debug=True)