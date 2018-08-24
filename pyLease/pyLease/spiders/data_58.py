# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as Sle
from pyLease.pyLease.utils.log_handle import init_logging

logger = init_logging()


class Data58Spider(CrawlSpider):
    name = 'data_58'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    rules = (
        Rule(Sle(allow=(r'/zufang/\d.*\w\.shtml?.*')), callback="hanles_parse"),
    )

    def handles_parse(self, response):
        Item = []
        response_body = Selector(response=response)
