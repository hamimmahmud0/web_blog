from app import app
from flask import jsonify,render_template, redirect, request, make_response, abort
import os, json, sqlite3
import time, random


app.config["IMAGE_UPLOADS"] = os.getcwd()+'/app/img'

with open(os.getcwd() + '\data.json', 'r') as f:
    data = json.load(f)

def random_string(length):
    string = ""
    seed = "abcdefghijklmnopqrstuvwxyz!@#$%12345908673450"
    for x in range(length):
        string += seed[random.randint(0, len(seed) - 1)]
    return string

class AdminCookie:
    def __init__(self):
        self.cookies = {}
    def is_cookie_valid(self, cookie):
        if cookie in self.cookies:
            return self.cookies[cookie] < time.time() + data["adminCookieLife"]*24*3600
        return False
    def new_cookie(self):
        tmp = random_string(62)
        if(tmp in self.cookies):
            tmp = self.new_cookie()
        self.cookies[tmp] = time.time()
        return tmp

adminCookie = AdminCookie()


@app.route("/wp-login")
def wplogin():
    if "adRay" in request.cookies:
        adRay = request.cookies.get("adRay")
        if adminCookie.is_cookie_valid(adRay):
            return redirect("/wp-admin", code=302)

    return render_template('wp-login.html')

@app.route('/login', methods=["POST"])
def login():
    if 'usr' in request.form and 'ps' in request.form:
        if request.form.get('usr') == data["admin"] and request.form.get('ps') == data["password"]:
            resp = make_response(redirect('/wp-admin',code=302))
            resp.set_cookie('adRay', adminCookie.new_cookie())
            return resp
    return redirect("/wp-login", code=302)

@app.route('/wp-admin')
def wpadmin():
    if "adRay" in request.cookies:
        adRay = request.cookies.get("adRay")
        if adminCookie.is_cookie_valid(adRay):
            db = sqlite3.connect("blog.db");
            c = db.cursor()
            c.execute("SELECT rowid, title, link, image, date FROM projects")
            a = c.fetchall()[::-1]
            c.execute("SELECT rowid, name, email, subject, description FROM requests")
            d = c.fetchall()[::-1]
            db.close()
            return render_template('wp-admin.html', data=data, projects = a, contacts = d)
    return redirect("/wp-login", code=302)

@app.route('/uploadproject', methods=["POST"])
def uploadproject():
    if "adRay" in request.cookies:
        adRay = request.cookies.get("adRay")
        if adminCookie.is_cookie_valid(adRay):
            f = request.form
            if 'link' in f and 'date' in f and 'label' in f and request.files:
                image = request.files["image"]
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                src = '/img/' + image.filename
                db = sqlite3.connect('blog.db')
                c = db.cursor()
                c.execute("INSERT INTO projects VALUES(\""+f["link"]+'\",\"'+f["date"]+'\",\"'+f["label"]+'\",\"'+src+"\")")
                db.commit()
                c.close()
                db.close()
                return redirect("/wp-admin")
    abort(404)

@app.route('/deleteproject', methods=["GET"])
def deleteProject():
    if 'rowid' in request.args:
        db = sqlite3.connect('blog.db')
        c = db.cursor()
        c.execute("DELETE FROM projects WHERE rowid = "+request.args["rowid"])
        db.commit()
        db.close()
    return redirect('/wp-admin')

@app.route('/deletecontact', methods=["GET"])
def deleteConatct():
    if 'rowid' in request.args:
        db = sqlite3.connect('blog.db')
        c = db.cursor()
        c.execute("DELETE FROM requests WHERE rowid = "+request.args["rowid"])
        db.commit()
        db.close()
    return redirect('/wp-admin')