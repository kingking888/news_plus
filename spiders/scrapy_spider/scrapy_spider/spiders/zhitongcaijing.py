# -*- coding: utf-8 -*-
import scrapy
import time

from ..items import NewsItem


class ZhitongcaijingSpider(scrapy.Spider):
    name = 'zhitongcaijing'
    allowed_domains = ['zhitongcaijing.com']
    start_urls = ['https://www.zhitongcaijing.com/']

    def parse(self, response):
        # 推荐 要闻 等十个栏目  除了'专栏'以外
        articles = response.xpath("//div[@class='tap-body list-a']//dd")
        for obj in articles:
            title = obj.xpath(".//h2//a/text()").extract_first()
            href = obj.xpath(".//h2//a/@href").extract_first()
            href = 'https://zhitongcaijing.com' + href
            # content 会有UnicodeError
            tags = []
            now = int(time.time())

            item = dict(
                title=title,
                content='',
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source='zhitongcaijing'
            )
            yield NewsItem(item)
