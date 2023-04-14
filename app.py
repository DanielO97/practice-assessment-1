from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.db')
db.init_app(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_featured = db.Column(db.Boolean, default=False)
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))


class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    products = db.relationship('Product', backref='product_type')


@app.route('/')
def index():
    entries = Product.query.filter(Product.is_featured.is_(True)).all()
    featured = {
        'pot': [],
        'utensil': [],
        'tea': [],
    }
    for entry in entries:
        featured[entry.product_type.name].append(entry)
    return render_template('index.html', pots=featured['pot'], utensils=featured['utensil'], tea=featured['tea'])


@app.route('/products')
def all_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/product/<id>')
def product_route(id):
    product = Product.query.filter(Product.id.is_(id)).first()
    return render_template('product.html', product=product)


@app.route('/buy/<id>')
def buy_product(id):
    product = Product.query.filter(Product.id.is_(id)).first()
    return render_template('buy.html', product=product)


if __name__ == '__main__':
    app.run()
