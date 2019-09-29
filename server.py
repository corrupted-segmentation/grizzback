from flask import Flask, render_template, send_from_directory, abort, send_file, safe_join, request
import magic
app = Flask(__name__)


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
