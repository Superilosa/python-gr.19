from flask import Flask, request, abort, send_file
from pathlib import Path


app = Flask(__name__)
files_dir = Path("btu-data")


@app.route("/")
def empty():
    return ""


@app.route("/download")
def download():
    name = request.args.get("filename", None)
    if name != None and name != "":
        file = files_dir / name
        if file.exists():
            return send_file(file)
        abort(404, "File not found")
    abort(400, "No filename sent")


if __name__ == '__main__':
    app.run(debug=True)