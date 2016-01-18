from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
import os, random, uuid
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'testapi.db')
db = SQLAlchemy(app)
CORS(app)

class Merchant(db.Model):
    merchant_id = db.Column(db.Integer, primary_key=True)
    merchant_name = db.Column(db.String())
    
    def __init__(self, merchant_name):
        self.merchant_name = merchant_name

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    goods_total = db.Column(db.Integer)
    grand_total = db.Column(db.Float) #db.Numeric
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    m_id = db.Column(db.Integer, db.ForeignKey('merchant.merchant_id'))
    merchant = db.relationship('Merchant', backref='orders')
    
    def __init__(self, merchant_id):
        self.m_id = merchant_id
        self.goods_total = random.randint(1,10)
        self.grand_total = float(random.randint(1,10))
        self.status = 'new'
        self.transaction_id = str(uuid.uuid4())

    
db.drop_all()
db.create_all()

def sample_data():
    iMerchants=[]
    iOrders=[]
    for iMerchant in range(2):
        m = Merchant('testmerchant'+str(iMerchant))
        iMerchants.append(m)
        db.session.add(m)
        db.session.commit()
        for iOrder in range(30):
            o = Order(m.merchant_id)
            iOrders.append(o)
            db.session.add(o)
            db.session.commit()
        

sample_data()

import flask.ext.restless

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Order, methods=['GET', 'POST', 'PATCH', 'DELETE'])

# start the flask loop
app.run(host='0.0.0.0',debug=True)
