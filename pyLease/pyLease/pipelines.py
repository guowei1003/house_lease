# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pyLease.pyLease.utils.db import connect
from pyLease.pyLease.utils.log_handle import init_logging

logger = init_logging()


class PyleasePipeline(object):

    def __init__(self):
        self.db = connect()

    def process_item(self, item, spider):

        return item
