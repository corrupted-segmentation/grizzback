from flask import Flask, render_template, send_from_directory, abort, send_file, safe_join, request
import magic
from sqlite3 import dbapi2 as sqlite
from flask_sqlalchemy import SQLAlchemy
import schedule
import emailler
import urllib.parse
import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///../grizzback/pizza.db'

db = SQLAlchemy(app)

pizzaCal = {"cheese": 1950, "pepperoni": 2210, "meat": 3020, "hawaiian": 2210}
revPizzaCal = dict((v,k) for k,v in pizzaCal.items())

class User(db.Model):
    email = db.Column(db.String(80))
    name = db.Column(db.String(50))
    team = db.Column(db.String(20))
    userid = db.Column(db.String(130), primary_key=True)

class Ptypes(db.Model):
    types = db.Column(db.String(11), primary_key=True)
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
    fName = urllib.parse.quote(request.form.get("fullName"))
    eMail = urllib.parse.quote(request.form.get("email"))
    userId = fName + eMail
    user = User(email=eMail, name=fName, team=request.form.get("team"), userid=userId)
    db.session.add(user)
    for pizza in request.form.getlist('pizzas'):
        thing = Ptypes(types=pizza, userid=userId )
        db.session.add(thing)

    db.session.commit()

    #print("\n\nSchedule:")
    #print(schedule.nextGame(request.form.get("team")))

    if(schedule.nextGame("now") == "now"):
        emailler.sendEmail(userId)

    return "nice job"

@app.route('/emailForm/<uid>/<mood>')
def emailForm(uid, mood):
    uid = urllib.parse.quote(uid)
    pizzaS = Ptypes.query.filter_by(userid=uid).all()

    rec =""
    cal = []
    for piz in pizzaS:
        if(pizzaCal.get(piz.types, -1) != -1):
            cal.append(pizzaCal.get(piz.types))
        
    cal.sort()
    if(mood == "vsad" or mood =="sad"):
        rec = revPizzaCal.get(max(cal))
    elif(mood == "vhappy" or mood=="happy"):
        rec = revPizzaCal.get(min(cal))
    else:
        rec = revPizzaCal.get(statistics.median_high(cal))

    return render_template("mood.html", pizza=rec, mood=mood)

        


#serving static files like images and js
@app.route('/static/<rfile>')
def images(rfile):
    try:
        return send_from_directory("./static/",rfile, mimetype=magic.from_file(safe_join("./static/", rfile), mime=True))
    except:
        return abort(404)


if __name__ == '__main__':
    app.run(debug = True)
