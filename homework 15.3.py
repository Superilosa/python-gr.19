from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/products.db"
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)


    def to_dict(self):
        return {"id" : self.id, "name" : self.name, "quantity" : self.quantity, "price" : self.price}


db.create_all()


@app.route("/")
def empty():
    return ""


@app.route("/add_product", methods=["POST"])
def add_product():
    name = request.args.get("name", None)
    quantity = request.args.get("quantity", None)
    price = request.args.get("price", None)
    new_product = Product(name=name, quantity=quantity, price=price)
    db.session.add(new_product)
    db.session.commit()
    return "Product added"


@app.route("/get_products")
@app.route("/get_products/<filter>")
def get_products(filter=None):
    products_query = Product.query

    if filter != None:

        if filter == "id":
            id = request.args.get("id", None)
            if id == None or id == "":
                abort(400, "No id sent for filtering")
            try:
                int(id)
            except ValueError:
                abort(400, "Id must be a real number")
            products_query = products_query.filter(Product.id == int(id))

        elif filter == "name":
            name = request.args.get("name", None)
            if name == None or name == "":
                abort(400, "No name sent for filtering")
            products_query = products_query.filter(Product.name.contains(name))

        elif filter == "quantity":
            quantity = request.args.get("quantity", None)
            if quantity == None or quantity == "":
                abort(400, "No quantity sent for filtering")
            try:
                int(quantity)
            except ValueError:
                abort(400, "Quantity must be a real number")
            operation = request.args.get("operation", "=")
            if operation == "=" or operation == "==":
                products_query = products_query.filter(Product.quantity == float(quantity))
            elif operation == ">":
                products_query = products_query.filter(Product.quantity > float(quantity))
            elif operation == "<":
                products_query = products_query.filter(Product.quantity < float(quantity))
            elif operation == ">=":
                products_query = products_query.filter(Product.quantity >= float(quantity))
            elif operation == "<=":
                products_query = products_query.filter(Product.quantity <= float(quantity))
            else:
                abort(400, "Invalid operation")

        elif filter == "price":
            price = request.args.get("price", None)
            if price == None or price == "":
                abort(400, "No price sent for filtering")
            try:
                float(price)
            except ValueError:
                abort(400, "Price must be a number")
            operation = request.args.get("operation", "=")
            if operation == "=" or operation == "==":
                products_query = products_query.filter(Product.price == float(price))
            elif operation == ">":
                products_query = products_query.filter(Product.price > float(price))
            elif operation == "<":
                products_query = products_query.filter(Product.price < float(price))
            elif operation == ">=":
                products_query = products_query.filter(Product.price >= float(price))
            elif operation == "<=":
                products_query = products_query.filter(Product.price <= float(price))
            else:
                abort(400, "Invalid operation")

        else:
            abort(400, "Invalid filter")


    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per-page", 5))
    products_query = products_query.paginate(page, per_page)
    products = [p.to_dict() for p in products_query.items]
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)