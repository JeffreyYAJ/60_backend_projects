from flask import Flask, request, jsonify
from app import app, db
from models import Product

@app.route('/api/products', methods = ['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for p in products:
        product_list.append(p.to_dict)
    return jsonify(product_list)
    
@app.route('/api/products/<int:id>', methods= ['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error":"Product not found"})
    return jsonify(product.to_dict())

@app.route('/api/products', methods = ['POST'])
def register_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({"error": "Missing required fields"})
    product = Product(
        name = data['name'],
        description = data.get("description", ""),
        price = data["price"],
        stock = data['stock']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"Message":"Product added"})

@app.route('/api/products/<int:id>', methods = ["UPDATE"])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"Message":"Product not found"})
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    
    db.session.commit()
    return jsonify({"Message":"Product modified"})

@app.route('/api/products/<int:id>', methods = ["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"Message":"Product not found"})
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"Message":"Product deleted"})
