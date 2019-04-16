# -*- coding: utf-8 -*-
import scrapy


class HahaSpider(scrapy.Spider):
    name = 'haha'
    allowed_domains = ['www']
    start_urls = ['http://www/']

    def parse(self, response):
        pass
