from app import app
from flask import render_template, request, jsonify, redirect
import json
import os, sqlite3

with open(os.getcwd() + '\data.json', 'r') as f:
    data = json.load(f)


@app.route("/")
def handleIndex():
    db = sqlite3.connect("blog.db")
    c = db.cursor()
    c.execute("SELECT * FROM projects")
    pjt = c.fetchall()[::-1]
    return render_template('home.html', data=data, card = pjt)


@app.route("/projects")
def handleProjects():
    return render_template('projects.html', data=data)


@app.route('/onsubmit', methods=["POST"])
def onsubmit():
    if request.method == 'POST':
        f = request.form
        if 'name' in f and 'email' in f and 'subject' in f and 'description' in f:
            db = sqlite3.connect('blog.db')
            c = db.cursor()
            c.execute("INSERT INTO requests VALUES('"+f["name"]+"','"+f["email"]+"','"+f["subject"]+"','"+f["description"]+"=')")
            db.commit()
            db.close()

            return render_template('on-submit.html')
    return redirect('/')

@app.route('/projects/template')
def handleTemp():
    return render_template('pjt_temp.html')