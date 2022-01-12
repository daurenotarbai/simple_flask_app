# -*- coding: utf-8 -*-
# @Time    : 12/02/2021 13:41
# @Author  : Aydar
# @FileName: sch_roles.py
# @Software: PyCharm
# @Telegram   ：aydardev
from marshmallow import fields, Schema

# from task_manager_api.api.schemas import (
#     EGovServicesSchema
# )
from task_manager_api.extensions import ma, db
from task_manager_api.models import (
    TblRoles, TblUsersRole
)


class TblRolesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TblRoles
        sqla_session = db.session
        load_instance = True


class TblUsersRoleSchema(ma.SQLAlchemyAutoSchema):
    roles_id = ma.auto_field()
    # egov_services_id = ma.auto_field()
    roles = ma.Nested(TblRolesSchema)
    # egov_services = ma.Nested(EGovServicesSchema)

    class Meta:
        model = TblUsersRole
        sqla_session = db.session
        load_instance = True
