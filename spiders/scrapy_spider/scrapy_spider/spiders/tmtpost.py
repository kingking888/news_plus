# -*- coding: utf-8 -*-
import time
import scrapy
from ..items import NewsItem


class TmtpostSpider(scrapy.Spider):
    name = 'tmtpost'
    allowed_domains = ['www.tmtpost.com']
    start_urls = ['https://www.tmtpost.com/']

    def parse(self, response):
        # 左侧 '推荐'
        left_objs = response.xpath("//ul[@class='article-list']//div[@class='cont']")
        for obj in left_objs:
            title = obj.xpath(".//h3//a/text()").extract_first()
            href = obj.xpath(".//h3//a/@href").extract_first()
            href = 'https://www.tmtpost.com/' + href
            now = int(time.time())

            tags = []
            div_tags = obj.xpath(".//div[@class='tag']//a")
            for tag_obj in div_tags:
                tag_name = tag_obj.xpath("./text()").extract_first()
                tag_href = tag_obj.xpath("./@href").extract_first()
                tag_dic = {
                    'tag': tag_name,
                    'tag_href': 'https://www.tmtpost.com/' + tag_href
                }
                tags.append(tag_dic)

            item = dict(
                title=title,
                content='',
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )

            yield NewsItem(item)

        # 左下 钛媒体-封面
        bottom_objs = response.xpath("//li[@class='group_part new']//li")
        for obj in bottom_objs:
            title = obj.xpath(".//h3//a[@class='title']/text()").extract_first()
            href = obj.xpath(".//h3//a[@class='title']/@href").extract_first()
            href = 'https://www.tmtpost.com/' + href
            now = int(time.time())

            tags = [
                {
                    'tag': '钛媒体·封面',
                    'tag_href': 'https://www.tmtpost.com/tag/3853985'
                }
            ]

            item = dict(
                title=title,
                content='',
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )
            yield NewsItem(item)

        # 右侧 瞬眼天下
        right_objs = response.xpath("//a[@class='text']")
        for obj in right_objs:
            title = obj.xpath("./text()").extract_first()
            href = obj.xpath("./@href").extract_first()
            href = 'https://www.tmtpost.com/' + href
            now = int(time.time())
            # 标签: 瞬眼天下 https://www.tmtpost.com/nictation
            tags = [
                {
                    'tag': '瞬眼天下',
                    'tag_href': 'https://www.tmtpost.com/nictation'
                }
            ]

            item = dict(
                title=title,
                content='',
                href=href,
                tags=tags,
                ts_origin=now,
                ts_crawl=now,
                source=self.name
            )
            yield NewsItem(item)
