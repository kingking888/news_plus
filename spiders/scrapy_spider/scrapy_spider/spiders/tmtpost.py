# -*- coding: utf-8 -*-
import time
import scrapy
from ..items import NewsItem

class TmtpostSpider(scrapy.Spider):
    name = 'tmtpost'
    allowed_domains = ['www.tmtpost.com']
    start_urls = ['https://www.tmtpost.com/']

    def parse(self, response):
        # 左侧'推荐'  下面的'钛媒体-封面'
        left_objs = response.xpath("//a[@class='title']")
        for obj in left_objs:
            title = obj.xpath("./text()").extract_first()
            href = obj.xpath("./@href").extract_first()
            href = 'https://www.tmtpost.com/' + href

            now = int(time.time())

            item = dict(
                title=title,
                content='',
                href=href,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )

            yield NewsItem(item)

        # 右侧瞬眼天下
        right_objs = response.xpath("//a[@class='text']")
        for obj in right_objs:
            title = obj.xpath("./text()").extract_first()
            href = obj.xpath("./@href").extract_first()
            href = 'https://www.tmtpost.com/' + href

            now = int(time.time())

            item = dict(
                title=title,
                content='',
                href=href,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )
            yield NewsItem(item)
