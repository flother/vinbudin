"""
Downloads data scraped by the catalogue spider and stored on Amazon S3,
saves it to local files, and adds, commits, and pushes those files to the
GitHub remote.
"""
import io
import os

from boto.s3.connection import S3Connection
from csvkit.unicsv import UnicodeCSVDictReader, UnicodeCSVWriter
from git import Repo


PRODUCT_FIELDS = (
    "id",
    "name",
    "supplier",
    "country_of_origin",
    "district_of_origin",
    "place_of_origin",
    "year",
    "alcohol_volume",
    "grape",
    "taste_group",
    "is_organic",
    "bottled_volume",
    "seal",
    "container",
    "category",
    "sub_category",
    "goes_with",
    "price",
    "is_temp_sale",
    "is_special_order",
    "is_special_reserve",
    "date_on_market",
    "is_available",
    "is_gift",
)
STOCK_FIELDS = (
    "product_id",
    "region",
    "store",
    "quantity",
)


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    products_filename = os.path.join(repo_root, "data/products.csv")
    stock_filename = os.path.join(repo_root, "data/stock.csv")

    print "Connecting to S3 bucket."
    conn = S3Connection()
    bucket = conn.get_bucket("flother")

    print "Cleaning products."
    products = bucket.get_key("vinbudin/data/Product.csv", validate=False)
    product_rows = UnicodeCSVDictReader(io.BytesIO(products.read()))
    with open(products_filename, "wb") as fh:
        products_output = UnicodeCSVWriter(fh, lineterminator="\n")
        products_output.writerow(PRODUCT_FIELDS)
        for row in sorted(product_rows, key=lambda r: r["id"]):
            products_output.writerow([row[key] for key in PRODUCT_FIELDS])

    print "Cleaning stock."
    stock = bucket.get_key("vinbudin/data/Stock.csv", validate=False)
    stock_rows = UnicodeCSVDictReader(io.BytesIO(stock.read()))
    with open(stock_filename, "wb") as fh:
        stock_output = UnicodeCSVWriter(fh, lineterminator="\n")
        stock_output.writerow(STOCK_FIELDS)
        for row in sorted(stock_rows, key=lambda r: (int(r["product_id"]),
                                                     r["store"])):
            stock_output.writerow([row[key] for key in STOCK_FIELDS])

    conn.close()
    print "Finished downloading from S3."

    repo = Repo(repo_root)
    repo.git.reset()
    if repo.is_dirty():
        print "Changes to commit."
        repo.index.add([products_filename, stock_filename])
        repo.index.commit("Add latest inventory data")
        print "Committed locally."
        repo.remotes.origin.pull()
        print "Pulled from origin."
        repo.remotes.origin.push()
        print "Pushed to origin."
    else:
        print "No changes to commit."


if __name__ == "__main__":
    main()
