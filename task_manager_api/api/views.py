from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from task_manager_api.extensions import apispec
from task_manager_api.api.resources import *
from task_manager_api.api.resources.res_tasks import TblTasksResource, TestRedisResource
# from task_manager_api.api.resources.
blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(TblRolesResource, "/roles", endpoint="roles")
api.add_resource(TblUserRolesResource, "/user-roles", endpoint="user-roles")
api.add_resource(TblTasksResource, "/tasks/", endpoint="task_list")
api.add_resource(TestRedisResource, "/test", endpoint="test")


@blueprint.before_app_first_request
def register_views():
    pass


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400



