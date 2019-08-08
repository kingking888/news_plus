# -*- coding: utf-8 -*-
import scrapy
import time

from ..items import NewsItem


class ThepaperSpider(scrapy.Spider):
    name = 'thepaper'
    allowed_domains = ['thepaper.cn']
    start_urls = ['https://www.thepaper.cn/']

    def parse(self, response):
        articles = response.xpath("//div[@class='newsbox listview']//div[starts-with(@id, 'cont')]")

        for obj in articles:
            title = obj.xpath(".//h2//a/text()").extract_first()
            href = obj.xpath(".//h2//a/@href").extract_first()
            href = 'https://www.thepaper.cn/' + href
            content = obj.xpath(".//p/text()").extract_first()

            tag_name = obj.xpath(".//div[@class='pdtt_trbs']//a/text()").extract_first()
            tag_href = obj.xpath(".//div[@class='pdtt_trbs']//a/@href").extract_first()
            tag_href = 'https://www.thepaper.cn/' + tag_href
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
                source='thepaper'
            )

            yield NewsItem(item)
