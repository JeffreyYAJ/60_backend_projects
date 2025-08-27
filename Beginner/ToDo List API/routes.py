from flask import Flask, jsonify, request
from models import Tache
from app import app, db
from datetime import datetime


@app.route('/taches', methods=['GET'])
def get_tasks():
    taches = Tache.query.all()
    task_list = []
    for tache in taches:
        task_list.append({
            'id':tache.id, 'titre': tache.titre, 'description': tache.description, 'date_creation': tache.creation_date, 'date_fin': tache.end_date
        }) 
    return jsonify(task_list)

@app.route('/taches/<int:id>', methods=["GET"])
def get_task(id):
    tache = Tache.query.get(id)
    if tache:
        return jsonify({'id':tache.id, 'titre': tache.titre, 'description': tache.description, 'date_creation': tache.creation_date, 'date_fin': tache.end_date})
    
    return jsonify({'Message': "Tache inexistante"})

@app.route('/taches', methods = ['POST'])
def add_task():
    data = request.get_json()
    creation_date = datetime.strptime(data['date_creation'], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(data['date_fin'], '%Y-%m-%d %H:%M:%S')
    
    new_task = Tache(titre = data['titre'], description= data['description'], creation_date = creation_date , end_date = end_date)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"Message": "tache ajoutee"})

@app.route("/taches/<int:id>", methods = ['PUT'])
def update_task(id):
    
    data = request.get_json()
    tache = Tache.query.get(id)
    try:
        creation_date = datetime.strptime(data['date_creation'], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(data['date_fin'], '%Y-%m-%d %H:%M:%S')
    except KeyError:
        pass
    
    if tache:
        data = request.get_json()
        if 'titre' in data:
            tache.titre= data['titre']
        if 'description' in data:
            tache.description = data['description']
        if 'date_creation' in data:
            tache.creation_date = creation_date
        if 'date_fin' in data:
            tache.end_date = end_date
        db.session.commit()
        return jsonify({"Message": "Tache mis a jour"})
    return jsonify({"Message":"Tache inexistante"})

@app.route('/taches/<int:id>', methods = ['DELETE'])
def delete_task(id):
    tache= Tache.query.get(id)
    if tache:
        db.session.delete(tache)
        db.session.commit()
        return jsonify({"Message": "Tache supprimee"})
    return jsonify({"Message": "tache inexistante"})