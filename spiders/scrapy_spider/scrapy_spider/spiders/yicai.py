# -*- coding: utf-8 -*-
import scrapy
import logging
import time

from ..items import NewsItem


class YicaiSpider(scrapy.Spider):
    name = 'yicai'
    allowed_domains = ['yicai.com']
    start_urls = ['https://www.yicai.com/']

    def parse(self, response):
        # articles = response.xpath("//div[@class='m-con']//div[starts-with(@class, 'm-list')]")
        articles = response.xpath("//div[@class='m-con']//a")
        for obj in articles:
            try:
                title = obj.xpath(".//h2/text()").extract_first()
                content = obj.xpath(".//p/text()").extract_first()
                href = obj.xpath("./@href").extract_first()
                href = 'https://www.yicai.com' + href
                now = int(time.time())
                tags = []

                item = dict(
                    title=title,
                    content=content,
                    href=href,
                    tags=tags,
                    ts_origin=now,
                    ts_crawl=now,
                    source='yicai'
                )

                yield NewsItem(item)

            except UnicodeEncodeError as err:
                logging.error(err)
                continue
