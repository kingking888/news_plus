# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from pymongo import MongoClient
from scrapy.exceptions import DropItem

from . import settings


class ScrapySpiderPipeline(object):
    def __init__(self, databseIp='127.0.0.1', databasePort=27017, mongodbName='test'):
        client = MongoClient(databseIp, databasePort)
        self.db = client[mongodbName]

    def process_item(self, item, spider):
        self.db.scrapy.insert(dict(item))
        return item


class DuplicatePipeline(object):
    """
    利用redis去重
    """
    # 初始化redis
    redis_db = redis.Redis(host='127.0.0.1', port=6379, db=4)
    redis_data_dict = 'jump_url'
    # 初始化mongo
    client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
    db = client[settings.MONGO_DBNAME]
    collection = db['scrapy']

    def __init__(self):
        self.redis_db.flushdb()
        if self.redis_db.hlen(self.redis_data_dict) == 0:
            db_docs = self.collection.find({}, {'href': 1, '_id': 0}).limit(20000)
            for obj in db_docs:
                print(obj)
                href = obj['href']
                print(href)
                self.redis_db.hset(self.redis_data_dict, href, 0)

    def process_item(self, item, spider):
        if self.redis_db.hexists(self.redis_data_dict, item['href']):
            raise DropItem('Duplicate item found: %s' % item)

        self.collection.insert_one(dict(item))
        return item
