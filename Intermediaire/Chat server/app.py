from flask import Flask, render_template
from flask_socketio import SocketIO, send

app =  Flask(__name__)
app.config['SECRET_KEY'] = "secret123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def handle_connect():
    print('user connected')

@socketio.on('message')
def handle_message(message):
    print(f"Message received: {message}")
    send(message, broadcast=True)
    
@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')
    
@app.route('/')
def index():
    return "Server started"

@app.route('/app')
def show_app():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="192.168.46.144", port= 5000, debug=True)
    