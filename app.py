from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static', 'images')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
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

@app.route('/product/<id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    if request.method == 'POST':
        product = Product.query.filter(Product.id.is_(id)).first()
        product.name = request.form['name']
        if request.files['image'].filename:
            product.image = request.files['image'].filename
            request.files['image'].save(os.path.join(app.config['UPLOAD_FOLDER'], product.image))
        product.price = request.form['price']
        product.is_featured = request.form['is_featured'] == 'on'
        product.product_type_id = request.form['product_type_id']
        db.session.commit()
        return redirect(url_for('edit_product', id=id))
    else:
        product = Product.query.filter(Product.id.is_(id)).first()
        return render_template('edit.html', product=product, product_types=ProductType.query.all())

@app.route('/product/<id>/delete', methods=['POST'])
def delete_product(id):
    product = Product.query.filter(Product.id.is_(id)).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('all_products'))

@app.route('/product/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            image=request.files['image'].filename,
            price=request.form['price'],
            is_featured=request.form['is_featured'] == 'on',
            product_type_id=request.form['product_type_id'],
        )
        db.session.add(product)
        db.session.commit()
        request.files['image'].save(os.path.join(app.config['UPLOAD_FOLDER'], product.image))
        return redirect(url_for('all_products'))
    else:
        return render_template('create.html', product_types=ProductType.query.all())

@app.route('/buy/<id>')
def buy_product(id):
    product = Product.query.filter(Product.id.is_(id)).first()
    return render_template('buy.html', product=product)


if __name__ == '__main__':
    app.run(debug=False)
