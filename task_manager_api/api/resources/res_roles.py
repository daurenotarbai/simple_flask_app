


from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from task_manager_api.extensions import db
from task_manager_api.commons.pagination import paginate
from task_manager_api.models import (
    TblRoles,
    TblUsersRole
)
from task_manager_api.api.schemas import (
    TblRolesSchema,
    TblUsersRoleSchema
)


class TblRolesResource(Resource):
    # method_decorators = [jwt_required]

    def get(self):
        schema = TblRolesSchema(many=True)
        query = TblRoles.query
        return paginate(query, schema)


class TblUserRolesResource(Resource):
    # method_decorators = [jwt_required]

    def get(self):
        schema = TblUsersRoleSchema(many=True)
        role_id = request.args.get('role_id', None)
        if role_id is not None:
            query = TblUsersRole.query.filter_by(roles_id=role_id)
        else:
            query = TblUsersRole.query
        return paginate(query, schema)

    def post(self):
        data = request.json
        user_role_schema = TblUsersRoleSchema(partial=True)
        data_object = user_role_schema.load(data, )
        db.session.add(data_object)
        db.session.commit()
        return {"msg": "user role created"}, 201

    def put(self):
        user_role_id = request.args.get("user_role_id")
        if user_role_id:
            schema = TblUsersRoleSchema(partial=True)
            user_role = TblUsersRole.query.get_or_404(user_role_id)
            user_role = schema.load(request.json, instance=user_role)
            db.session.commit()
            return {"msg": "user role updated", "user_role": schema.dump(user_role)}
        else:
            return {"msg": "user role required"}, 400

    def delete(self):
        user_role_id = request.args.get("user_role_id")
        if user_role_id:
            user_role = TblUsersRole.query.get_or_404(user_role_id)
            db.session.delete(user_role)
            db.session.commit()
            return {"msg": "user role deleted"}
        else:
            return {"msg": "user_role_id required"}, 400
