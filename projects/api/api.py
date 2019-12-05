import flask
from flask import jsonify
from select_all import select_all

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return (
        "<h1>This is the home page for the Python Server</h1>"
        "<p>This is where we will right queries from</p>"
    )


@app.route('/all', methods=['GET'])
def all_things():
    all_things_ = select_all()
    return jsonify(all_things_)


# This starts the server at http://127.0.0.1:5000/
app.run()
