from flask import Flask, jsonify
import json

app = Flask(__name__)

dict = {"Dictionary" : True, "Info" : "Text", "Number" : 1}
json_header = {"content-type" : "application/json"}


@app.route("/")
def empty():
    return ""


@app.after_request
def after_request(response):
    if response.content_type == "dict":
        return jsonify(response)
    return response


@app.route("/dictionary")
def dictionary():
    return dict


@app.route("/json")
def return_json():
    return json.dumps(dict), 200, json_header



if __name__ == '__main__':
    app.run(debug=True)