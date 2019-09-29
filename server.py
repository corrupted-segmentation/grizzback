from flask import Flask, render_template, send_from_directory, abort, send_file, safe_join, request
import magic
from sqlite3 import dbapi2 as sqlite
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///../grizzback/pizza.db'

db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String(80))
    name = db.Column(db.String(50))
    team = db.Column(db.String(20))
    userid = db.Column(db.String(130), primary_key=True)

class ptypes(db.Model):
    pizzatypes = db.Column(db.String(11), primary_key=True)
    userid = db.Column(db.String(130), primary_key=True)

#nav bar routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    return render_template('intro-form.html')

#api stuff
@app.route('/inForm', methods=['POST'])
def inForm():
    print(request.form)
    userid = request.form.get("name") + request.form.get("email")
    user = User(email=request.form.get("email"), name=request.form.get("name"), team=request.form.get("team"), userid)
    db.session.add(user)
    return "nice job"

#serving static files like images and js
@app.route('/static/<rfile>')
def images(rfile):
    try:
        return send_from_directory("./static/",rfile, mimetype=magic.from_file(safe_join("./static/", rfile), mime=True))
    except:
        return abort(404)


if __name__ == '__main__':
    app.run(debug = True)
