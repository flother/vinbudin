# coding: UTF-8
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
