# default settings for scrapy
BOT_NAME = 'scrapy_numbeo_ccli'

SPIDER_MODULES = ['scrapy_numbeo_ccli.numbeo-ccli', 'scrapy_numbeo_ccli.expatistan']
NEWSPIDER_MODULE = 'scrapy_numbeo_ccli.numbeo-ccli'