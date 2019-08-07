import sys
import logging

sys.path.append('../../../../')

from flask import current_app, request
from flask_restful import Resource, reqparse
from spiders.selenium_spider import bloomberg

parser = reqparse.RequestParser()
parser.add_argument('spider')
parser.add_argument('action')


def test():
    print('testing')


def run_bloomberg():
    spider = bloomberg.Bloomberg()
    spider.run()


spider_list = ['run_bloomberg', ]
action_list = ['start', 'pause', 'resume']


class CustomScheduler(Resource):
    """
    http://127.0.0.1:5000/api/scheduler?spider=run_bloomberg&action=start
    http://127.0.0.1:5000/api/scheduler?spider=run_bloomberg&action=pause
    http://127.0.0.1:5000/api/scheduler?spider=run_bloomberg&action=resume
    """

    def get(self):
        args = parser.parse_args()
        spider = args['spider']
        action = args['action']

        if not spider or not action:
            error_msg = {'error': '没有指定爬虫或者操作'}
            print(error_msg)
            return error_msg

        if spider not in spider_list or action not in action_list:
            error_msg = {'error': '错误的爬虫或者操作'}
            print(error_msg)
            return error_msg

        print(spider, action)
        if action == 'start':
            try:
                result = current_app.apscheduler.add_job(func=eval(spider), id=spider, args='',
                                                         trigger='interval',
                                                         minutes=1)
                logging.info(result)
            except Exception as err:
                logging.error(err)

        elif action == 'pause':
            try:
                result = current_app.apscheduler.pause_job(spider)
                logging.info(result)
            except Exception as err:
                logging.error(err)

        elif action == 'resume':
            try:
                result = current_app.apscheduler.resume_job(spider)
                logging.info(result)
            except Exception as err:
                logging.error(err)

        return {'status': 200}
