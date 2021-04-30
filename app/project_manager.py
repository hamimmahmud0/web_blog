from app import app
import sqlite3

from flask import jsonify, request, abort



project_per_page = 2;

@app.route('/projects/get', methods = ["GET"])
def handleProjectGet():
    if "p" in request.args:
        p = request.args["p"]
        p = int(p)
        db = sqlite3.connect('blog.db')
        c = db.cursor()
        c.execute("SELECT * FROM projects")
        data = c.fetchall()
        print(data)
        if len(data) < project_per_page:
            return jsonify(data)
        data = data[::-1][p*2:(p+1)*2]
        return jsonify(data)
    abort(403)

