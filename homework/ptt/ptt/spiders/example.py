# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.comhttps://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html']
    start_urls = ['http://example.comhttps://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html/']

    def parse(self, response):
        pass
