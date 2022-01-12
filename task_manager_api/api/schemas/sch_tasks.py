
from marshmallow import fields, Schema

# from task_manager_api.api.schemas import (
#     EGovServicesSchema
# )
from task_manager_api.extensions import ma, db
from task_manager_api.models.mdl_tasks import TblTasks


class TblTasksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TblTasks
        sqla_session = db.session
        load_instance = True



