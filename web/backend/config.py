import redis
import logging


class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    # session
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR
