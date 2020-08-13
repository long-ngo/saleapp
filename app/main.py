from flask import redirect, render_template, request, url_for

from app import app, dao

import hashlib


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def product_list():
    return render_template("products.html",
        products=dao.read_products(**dict(request.args)))

@app.route("/products/<int:category_id>")
def product_by_category_id(category_id):
    return render_template("products.html", 
        products=dao.read_products_by_category_id(category_id))

@app.route("/products/add", methods=["get", "post"])
def add_or_update_product():
    product_id = request.args.get("product_id")
    product = None
    err = None

    if request.method == "POST":
        if product_id:
            data = dict(request.form.copy())
            data["product_id"] = product_id
            if dao.update_products(**data):
                return redirect(url_for("product_list"))
        else:
            if dao.add_products(**dict(request.form)):
                return redirect(url_for("product_list"))
        err = "Đã xãy ra lỗi!!! Vui lòng kiểm tra lại"

    if product_id:
        product = dao.read_products_by_id(product_id) 

    return render_template("product-add.html", 
        categories=dao.read_categories(),
        product=product,
        err=err)

@app.route("/login", methods=["get", "post"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
