from flask import render_template, request

from app import app, dao


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def product_list():
    req = request.args
    return render_template("products.html", products=dao.read_products(
        req.get("keyword"),
        req.get("from_price"),
        req.get("to_price")
        ))

@app.route("/products/<int:category_id>")
def product_by_cat_id(category_id):
    return render_template("products.html", products=dao.read_products_by_category_id(category_id))

if __name__ == "__main__":
    app.run(debug=True)
