from flask import Flask
from flask_pymongo import PyMongo
from .celery import make_celery

app = Flask(__name__)

app.config.from_object('config')
mongo = app.mongo = PyMongo(app)
# /new_task /new_task/ will be handled in the same way
app.url_map.strict_slashes = False

app = Flask(__name__)

# celery setup
app.celery = celery = make_celery(app)


from executor_app import executor_app

# Register blueprint(s)
app.register_blueprint(executor_app, url_prefix='/')