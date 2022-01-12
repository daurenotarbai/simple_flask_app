from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from task_manager_api.extensions import db
from task_manager_api.commons.pagination import paginate
from task_manager_api.models.mdl_tasks import TblTasks
from task_manager_api.api.schemas.sch_tasks import TblTasksSchema
import redis
from task_manager_api.api.helpers import UUIDEncoder
# from uuid import UUID


class TblTasksResource(Resource):
    # method_decorators = [jwt_required]

    def get(self):
        schema = TblTasksSchema(many=True)
        task_id = request.args.get('task_id', None)
        if task_id is not None:
            query = TblTasks.query.filter_by(task_id=task_id)
        else:
            query = TblTasks.query
        return schema.dump(query)

    def post(self):
        data = request.json
        schema = TblTasksSchema(partial=True)
        data_object = schema.load(data, )
        added_object = schema.dump(data_object)
        db.session.add(data_object)
        db.session.commit()
        return added_object, 201

    def put(self):
        task_id = request.args.get("task_id")
        print("Task_id",task_id)
        if task_id:
            schema = TblTasksSchema(partial=True)
            task = TblTasks.query.get_or_404(task_id)
            task = schema.load(request.json, instance=task)
            db.session.commit()
            return {"msg": "task info updated", "task": schema.dump(task)}
        else:
            return {"msg": "task_id required"}, 400

    def delete(self):
        task_id = request.args.get("task_id")
        if task_id:
            task = TblTasks.query.get_or_404(task_id)
            db.session.delete(task)
            db.session.commit()
            return {"msg": "task deleted"}
        else:
            return {"msg": "task_id required"}, 400

from time import sleep
import datetime
import random
from pprint import pprint
import json
class TestRedisResource(Resource):
    # method_decorators = [jwt_required]

    def get(self):
        # client = redis.Redis(host='127.0.0.1', port=6379)
        task_id = request.args.get('task_id', None)
        if task_id:
            query = TblTasks.query.filter_by(task_id=task_id)
        else:
            query = TblTasks.query

        queryset = []
        dd = {}
        for task in query:
            q = {}

            q["task_id"] = task.task_id
            q["task_title"] = task.task_title
            q["task_description"] = task.task_description
            result_json = json.dumps(q, cls=UUIDEncoder)
            result_data = json.loads(result_json)
            dd['task_id:{}'.format(str(task.task_id))] = result_data
        hats = dd
        client = redis.Redis(db=4, host='127.0.0.1', port=6379)
        with client.pipeline() as pipe:
            for h_id, hat_id in hats.items():
                pipe.hmset(h_id, hat_id)
            pipe.execute()
        client.bgsave()
        print(client.keys())
        pprint(client.hgetall("task_id:dc328d26-f07f-4e5f-b46f-0dbe6629a6bd"))

##Test1
        # client.set('Language', "Python")
        # print((client.get('Language')))
##Test2
        # client.lpush("LanguageList", "Kotlin")
        # client.lpush("LanguageList", "Python")
        # while (client.llen('LanguageList') != 0):
        #     print(client.lpop('LanguageList'))


##Test3
        # client.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
        # client.set('Language', "Python", px=80000)
        # print((client.get('Language')))
        # print((client.ttl('Language')))
        # sleep(3)
        # print((client.ttl('Language')))


##Test4
        # today = datetime.date.today()
        # visitors = {"Dana", "John", "Alex"}
        # str_today = today.isoformat()
        # client.sadd(str_today, *visitors)
        # print(client.smembers(str_today))
        # print(client.scard(today.isoformat()))
##Test5
        # import random
        #
        # random.seed(444)
        # hats = {f"hat_id:{random.getrandbits(32)}": i for i in (
        #     {
        #         "id":1,
        #         "color": "black",
        #         "price": 49.99,
        #         "style": "fitted",
        #         "quantity": 1000,
        #         "npurchased": 0,
        #     },
        #     {
        #         "id": 2,
        #         "color": "maroon",
        #         "price": 59.99,
        #         "style": "hipster",
        #         "quantity": 500,
        #         "npurchased": 0,
        #     },
        #     {
        #         "id": 3,
        #         "color": "green",
        #         "price": 99.99,
        #         "style": "baseball",
        #         "quantity": 200,
        #         "npurchased": 0,
        #     })
        #         }
        # pprint(hats)
        # client = redis.Redis(db=1, host='127.0.0.1', port=6379)
        # with client.pipeline() as pipe:
        #     for h_id, hat_id in hats.items():
        #         pipe.hmset(h_id, hat_id)
        #     pipe.execute()
        # client.bgsave()
        # print(client.hgetall("hat:1236154736"))
        # client.hincrby("hat:1236154736", "quantity", -1)
        # print(client.hget("hat:1236154736", "quantity"))
        # print(client.keys())
        # client.expire("runner", datetime.timedelta(seconds=3))
##Test6
        # client = redis.Redis(db=2, host='127.0.0.1', port=6379)
        # restaurant_484272 = {
        #     "name": "Ravagh",
        #     "type": "Persian",
        #     "address": {
        #         "street": {
        #             "line1": "11 E 30th St",
        #             "line2": "APT 1",
        #         },
        #         "city": "New York",
        #         "state": "NY",
        #         "zip": 10016,
        #     }
        # }
        #
        # client.set(484272,json.dumps(restaurant_484272))
        # pprint(json.loads(client.get(484272)))
##Test7





    def post(self):
        data = request.json
        schema = TblTasksSchema(partial=True)
        data_object = schema.load(data, )
        db.session.add(data_object)
        db.session.commit()
        return {"msg": "task created"}, 201

    def put(self):
        user_role_id = request.args.get("user_role_id")
        if user_role_id:
            schema = TblTasksSchema(partial=True)
            user_role = TblTasks.query.get_or_404(user_role_id)
            user_role = schema.load(request.json, instance=user_role)
            db.session.commit()
            return {"msg": "task info updated", "user_role": schema.dump(user_role)}
        else:
            return {"msg": "task_id required"}, 400

    def delete(self):
        task_id = request.args.get("task_id")
        if task_id:
            task = TblTasks.query.get_or_404(task_id)
            db.session.delete(task)
            db.session.commit()
            return {"msg": "task deleted"}
        else:
            return {"msg": "task_id required"}, 400