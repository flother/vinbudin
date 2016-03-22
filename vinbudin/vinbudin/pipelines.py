# coding: UTF-8
import datetime

from csvkit.unicsv import UnicodeCSVWriter


class ProductPipeline(object):

    CONTAINERS = {
        "DS.": u"dós",
        "FL.": "flaska",
        u"KÚT.": u"kútur",
        "PET": "peli",
        "PK.": "pakki",
        "PKN": "pakkning",
        "STK.": "stykki",
    }
    SEALS = {
        "FLEXTAP": "flextappi",
        "PLAST": "plasttappi",
        "T-PLAST": "plasttappi",
        "TKORKUR": "korktappi",
        "SKRUF": u"skrúftappi",
        "HIMNUKORKU": "korktappi",
        "SK-SK": u"skrúftappi",
        "F-KORKUR": "korkur",
        "STKORK": "korkur",
        "STKORK-D": "korkur",
        "VITOP": "Vitop",
    }
    GOES_WITH = {
        "1": u"saltfiskur",  # Saltfish, ~20 records
        "2": u"pylsur",  # Sausages, ~80 records
        "3": u"pítsa",  # Pizza, ~80 records
        "4": u"sushi",  # Sushi, ~100 records
        "A": u"fordrykkir og smáréttir",  # Aperitifs/appetizers, ~320 records
        "B": u"skelfiskur",  # Shellfish, ~280 records
        "C": u"fiskur",  # Fish, ~430 records
        "D": u"alifuglar",  # Poultry, ~440 records
        "E": u"nautakjöt",  # Beef, ~330 records
        "F": u"lambakjöt",  # Lamb, ~410 records
        "G": u"svínakjöt",  # Pork, ~320 records
        "H": u"kröftugri villibráð",  # Strong game, ~180 records
        "I": u"grænmetisréttir",  # Vegetarian, ~220 records
        "J": u"grillað kjöt",  # Grilled meat, ~310 records
        "K": u"austurlenskur matur",  # Asian food, ~90 records
        "L": u"ostar",  # Cheese, ~250 records
        "M": u"pastaréttir",  # Pasta, ~310 records
        "N": u"ábætisréttir",  # Dessert wines, ~50 records
        "O": u"sólpallavín",  # Wines on the sundeck, ~20 records
        "P": u"smáréttir",  # Hors-d'oeuvres, ~540 records
        "R": u"reykt kjöt",  # Smoked meats, ~60 records
        "S": u"pottréttir",  # Casseroles, ~160 records
        "T": u"léttari villibráð",  # "Lighter" game, ~190 records
        "V": u"sterkkryddaður matur",  # Spicy foods, ~20 records
        "W": u"eitt og sér",  # Wine to serve on their own, ~10 records
        # "Y": "",  # ?, ~1110 records
        # u"Æ": "",  # ?, ~220 records
    }

    def __init__(self):
        self.products = []

    def close_spider(self, spider):
        with open("../data/products.csv", "wb") as fh:
            csv = UnicodeCSVWriter(fh)
            csv.writerow([
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
                "price",
                "is_temp_sale",
                "is_special_order",
                "is_special_reserve",
                "date_on_market",
                "is_available",
                "is_gift",
            ])
            csv.writerows(sorted(self.products, key=lambda i: i[0]))

    def process_item(self, item, spider):
        if item["type"] == "product":
            item["price"] = int(item["price"])
            item["date_on_market"] = datetime.datetime.strptime(
                item["date_on_market"], "%Y-%m-%dT00:00:00").date()
            item["container"] = self.CONTAINERS.get(item["container"],
                                                    item["container"].lower())
            item["seal"] = self.SEALS.get(item["seal"], item["seal"].lower())
            # Use full descriptions for the "goes_with" fields.
            # item["goes_with"] = "{" + ", ".join([
            #     self.GOES_WITH.get(item["goes_with"],
            #                        item["goes_with"])]) + "}"
            # Use abbreviated terms for "goes_with" field.
            item["goes_with"] = "{" + ",".join(item["goes_with"]) + "}"
            # Convert boolean values to "true" or "false".
            item["is_organic"] = str(item["is_organic"]).lower()
            item["is_temp_sale"] = str(item["is_temp_sale"]).lower()
            item["is_special_order"] = str(item["is_special_order"]).lower()
            item["is_special_reserve"] = str(item["is_special_reserve"]).lower()
            item["is_available"] = str(item["is_available"]).lower()
            item["is_gift"] = str(item["is_gift"]).lower()

            self.products.append([
                item["id"],
                item["name"],
                item["supplier"],
                item["country_of_origin"],
                item["district_of_origin"],
                item["place_of_origin"],
                item["year"],
                item["alcohol_volume"],
                item["grape"],
                item["taste_group"],
                item["is_organic"],
                item["bottled_volume"],
                item["seal"],
                item["container"],
                item["category"],
                item["sub_category"],
                item["goes_with"],
                item["price"],
                item["is_temp_sale"],
                item["is_special_order"],
                item["is_special_reserve"],
                item["date_on_market"],
                item["is_available"],
                item["is_gift"],
            ])
        return item


class StockPipeline(object):

    def __init__(self):
        self.stock = []

    def close_spider(self, spider):
        with open("../data/stock.csv", "wb") as fh:
            csv = UnicodeCSVWriter(fh)
            csv.writerow([
                "product_id",
                "region",
                "store",
                "quantity",
            ])
            csv.writerows(sorted(self.stock, key=lambda i: i[:3]))

    def process_item(self, item, spider):
        if item["type"] == "stock":
            self.stock.append([
                item["product_id"],
                item["region"],
                item["store"],
                item["quantity"],
            ])
        return item
