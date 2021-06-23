from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def empty():
    return ""


@app.before_request
def before_request():
    print(request.remote_addr)


@app.route("/print/<text>")
def print_text(text):
    return text


@app.route("/hello")
def hell():
    return "Hi"


if __name__ == '__main__':
    app.run(debug=True)