from app import app
import os
from flask import send_from_directory, jsonify, abort

@app.route('/<dir>')
def handleDir(dir):
    if os.path.exists(os.getcwd()+'/app/static/'+dir):
        return send_from_directory('static',dir)
    else:
        abort(404)

@app.route('/img/<file>')
def sendImage(file):
    return send_from_directory('img', file)
