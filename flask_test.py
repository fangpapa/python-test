from crypt import methods

import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python"

@app.route("/abc")
def hello2():
    return "Hello Python2"

@app.route("/abcdef", methods = ["POST"])
def hello3():
    return "Hello Python3"

if __name__ == "__main__":
    app.run()