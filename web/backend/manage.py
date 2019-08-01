from flask import render_template, jsonify
from flask_script import Manager
from news import create_app
from flask_restful import Api

from news.apps.newsflow import NewsFlowList

# 环境切换 dev/prod
app = create_app('dev')
# Restful API
api = Api(app)
# Flask-script
manager = Manager(app)


# 总入口
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


# 路由
api.add_resource(NewsFlowList, '/api/newsflow')

if __name__ == '__main__':
    manager.run()
