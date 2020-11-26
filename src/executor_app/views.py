from flask_restful import Resource, reqparse
from app import mongo
from bson.objectid import ObjectId

from .tasks import exec_command
from .consts import TASK_COMPLETED, TASK_CREATED, DEFAULT_TASK_BODY


class GetOutputView(Resource):
    def get(self, id):
        valid = ObjectId.is_valid(id)
        if not valid:
            return '', 404
        task = mongo.db.tasks.find_one_or_404(dict(_id=ObjectId(id)))
        return dict(output=task.get('output'), status=task.get('status'))


parser = reqparse.RequestParser()
parser.add_argument('cmd', type=str, required=True)


class NewTaskView(Resource):
    def post(self, *args, **kwargs):
        args = parser.parse_args()
        cmd = args['cmd']
        task = dict(**DEFAULT_TASK_BODY, cmd=cmd)
        inserted_id = mongo.db.tasks.insert_one(task).inserted_id
        repr_value = str(inserted_id)
        s = exec_command.delay(repr_value)
        return dict(task=repr_value)

