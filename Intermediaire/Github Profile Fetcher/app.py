from flask import Flask

app = Flask(__name__)
GITHUB_API_URL = "https://api.github.com/users/"

from routes import *

if __name__ == "__main__":
    app.run(debug = True)
