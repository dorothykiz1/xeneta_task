from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Port(db.Model):
    __tablename__ = 'ports'
 
    code = db.Column(db.Text, primary_key = True)
    name = db.Column(db.String())
    parent_slug = db.Column(db.String())
     
    def __init__(self, code,name,parent_slug):
        self.code = code
        self.name = name
        self.parent_slug = parent_slug

 
    def __repr__(self):
        return f"{self.code}:{self.parent_slug}"

class Price(db.Model):
    __tablename__ = 'prices'
 
    id = db.Column(db.Integer, primary_key = True)
    orig_code = db.Column(db.String())
    dest_code = db.Column(db.String())
    day = db.Column(db.Date())
    price = db.Column(db.Integer())

     
    def __init__(self, orig_code,dest_code,day,price):
        self.orig_code = orig_code
        self.dest_code = dest_code
        self.day = day
        self.price = price


 
    def __repr__(self):
        return f"{self.orig_code}:{self.price}"


class Region(db.Model):
    __tablename__ = 'regions'
 
    slug = db.Column(db.Text, primary_key = True)
    name = db.Column(db.String())
    parent_slug = db.Column(db.String())
     
    def __init__(self,slug,name,parent_slug):
        self.name = name
        self.slug = slug
        self.parent_slug = parent_slug

 
    def __repr__(self):
        return f"{self.slug}:{self.parent_slug}"

