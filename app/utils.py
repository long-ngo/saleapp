import csv
import os
from datetime import datetime

from app import app, dao


def export_csv():
    products = dao.read_products()
    path = os.path.join(app.root_path, "data/products.csv")

    with open(path, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "description", "price", "images", "category_id"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    return path
