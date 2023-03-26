from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')

pots = [
    {
        'name': 'Princess Zi',
        'price': '89',
        'image': 'pot2',
        'link':'/product/pots/princess-zi',
    },
    {'name': 'Reslience', 'price': '99', 'image': 'pot1', 'link':'/product/pots/reslience'},
    {'name': 'Watergate', 'price': '120', 'image': 'pot2', 'link':'/product/pots/watergate'},
    {'name': 'Yunnan', 'price': '70', 'image': 'pot3', 'link':'/product/pots/yunnan'},
    {'name': 'Bao Li', 'price': '55', 'image': 'pot4', 'link':'/product/pots/bao-li'},
]

utensils = [
    {
        'name': 'Handmade teadesk',
        'price': '150$',
        'image': 'utensil1',
        'link':'/product/utensils/handmade-teadesk',
    },
    {
        'name': 'Handmade ceramic tea cups',
        'price': '89$',
        'image': 'utensil2',
        'link':'/product/utensils/handmade-ceramic-tea-cups',
    },
    {
        'name': 'Burano Glass kettle',
        'price': '60$',
        'image': 'utensil3',
        'link':'/product/utensils/burano-glass-kettle',
    },
    {
        'name': 'Super bottle',
        'price': '40$',
        'image': 'utensil4',
        'link':'/product/utensils/super-bottle',
    },
    {
        'name': 'Silver style',
        'price': '30$',
        'image': 'utensil5',
        'link':'/product/utensils/silver-style',
    },
]
tea = [
    {
        'name': 'Da Shu Cha',
        'price': '25$',
        'image': 'product1',
        'link':'/product/tea/du-shu-cha',
    },
    {
        'name': 'Qizi Beeng Cha',
        'price': '25$',
        'image': 'product2',
        'link':'/product/tea/qizi-beeng-cha',
    },
    {
        'name': 'Ging May Cha',
        'price': '25$',
        'image': 'product3',
        'link':'/product/tea/ging-may-cha',
    },
    {
        'name': 'Yunnan QI Zi Bing Cha',
        'price': '35$',
        'image': 'product4',
        'link':'/product/tea/yunnan-qi-zi-bing-cha',
    },
    {
        'name': 'Yunnan Bingcha',
        'price': '20$',
        'image': 'product5',
        'link':'/product/tea/yunnan-bing-cha',
    },
]


@app.route('/')
def index():
    return render_template('index.html', pots=pots, utensils=utensils, tea=tea)


@app.route('/product/<product_type>/<name>')
def product_route(product_type, name):
    return render_template('product.html', product_type=product_type, name=name)

@app.route('/buy/product/<product_type>/<name>')
def buy_product(product_type, name):
    return render_template('buy.html', product_type=product_type, name=name)

if __name__ == '__main__':
    app.run()
