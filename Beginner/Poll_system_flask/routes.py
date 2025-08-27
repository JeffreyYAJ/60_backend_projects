from flask import Flask, request, jsonify
import json
from models import Poll, Option
from app import db, app

@app.route('/polls', methods = ['POST'])
def create_poll():
    data = request.json()
    question =data.get('question')
    if not question:
        return jsonify({"error": "No question provided"})
    options = data.get('options', [])
    poll = Poll(question=question)
    for option in options:
        option_text = option.get('option_text')
        if option_text:
            poll.options.append(Option(option_text=option_text))
    db.session.add(poll)
    db.session.commit()
    return jsonify({"message": "Poll created successfully", "poll_id": poll.id})

@app.route('/polls/<int:poll_id>', methods=['GET'])
def get_poll(poll_id):
    poll = Poll.query.get(poll_id)
    if not poll:
        return jsonify({"Error": "Poll not existing"})
    for option in poll.options:
        poll.options.append({"id":option.id, "option_text": option.option_text, "votes": option.votes})
        
    return jsonify({"id": poll.id, "question": poll.question, "options": poll.options})

@app.route('/polls/<int:poll_id>/vote', methods=['POST'])
def vote_poll(poll_id):
    data = request.json()
    option_id = data.get('option_id')
    if not option_id:
        return jsonify({"Message": "No option selected"})
    poll = Poll.query.get(poll_id)
    if not poll:
        return jsonify({"Error": "Poll not found"})
    option = Option.query.get(option_id)
    if not option:
        return jsonify({"Error": "Option not existing"})
    option.votes += 1
    
    db.session.commit()
    return jsonify({"Message": "Vote saved"})

 
