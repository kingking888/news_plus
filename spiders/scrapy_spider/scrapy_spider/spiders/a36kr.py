# -*- coding: utf-8 -*-
import time
import scrapy
from ..items import NewsItem


class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['36kr.com']
    start_urls = ['https://36kr.com/newsflashes']

    def parse(self, response):
        data_list = response.xpath("//div[@class='newsflash-item']")
        for data in data_list:
            title = data.xpath(".//a[@class='item-title']/text()").extract_first()
            content = data.xpath(".//div[@class='item-desc']/text()").extract_first()
            href = data.xpath(".//a[@class='item-title']/@href").extract_first()
            # 拼接href
            href = 'https://36kr.com/newsflashes' + href
            print(title, content, href)

            now = int(time.time())

            item = dict(
                title=title,
                content=content,
                href=href,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )

            yield NewsItem(item)