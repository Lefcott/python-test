from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html", multichannel='MULTIchannel')


@app.route('/favicon.png')
def favicon():
    return render_template("favicon.png")
@app.route('/style.css')
def style():
    return render_template("style.css")

# @app.route('/')
# def index():
#     return "Hello World!"


if __name__ == '__main__':
    app.run()
