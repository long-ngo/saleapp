import json
import os

from app import app


def read_products(key_word=None, from_price=None, to_price=None):
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        products = json.load(f)
        if key_word:
            return [product for product in products 
                if key_word.lower().strip() in product["name"].lower()]
        if from_price and to_price:
            return [product for product in products 
                if float(from_price) <= product["price"] and product["price"] <= float(to_price)]
        return products

def read_products_by_category_id(category_id):
    return [product for product in read_products() 
        if product["category_id"] == category_id]
