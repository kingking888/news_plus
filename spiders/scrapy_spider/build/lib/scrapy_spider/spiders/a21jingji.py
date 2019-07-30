# -*- coding: utf-8 -*-
import scrapy


class A21jingjiSpider(scrapy.Spider):
    name = '21jingji'
    allowed_domains = ['www.21jingji.com']
    start_urls = ['http://www.21jingji.com/']

    def parse(self, response):
        data_list = response.xpath("//div[@id='data_list']//div[@class='li']")
        for data in data_list:
            title = data.xpath(".//a[@class='listTit']/text()").extract_first()
            print(title)
            content = data.xpath(".//p[@class='listCont']/a/text()").extract_first()
            print(content)
            href = data.xpath(".//a[@class='listTit']/@href").extract_first()
            print(href)


