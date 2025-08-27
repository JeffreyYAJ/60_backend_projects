from flask import Flask , request, jsonify, redirect
from models import URL
from app import app, db
from datetime import datetime
import random, string

def shorten_string(url):
    """Generates a random string of 6 characters for the shortened URL."""
    characters =  string.ascii_letters + string.digits
    return request.host_url + ''.join(random.choice(characters) for _ in range(3))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    creation_date = datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S")
    new_url = URL(original_url=data['original_url'], shorten_url=shorten_string(data['original_url']), created_at=creation_date)
    db.session.add(new_url)
    db.session.commit()
    return jsonify({"shortened_url": new_url.shorten_url})

@app.route('/<shorten_url>', methods=["GET"])
def redirect_url(shorten_url):
    url = URL.query.filter_by(shorten_url = shorten_url)
    if url.first():
        return redirect(url.first().original_url)
    return jsonify({"Error":"URL not found"})
    
    
@app.route('/urls', methods = ["GET"])
def list_urls():
    urls = URL.query.all()
    url_list = []
    for url in urls:
        url_list.append({"original_url":url.original_url, "shorten_url":url.shorten_url, "created_at":url.created_at.strftime("%Y-%m-%d %H:%M:%S")})
    return jsonify(url_list)

@app.route('/urls/<shorten_url>', methods = ['DELETE'])
def delete_shorten_url(shorten_url):
    url = URL.query.get(shorten_url)
    if url:
        db.session.delete(url)
        db.session.commit()
        return jsonify({"Message":"URL deleted"})
    return jsonify({"Error":"URL not found"})

@app.route('/test')
def test():
    return jsonify({"Message":"Test successful"})
    