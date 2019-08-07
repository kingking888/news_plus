import logging
import time
from init_db import init_mongo, init_redis
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# logging.basicConfig(filename='log.txt',
#                     format='[%(levelname)s]%(asctime)s -%(name)s-%(module)s[line:%(lineno)d]:%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=logging.INFO)


class Bloomberg():
    def __init__(self):
        self.start_url = 'https://www.bloomberg.com/asia'
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(30)
        self.collection = init_mongo()
        self.redis_db = init_redis()

    def get_content_list(self):
        """
        提取页面内容, 生成列表
        :return:
        """
        res_list = []
        try:
            title_list = []
            href_list = []

            titles = self.driver.find_elements_by_xpath("//article/h3/a")
            for title in titles:
                title_str = title.text
                href = title.get_attribute('href')

                title_list.append(title_str)
                href_list.append(href)

            # 遍历结果列表， 拼接字典
            mid = map(list, zip(title_list, href_list))
            for item in mid:
                new_dic = dict(zip(['title', 'href'], item))
                res_list.append(new_dic)
        except Exception as err:
            logging.error(err)

        return res_list

    def duplicate_filter(self, res_list):
        """利用redis去重"""
        redis_data_dict = 'jump_url'
        self.redis_db.flushdb()
        if self.redis_db.hlen(redis_data_dict) == 0:
            db_docs = self.collection.find({'source': 'bloomberg'}, {'href': 1, '_id': 0}).limit(20000)
            for obj in db_docs:
                href = obj['href']
                self.redis_db.hset(redis_data_dict, href, 0)

        for data in res_list[:]:
            if self.redis_db.hexists(redis_data_dict, data['href']):
                res_list.remove(data)
                logging.info('Duplicate item found: %s' % data)

        return res_list

    def write_db(self, filtered_list):
        try:
            for data in filtered_list:
                href = data['href']
                title = data['title']
                now = int(time.time())

                item = dict(
                    title=title,
                    content='',
                    href=href,
                    ts_origin=now,
                    ts_crawl=now,
                    source='bloomberg'
                )

                self.collection.insert_one(item)
                logging.info('已插入一条数据 %s' % item)
        except Exception as err:
            logging.error(err)

    def run(self):
        try:
            self.driver.get(self.start_url)
        except TimeoutException:
            print('Time out after 30 seconds when loading page.')
            self.driver.execute_script('window.stop()')

        try:
            res_list = self.get_content_list()
            filtered_list = self.duplicate_filter(res_list)
            self.write_db(filtered_list)
        except Exception as err:
            logging.error(err)
        self.driver.quit()


