import scrapy


class Product(scrapy.Item):

    id = scrapy.Field()
    name = scrapy.Field()
    supplier = scrapy.Field()
    country_of_origin = scrapy.Field()
    district_of_origin = scrapy.Field()
    place_of_origin = scrapy.Field()
    year = scrapy.Field()
    alcohol_volume = scrapy.Field()
    grape = scrapy.Field()
    taste_group = scrapy.Field()
    is_organic = scrapy.Field()
    bottled_volume = scrapy.Field()
    seal = scrapy.Field()
    container = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    goes_with = scrapy.Field()
    price = scrapy.Field()
    is_temp_sale = scrapy.Field()
    is_special_order = scrapy.Field()
    is_special_reserve = scrapy.Field()
    date_on_market = scrapy.Field()
    is_available = scrapy.Field()
    is_gift = scrapy.Field()
    type = scrapy.Field()


class Stock(scrapy.Item):

    product_id = scrapy.Field()
    region = scrapy.Field()
    store = scrapy.Field()
    quantity = scrapy.Field()
    type = scrapy.Field()
