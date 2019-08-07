# -*- coding: utf-8 -*-
import scrapy
import time

from ..items import NewsItem


class DoitSpider(scrapy.Spider):
    name = 'doit'
    allowed_domains = ['doit.com.cn']
    start_urls = ['https://www.doit.com.cn/']

    def parse(self, response):
        # 首页 最新文章
        articles = response.xpath("//article")
        for obj in articles:
            title = obj.xpath(".//header//h2//a/text()").extract_first()
            href = obj.xpath(".//header//h2//a/@href").extract_first()
            content = obj.xpath(".//p[@class='note']/text()").extract_first()
            tag_name = obj.xpath(".//header/a/text()").extract_first()
            tag_href = obj.xpath(".//header/a/@href").extract_first()
            now = int(time.time())
            tags = [
                {
                    'tag': tag_name,
                    'tag_href': tag_href
                }
            ]

            item = dict(
                title=title,
                content=content,
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source='doit'
            )

            yield NewsItem(item)



