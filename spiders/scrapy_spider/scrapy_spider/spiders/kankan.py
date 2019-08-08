# -*- coding: utf-8 -*-
import scrapy
import time

from ..items import NewsItem


class KankanSpider(scrapy.Spider):
    name = 'kankan'
    allowed_domains = ['kankanews.com']
    start_urls = ['http://www.kankanews.com/']

    def parse(self, response):
        articles = response.xpath("//div[@class='infor']")
        for obj in articles:
            title = obj.xpath(".//h1/text()").extract_first()
            href = obj.xpath(".//a/@href").extract_first()
            content = obj.xpath(".//p/text()").extract_first()
            now = int(time.time())
            tags = []

            item = dict(
                title=title,
                content=content,
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source='kankan'
            )

            yield NewsItem(item)