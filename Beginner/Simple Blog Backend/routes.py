from flask import Flask, jsonify, request
from models import Post
from app import app, db
from datetime import datetime

def translate_date(date):
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date
    
def translate_string(string):
    string = datetime.strftime(string, "%d-%m-%Y, %H:%M:%S")
    
@app.route('/create_post', methods = ['POST'])
def create_post():
    data =request.json()
    post = Post(title = data['title'], content = data['content'], author = data['content'], created_at = data['created_at'])
    db.session.add(post)
    db.session.commit()
    return jsonify({"Message":"Post created"})

@app.route('/get_post', methods = ['GET'])
def get_all_post():
    posts = Post.query.all()
    post_list = []
    for post in posts:
        post_list.append({
            "id": post.id, "title": post.title, "content": post.content, "author": post.author, "created_at": post.created_at
        }) 

    return jsonify(post_list)

@app.route('/get_post/<int:id>', methods = ['GET'])
def get_post(id):
    post = Post.query.get(id)
    if post:
        return jsonify({'id': post.id, 'title':post.title, 'content': post.content, 'author':post.author, 'created_at': post.created_at})
    return jsonify({"Error":"post not found"})

@app.route('/delete_post/<int:id>', methods = ['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"Message":"Post deleted"})
    return jsonify({"Error": "Post not found"})

@app.route('/update_post/<int:id>', methods = ['UPDATE'])
def update_post(id):
    data = request.json()
    post = Post.query.get(id)
    if post:
        if 'title' in data:
            post.title = data['title']
        if 'author' in data:
            post.author = data['author']
        if 'content' in data:
            post.content = data['content']
        db.session.commit()
        return jsonify({"Message":"Post updated"})
    return jsonify({"Error":"Post not found"})


    