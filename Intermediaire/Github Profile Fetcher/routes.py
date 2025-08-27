from flask import Flask, request, jsonify
from app import app, GITHUB_API_URL
import requests

@app.route('/<username>', methods = ['GET'])
def get_profile(username):
    url = f"{GITHUB_API_URL}{username}"
    resp = requests.get(url)
    if resp.status_code == 404:
        return jsonify({'error':'User not found'})
    if resp.status_code != 200:
        return jsonify({'error':'Failed to fetch data. Check your internet connection'})

    data = resp.json()

    
    profile = {
            "login": data.get('login'),
            
            "repos_url": data.get('repos_url'),
            "name": data.get("name"),
            "blog": data.get('blog'),
            "location": data.get('location'),
            "email": data.get('email'),
            "hireable": data.get('hireable'),
            "bio": data.get('bio'),
            "public_repos": data.get('public_repos'),
            "public_gists": data.get('public_gists'),
            "followers": data.get('followers'),
            "following": data.get('following'),
            "created_at": data.get('created_at'),
            "updated_at": data.get('updated_at')        
            }

    return jsonify(profile)
    
    
