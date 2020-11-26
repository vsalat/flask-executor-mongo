import os

DEBUG = bool(os.environ.get("DEBUG", False))

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY", "secret")

SECRET_KEY = os.environ.get("SECRET_KEY", "secret")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/myDatabase")
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                   'redis://localhost:6379/4')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND',
                                       'redis://localhost:6379/4')