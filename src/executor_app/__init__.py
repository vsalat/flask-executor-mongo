from flask import Blueprint
from flask_restful import Api

from .views import GetOutputView, NewTaskView


executor_app = Blueprint('executor_app', __name__)
api = Api(executor_app)
api.add_resource(GetOutputView, '/get_output/<id>')
api.add_resource(NewTaskView, '/new_task')
