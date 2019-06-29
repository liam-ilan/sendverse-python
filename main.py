import eventlet
eventlet.monkey_patch()

from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from flask_socketio import SocketIO

# Setup
app = Flask(__name__)
socketio = SocketIO(app)

# app globals
namespaces = []
count = 0

## routes
@app.route('/')
def homepage():
  return app.send_static_file('homepage/index.html')

# route creates chatroom. chatroom name is the string after /
@app.route('/<path>')
def chatroom(path):

  # make sure this is a unique new room
  if path not in namespaces:
    namespaces.append(path)

    # socket event listeners
    @socketio.on('connect', namespace='/' + path)
    def handle_connect(methods=['GET', 'POST']):
      global count
      count += 1

    # listen to messages in this namespace
    @socketio.on('message', namespace='/' + path)
    def handle_message(json):
      socketio.emit('message', json, namespace='/' + path, broadcast=True, include_self=False)
  
    @socketio.on('disconnect')
    def handle_disconnect(methods=['GET', 'POST']):
      global count
      count -= 1 if count else 0

  return app.send_static_file('chatroom/index.html')

# route accessed via homepage ajax call
@app.route('/data/count')
def handle_count():
  return jsonify({'online': count})

# static assets served from folders
@app.route('/<folder>/<path:path>')
def static_js(folder, path):
  return app.send_static_file(folder + '/' + path)

if __name__ == '__main__':
  socketio.run(app, debug=True)
