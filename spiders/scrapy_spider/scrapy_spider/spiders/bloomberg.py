# -*- coding: utf-8 -*-
import scrapy


class BloombergSpider(scrapy.Spider):
    name = 'bloomberg'
    allowed_domains = ['bloomberg.com']
    start_urls = ['http://bloomberg.com']

    def parse(self, response):
        print(response)
        articles = response.xpath("//article")
        print(articles)
        for article in articles:
            title = article.xpath("./h3/a/text()").extract_first()

            print(title)
