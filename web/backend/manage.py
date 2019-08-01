from random import randint
from flask import render_template
from config import Config
from flask_script import Manager
from news import create_app

# 环境切换 dev/prod
app = create_app('dev')
# Flask-script
manager = Manager(app)


# @app.route('/api/random')
# def random_number():
#     response = {
#         'randomNumber': randint(1, 100)
#     }
#
#     return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


app.config.from_object(Config)

if __name__ == '__main__':
    manager.run()
