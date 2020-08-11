from flask import render_template, request, redirect, url_for

from app import app, dao


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def product_list():
    return render_template("products.html",
        products=dao.read_products(**dict(request.args)))

@app.route("/products/<int:category_id>")
def product_by_cat_id(category_id):
    return render_template("products.html", 
        products=dao.read_products_by_id(category_id))

@app.route("/products/add", methods=["GET", "POST"])
def add_or_update_product():
    err = ""
    if request.method.lower() == "post":
        if dao.add_products(**dict(request.form)):
            return redirect(url_for("product_list"))
        err = "Đã xãy ra lỗi!!! Vui lòng kiểm tra lại"
    return render_template("product-add.html", 
        categories=dao.read_categories(), 
        err=err)

if __name__ == "__main__":
    app.run(debug=True)
