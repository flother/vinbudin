# coding: UTF-8
from multifeedexporter import MultiFeedExporter


BOT_NAME = "vinbudin"
SPIDER_MODULES = ['vinbudin.spiders']
NEWSPIDER_MODULE = 'vinbudin.spiders'
USER_AGENT = u"Vínbúðin scraper (+https://github.com/flother/vinbudin)"


CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
COOKIES_ENABLED = False
DEPTH_STATS = False


ITEM_PIPELINES = {
    "vinbudin.pipelines.ProductPipeline": 100,
    "vinbudin.pipelines.StockPipeline": 200,
}


EXTENSIONS = {
    'scrapy.contrib.feedexport.FeedExporter': None,
    'multifeedexporter.MultiFeedExporter': 500,
}
MULTIFEEDEXPORTER_ITEMS = MultiFeedExporter.get_bot_items(BOT_NAME)
FEED_FORMAT = "csv"
