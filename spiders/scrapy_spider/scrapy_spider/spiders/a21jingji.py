# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import NewsItem


class A21jingjiSpider(scrapy.Spider):
    name = '21jingji'
    allowed_domains = ['www.21jingji.com']
    start_urls = ['http://www.21jingji.com/']

    def parse(self, response):
        data_list = response.xpath("//div[@id='data_list']//div[@class='li']")
        for data in data_list:
            title = data.xpath(".//a[@class='listTit']/text()").extract_first()
            content = data.xpath(".//p[@class='listCont']/a/text()").extract_first()
            href = data.xpath(".//a[@class='listTit']/@href").extract_first()
            # 21经济没有发布时间, 用采集时间
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
