from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Port,Region,Price
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bugingo1@localhost/xeneta'
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

@app.route("/", methods = ['GET'])
def get_port():
    
    results = db.session.query(Port).filter(Port.code=='IESNN')
    return render_template("ports.html", results=results)

@app.route('/rates', methods = ['GET'])
def login():
    if request.method == 'GET':
        date_from=request.args.get('date_from')
        date_to=request.args.get('date_to')
        origin=request.args.get('origin')
        destination=request.args.get('destination')

    results = sql("select day ,count(day),count(distinct(dest_code)) as port_no, sum(price),avg(price) from public.prices where orig_code='CNSGH' and dest_code in (SELECT code FROM public.ports where parent_slug ='north_europe_main') and day BETWEEN '2016-01-01' AND '2016-01-10' group by day order by day ;")
    return render_template("ports.html", results=results)
        
        # for result in results:
        #      print (result)

        # return "day : {}, average_price: {}".format(result.day,result.price)

 
 


if __name__ == '__main__':
    from flask_sqlalchemy import get_debug_queries
    app.run(debug=True)

   