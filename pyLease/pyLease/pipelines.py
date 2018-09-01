# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utils.db import connect


class PyleasePipeline(object):

    def __init__(self):
        self.db = connect()

    def process_item(self, item, spider):

        return item
