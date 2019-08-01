from flask_pymongo import PyMongo
from flask_restful import Resource, reqparse
from flask import current_app

parser = reqparse.RequestParser()
parser.add_argument('category', action='append')



class NewsFlowList(Resource):
    """
        新闻列表
        /api/newsflow
    """
    def get(self):
        # 获取类别参数
        args = parser.parse_args()
        categories = args['category']
        print(categories)
        # 初始化mongo
        mongo = PyMongo(current_app)
        collection = mongo.db.scrapy
        if not categories:
            # 全不选
            return []

        query = {'source': {'$in': categories}}
        projection = {'_id': 0}
        sort = [('ts_crawl', -1)]
        cursor = collection.find(query, projection).sort(sort).limit(20)
        cursor_li = list(cursor)
        print(cursor_li)


        response = {'status': 200}
        return cursor_li
