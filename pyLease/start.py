# coding:utf-8
# 启动脚本
# 针对58同城
# 时间：2018年8月30日15点55分

from scrapy import cmdline

cmdline.execute("scrapy crawl data_58".split())
