from flask import Flask, request, jsonify
from models import Contact
from app import app, db

@app.route('/contact', methods= ['GET'])
def get_all_contacts():
    contacts = Contact.query.all()
    contact_list = []
    for contact in contacts:
        contact_list.append({
            "id": contact.id,
            "name": contact.name,
            "number":  contact.number,
            "email": contact.email           
        })
    return jsonify(contact_list)

@app.route('/contact/<int:id>', methods = ['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    if contact:
        return jsonify({"id": contact.id,"name": contact.name, "number": contact.number, "email": contact.email})
    
    return jsonify({"Error": "Contact inexistant"})

@app.route('/contact', methods = ["POST"])
def add_contact():
    data = request.get_json()
    if 'email' in data:
        new_contact = Contact(name = data['name'], number= data['number'], email=data['email'])
    else:
        new_contact = Contact(name = data['name'], number= data['number'], email="")
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"Mesage": " contact enregistree"})


@app.route('/contact/<int:id>', methods = ['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)
    if contact:
        data = request.get_json()
        if 'name' in data:
            contact.name = data['name']
        if 'number' in data:
            contact.number = data['number']
        if 'email' in data:
            contact.email = data['email']
        db.session.commit()
        return jsonify({"Message": "contact modifier"})
    
    return jsonify({"Error": "Contact inexistant"})

@app.route('/contact/<int:id>', methods = ["DELETE"])
def delete_contact():
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"Message": "Contact supprimer"})
    return jsonify({"Error":  "Erreur de suppresion"})