# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PyleaseItem(scrapy.Item):
    """
    Item Field Defined
    """
    # WEB Field
    web_title = scrapy.Field()  # '页面主题'
    web_public_time = scrapy.Field()  # '发布时间'
    web_visit = scrapy.Field()  # '网页浏览量'
    web_publisher = scrapy.Field()  # '发布者'
    identify_info = scrapy.Field()  # '认证信息'
    company_info = scrapy.Field()  # '企业(或个人)信息'
    web_pub_type = scrapy.Field()  # '发布来源：0为未知，1为个人房源，2为经纪人房源'
    house_desc = scrapy.Field()  # '房源描述'

    # HOUSE Field
    house_size = scrapy.Field()  # '房屋面积：单位平方米'
    leasehold = scrapy.Field()  # '租赁方式：1为整租，2为合租'
    bedroom_count = scrapy.Field()  # '卧室数量'
    living_room_count = scrapy.Field()  # '客厅数量'
    toilet_count = scrapy.Field()  # '卫生间数量'
    province = scrapy.Field()  # '位置：省'
    city = scrapy.Field()  # '位置：市'
    house_estate = scrapy.Field()  # '小区'
    address = scrapy.Field()  # '详细地址'

    # facility
    facility = scrapy.Field()  # '房屋配套设施'

    # bright spot
    bright_spot = scrapy.Field()  # '房屋亮点'
