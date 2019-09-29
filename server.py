from flask import Flask, render_template, send_from_directory, abort, send_file, safe_join
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    return render_template('intro-form.html')

@app.route('/static/<rfile>')
def images(rfile):
    try:
        return send_file(filename_or_fp=safe_join("./static/", rfile))
        #return send_from_directory("./static/",rfile, mimetype='text/plain')
    except:
        return abort(404)

if __name__ == '__main__':
    app.run(debug = True)
