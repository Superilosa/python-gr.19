from flask import Flask, request
import json
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/product-store.db"
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    category = db.Column(db.String(256))

    def to_dict(self):
        return {"name" : self.name, "quantity" : self.quantity, "price" : self.price, "category" : self.category}

    def get_id(self):
        return self.id


db.create_all()


@app.route("/")
def empty():
    return "Hello on products store"


@app.route("/create-product", methods=["POST"])
def create_product():
    name = request.args.get("name", None)
    quantity = request.args.get("quantity", None)
    price = request.args.get("price", None)
    category = request.args.get("category", None)
    new_product = Product(name=name, quantity=quantity, price=price, category=category)
    db.session.add(new_product)
    db.session.commit()
    return "Product added"


@app.route("/read-products")
def read_products():
    products_dict = {}
    header = {"content-type" : "application/json"}
    products = Product.query.filter_by().all()
    for product in products:
        id = product.get_id()
        products_dict[id] = product.to_dict()

    return json.dumps(products_dict), 200, header



if __name__ == '__main__':
    app.run(debug=True)