from flask import Flask, request, jsonify
from models import Movie
from app import db, app

@app.route('/movies', methods = ["POST"])
def add_movie():
    data = request.get_json()
    movie = Movie(name = data['name'], genre = data['genre'], year = data['year'], description = data.get('description', ''))
    db.session.add(movie)
    db.session.commit()
    return jsonify({"Message": "Movie added"})

@app.route('/movie', methods = ['GET'])
def get_movies():
    movies = Movie.query.all()
    movie_list = []
    for movie in movies:
        movie_list.append(movie.to_dict())
    return jsonify(movie_list)

@app.route('/movie/search', methods = ['GET'])
def search_movie():
    title = request.args.get('name', '')
    genre = request.args.get('genre', '')
    year = request.args.get('year', '')
     
    # query = Movie.query
    if title:
        query = Movie.query.filter(Movie.name.ilike(f"%{title}%"))    
    if genre:
        query = Movie.query.filter(Movie.genre.ilike(f"%{genre}%"))
    if year:
        query = Movie.query.filter(Movie.year.ilike(f"%{year}%"))
        
    result = Movie.query.all()
    movie_got = []
    for movie in result:
        movie_got.append(movie)
    return jsonify(movie_got)


    