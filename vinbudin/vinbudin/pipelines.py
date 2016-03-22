# coding: UTF-8
import datetime


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
        return item


class StockPipeline(object):

    def process_item(self, item, spider):
        if item["type"] == "stock":
            item["product_id"] = int(item["product_id"])
            item["quantity"] = int(item["quantity"])
        return item
