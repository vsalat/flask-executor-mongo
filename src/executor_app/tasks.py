import os
from bson.objectid import ObjectId

from app import celery, mongo


@celery.task()
def exec_command(id):
    object_id = ObjectId(id)
    task = mongo.db.tasks.find_one_or_404(dict(_id=object_id))
    execution = os.system(task['cmd'])
    output = execution.read()
    mongo.db.tasks.update_one(
        {'_id': object_id},
        {"$set": dict(output=output)},
        upsert=False)
