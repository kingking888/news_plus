# -*- coding: utf-8 -*-
import time
import scrapy

from ..items import NewsItem


class M21caijingSpider(scrapy.Spider):
    name = 'm21caijing'
    allowed_domains = ['m.21jingji.com']
    start_urls = ['https://m.21jingji.com/']

    def parse(self, response):
        articles = response.xpath("//div[@class='news_list']//a")
        for obj in articles:
            title = obj.xpath(".//div[@class='news_title']/text()").extract_first()
            href = obj.xpath("./@href").extract_first()
            now = int(time.time())
            tags = []

            item = dict(
                title=title,
                content='',
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source='m21caijing'
            )
            yield NewsItem(item)
