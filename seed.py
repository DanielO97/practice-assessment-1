from app import app, db, Product, ProductType

product_types = ['tea', 'pot', 'utensil']
product_type_entries = []

for product_type in product_types:
    product_type_entries.append(ProductType(name=product_type))


products = [
    {
        'name': 'Princess Zi',
        'price': '89',
        'image': 'pot2',
        'type': product_type_entries[1],
        'is_featured': True,
    },
    {
        'name': 'Watergate',
        'price': '120',
        'image': 'pot2',
        'type': product_type_entries[1],
        'is_featured': True,
    },
    {
        'name': 'Yunnan',
        'price': '70',
        'image': 'pot3',
        'type': product_type_entries[1],
        'is_featured': True,
    },
    {
        'name': 'Bao Li',
        'price': '55',
        'image': 'pot4',
        'type': product_type_entries[1],
        'is_featured': True,
    },
    {
        'name': 'Handmade teadesk',
        'price': '150$',
        'image': 'utensil1',
        'type': product_type_entries[2],
        'is_featured': True,
    },
    {
        'name': 'Handmade ceramic tea cups',
        'price': '89$',
        'image': 'utensil2',
        'type': product_type_entries[2],
        'is_featured': True,
    },
    {
        'name': 'Burano Glass kettle',
        'price': '60$',
        'image': 'utensil3',
        'type': product_type_entries[2],
        'is_featured': True,
    },
    {
        'name': 'Super bottle',
        'price': '40$',
        'image': 'utensil4',
        'type': product_type_entries[2],
        'is_featured': True,
    },
    {
        'name': 'Silver style',
        'price': '30$',
        'image': 'utensil5',
        'type': product_type_entries[2],
        'is_featured': True,
    },
    {
        'name': 'Da Shu Cha',
        'price': '25$',
        'image': 'product1',
        'type': product_type_entries[0],
        'is_featured': True,
    },
    {
        'name': 'Qizi Beeng Cha',
        'price': '25$',
        'image': 'product2',
        'type': product_type_entries[0],
        'is_featured': True,
    },
    {
        'name': 'Ging May Cha',
        'price': '25$',
        'image': 'product3',
        'type': product_type_entries[0],
        'is_featured': True,
    },
    {
        'name': 'Yunnan QI Zi Bing Cha',
        'price': '35$',
        'image': 'product4',
        'type': product_type_entries[0],
        'is_featured': True,
    },
    {
        'name': 'Yunnan Bingcha',
        'price': '20$',
        'image': 'product5',
        'type': product_type_entries[0],
        'is_featured': True,
    },
]

product_entries = []
for product in products:
    entry = Product(
        name=product['name'],
        price=product['price'],
        image=product['image'],
        is_featured=product['is_featured'],
    )
    product['type'].products.append(entry)
    product_entries.append(entry)


with app.app_context():
    db.create_all()
    for entry in product_type_entries:
        db.session.add(entry)
    for entry in product_entries:
        db.session.add(entry)
    db.session.commit()
