import json
import os

from app import app


def read_products(keyword=None, from_price=None, to_price=None):
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        products = json.load(f)
        if keyword:
            return [product for product in products if keyword.lower().strip() in product["name"].lower()]
        if from_price and to_price:
            return [product for product in products 
                if float(from_price) <= product["price"] and product["price"] <= float(to_price)]
        return products

def read_products_by_category_id(category_id):
    return [product for product in read_products() if product["category_id"] == category_id]

def read_products_by_id(product_id):
    products = read_products()
    for product in products:
        if product["id"] == int(product_id):
            return product
    return None

def write_products(products):
    try:
        with open(os.path.join(app.root_path, "data/products.json"), "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
            return True
    except expression as ex:
        print(ex)
        return False

def add_products(name, description, price, images, category_id):
    products = read_products()
    products.append({
        "id": len(products) + 1,
        "name": name,
        "description": description,
        "price": float(price),
        "images": images,
        "category_id": int(category_id)
    })
    return write_products(products)
    
def update_products(product_id, name, description, price, images, category_id):
    products = read_products()
    for product in products:
        if product["id"] == int(product_id):
            product["name"] = name
            product["description"] = description
            product["price"] = float(price)
            product["images"] = images
            product["category_id"] = int(category_id)
            break
    return write_products(products)

def delete_product(product_id):
    products = read_products()
    for idx, product in enumerate(products):
        if product["id"] == int(product_id):
            del products[idx]
            break
    return write_products(products)

def read_categories():
    with open(os.path.join(app.root_path, "data/categories.json"), encoding="utf-8") as f:
        return json.load(f)

def read_users():
    with open(os.path.join(app.root_path, "data/users.json"), encoding="utf-8") as f:
        return json.load(f)
