from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from pathlib import Path


app = Flask(__name__)
upload_dir = Path("uploaded")
if not upload_dir.exists():
    upload_dir.mkdir()


@app.route("/")
def empty():
    return ""


@app.route("/upload-file", methods=["POST"])
def upload_file():
    if "file" in request.files and request.files["file"]:
        file = request.files["file"]
        name = secure_filename(file.filename)
        if name[-3:] == "png" or name[-3:] == "pdf":
            file.save(upload_dir / name)
            return "File uploaded"
        abort(400, "Only png or pdf files allowed")
    abort(400, "No file sent")


if __name__ == '__main__':
    app.run(debug=True)