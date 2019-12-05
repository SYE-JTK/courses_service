import flask
from queries import all_stud, depts

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
    return all_stud()


@app.route('/dept', methods=['GET'])
def all_dept():
    return depts()


# This starts the server at http://127.0.0.1:5000/
app.run()
