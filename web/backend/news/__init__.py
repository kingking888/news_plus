import logging
import redis

from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import DevConfig, ProdConfig
from flask_pymongo import PyMongo
from flask_cors import CORS

config = {
    "dev": DevConfig,
    "prod": ProdConfig
}

redis_store = None


def setup_log(config_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    # 配置项目日志
    setup_log(config_name)
    app = Flask(
        __name__,
        static_folder="./../../dist/static",
        template_folder="./../../dist"
    )
    # 配置 生产环境和开发环境切换
    app.config.from_object(config[config_name])
    # 配置数据库 MongoDB
    app.config.update(
        MONGO_URI='mongodb://remote:remote@139.196.102.128:27017/news_plus',
        # MONGO_USERNAME='remote',
        # MONGO_PASSWORD='remote',
    )
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)
    # CORS跨域
    # cors = CORS(app, resources={r"/api/*": {"origin": "*"}})
    CORS(app)

    return app
