import redis

from settings import *
from pymongo import MongoClient


def init_mongo():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DBNAME]
    db.authenticate(name=MONGO_USER, password=MONGO_PWD)
    collection = db[MONGO_COLLECTION]

    return collection


def init_redis():
    redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    return redis_db
