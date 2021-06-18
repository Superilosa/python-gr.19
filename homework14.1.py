from flask import Flask, request, abort
import json
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/library.db"
db = SQLAlchemy(app)
header = {"content-type": "application/json"}


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    year = db.Column(db.INTEGER)
    author = db.Column(db.String(64))
    quantity = db.Column(db.INTEGER)
    isbn = db.Column(db.String(32), unique=True)

    def to_dict(self):
        return {"name" : self.name, "year" : self.year, "author" : self.author, "quantity" : self.quantity, "isbn" : self.isbn}

    def get_id(self):
        return self.id


db.create_all()


@app.route("/")
def empty():
    return ""


@app.route("/books", methods=["GET", "POST"])
@app.route("/books/<id>", methods=["GET", "PUT", "DELETE"])
def books(id=None):
    if request.method == "POST":
        name = request.args.get("name", None)
        year = request.args.get("year", None)
        author = request.args.get("author", None)
        quantity = request.args.get("quantity", None)
        isbn = request.args.get("isbn", None)
        if name == None:
            abort(400, "Name is required for book")
        similar_isbn = Book.query.filter_by(isbn=isbn).first()
        if similar_isbn:
            abort(400, "Sent isbn already taken")
        new_book = Book(name=name, year=year, author=author, quantity=quantity, isbn=isbn)
        db.session.add(new_book)
        db.session.commit()
        return "Book added"

    elif request.method == "GET":
        if id == None:
            books_dict = {}
            books = Book.query.all()
            for book in books:
                id = book.get_id()
                books_dict[id] = book.to_dict()

            return json.dumps(books_dict), 200, header
        else:
            book = Book.query.filter_by(id=id).first()
            if book:
                return json.dumps(book.to_dict()), 200, header
            abort(404, "Book with given ID not found")

    elif request.method == "PUT":
        book = Book.query.filter_by(id=id).first()
        if book:
            name = request.args.get("name", None)
            year = request.args.get("year", None)
            author = request.args.get("author", None)
            quantity = request.args.get("quantity", None)
            isbn = request.args.get("isbn", None)
            if name != None:
                book.name = name
            if year != None:
                book.year = year
            if author != None:
                book.author = author
            if quantity != None:
                book.quantity = quantity
            if isbn != None:
                similar_isbn = Book.query.filter_by(isbn=isbn).first()
                if similar_isbn:
                    abort(400, "Sent isbn already taken")
                book.isbn = isbn
            db.session.add(book)
            db.session.commit()
            return "Book edited"
        else:
            abort(404, "Book with given ID not found")

    elif request.method == "DELETE":
        book = Book.query.filter_by(id=id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return "Book deleted"
        abort(404, "Book with given ID not found")


if __name__ == '__main__':
    app.run(debug=True)