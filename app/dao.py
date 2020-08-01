from app import app
import json
import os

def read_products():
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        return json.load(f)
