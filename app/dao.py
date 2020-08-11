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

def read_products_by_id(category_id):
    return [product for product in read_products() if product["category_id"] == category_id]

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
    return update_products(products)
    
def update_products(products):
    try:
        with open(os.path.join(app.root_path, "data/products.json"), "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
            return True
    except expression as ex:
        print(ex)
        return False
    

def read_categories():
    with open(os.path.join(app.root_path, "data/categories.json"), encoding="utf-8") as f:
        return json.load(f)