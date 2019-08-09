# -*- coding: utf-8 -*-
import scrapy
import time
import logging

from ..items import NewsItem


class StdailySpider(scrapy.Spider):
    name = 'stdaily'
    allowed_domains = ['stdaily.com']
    start_urls = ['http://www.stdaily.com/index/kejixinwen/kejixinwen.shtml']

    def parse(self, response):
        articles = response.xpath("//div[@class='f_lieb_list']//dl")

        for obj in articles:
            try:
                title = obj.xpath(".//h3//a/text()").extract_first()
                href = obj.xpath(".//h3//a/@href").extract_first()
                href = 'http://www.stdaily.com' + href
                content = obj.xpath(".//p/text()").extract_first()
                content = content.strip()
                now = int(time.time())
                tags = []

                item = dict(
                    title=title,
                    content=content,
                    href=href,
                    tags=tags,
                    ts_origin=now,
                    ta_crawl=now,
                    source='stdaily'
                )
                yield NewsItem(item)

            except UnicodeEncodeError as err:
                logging.error(err)
                continue
