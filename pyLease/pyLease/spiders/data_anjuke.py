# -*- coding: utf-8 -*-
import scrapy


class DataAnjukeSpider(scrapy.Spider):
    name = 'data_anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
