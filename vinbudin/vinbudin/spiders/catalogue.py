# coding: UTF-8
import json

import scrapy

from vinbudin.items import Product, Stock


class CatalogueSpider(scrapy.Spider):

    name = "catalogue"
    allowed_domains = ["vinbudin.is"]

    def start_requests(self):
        yield scrapy.Request("http://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/DoSearch?skip=0&count=10000&orderBy=random",
                             self.parse_products,
                             headers={"Content-Type": "application/json"})

    def parse_products(self, response):
        catalogue = json.loads(response.body_as_unicode())
        products = json.loads(catalogue["d"])["data"]
        for product in products:
            item = Product()
            item["id"] = product["ProductID"]
            item["name"] = product["ProductName"]
            item["country_of_origin"] = product["ProductCountryOfOrigin"]
            item["district_of_origin"] = product["ProductDistrictOfOrigin"]
            item["place_of_origin"] = product["ProductPlaceOfOrigin"]
            item["year"] = product["ProductYear"]
            item["alcohol_volume"] = product["ProductAlchoholVolume"]
            item["grape"] = product["ProductWine"]
            item["taste_group"] = product["ProductTasteGroup"]
            item["is_organic"] = str(product["ProductOrganic"]).lower()
            item["bottled_volume"] = product["ProductBottledVolume"]
            item["seal"] = product["ProductPackagingClosing"]
            item["container"] = product["ProductContainerType"]
            item["category"] = product["ProductCategory"]["name"]
            try:
                item["sub_category"] = product["ProductSubCategory"]["name"]
            except TypeError:
                item["sub_category"] = ""
            item["goes_with"] = product["ProductFoodCategories"]
            item["price"] = product["ProductPrice"]
            item["is_temp_sale"] = str(product["ProductIsTemporaryOnSale"]).lower()
            item["is_special_order"] = str(product["ProductIsSpecialOrder"]).lower()
            item["is_special_reserve"] = str(product["ProductSpecialReserve"]).lower()
            item["date_on_market"] = product["ProductDateOnMarket"]
            item["is_available"] = str(product["ProductIsAvailableInStores"]).lower()
            item["is_gift"] = str(product["ProductIsGift"]).lower()
            item["type"] = "product"
            yield scrapy.Request("http://www.vinbudin.is/Heim/vörur/stoek-vara.aspx/?productid={:05}".format(item["id"]),
                                 self.parse_stock,
                                 meta={"product": item})

    def parse_stock(self, response):
        product = response.meta["product"]
        product["supplier"] = response.xpath("//span[@id='ctl01_ctl00_Label_ProductSeller']//text()").extract_first()
        yield product

        for table in response.css("table.tableStockStatus"):
            rows = table.css("tr")
            region = rows[0].css("th::text").extract_first()
            for store in rows[1:]:
                item = Stock()
                item["product_id"] = product["id"]
                item["region"] = region
                store_name, quantity = store.css("td::text").extract()[:2]
                item["store"] = store_name
                item["quantity"] = quantity
                item["type"] = "stock"
                yield item
