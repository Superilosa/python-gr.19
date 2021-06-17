from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def empty():
    return ""


@app.route("/hello")
def hello():
    return "Hello World"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello - {name}"


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5555, debug=True)
    serve(app, host="0.0.0.0", port=5555)