import hashlib

from flask import (jsonify, redirect, render_template, request, send_file,
                   session, url_for)

from app import app, dao, utils


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
        products=dao.read_products_by_category_id(category_id=category_id))

@app.route("/products/add", methods=["GET", "POST"])
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
        product = dao.read_products_by_id(product_id=product_id) 

    return render_template("product-add.html", 
        categories=dao.read_categories(),
        product=product,
        err=err)

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if dao.delete_product(product_id=product_id):
        return jsonify({
            "status": 200,
            "message": "successful",
            "data": {"product_id": product_id}
        })
    return jsonify({
        "status": 500,
        "message": "Failed"
    })

@app.route("/products/export")
def export_product():
    return send_file(utils.export_csv())

@app.route("/login", methods=["GET", "POST"])
def login():
    err_msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.validate_user(username=username, password=password)
        if user:
            session["user"] = user
            return redirect(url_for("index"))
        else:
            err_msg = "Đăng nhập không thành công"
    return render_template("login.html", err_msg=err_msg)

@app.route("/logout")
def logout():
    del session["user"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
