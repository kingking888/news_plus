from flask_pymongo import PyMongo
from flask_restful import Resource, reqparse
from flask import current_app

parser = reqparse.RequestParser()
parser.add_argument('category', action='append')
parser.add_argument('skip', type=int)


class NewsFlowList(Resource):
    """
        新闻列表
        /api/newsflow
    """

    def get(self):
        # 获取参数
        args = parser.parse_args()
        categories = args['category']
        skip = args['skip']
        # 初始化mongo
        mongo = PyMongo(current_app)
        collection = mongo.db.scrapy
        if not categories:
            # 全不选
            return []

        query = {'source': {'$in': categories}}
        projection = {'_id': 0}
        sort = [('ts_crawl', -1)]
        cursor = collection.find(query, projection).skip(skip).sort(sort).limit(20)
        cursor_li = list(cursor)

        return cursor_li
