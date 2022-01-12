
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.sql import func

from task_manager_api.extensions import db


class TblTasks(db.Model):
    __tablename__ = 'tbl_tasks'
    task_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    task_title = db.Column(db.String(180), nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    reminder = db.Column(db.Boolean(True))
    create_time = db.Column(db.DateTime(timezone=True), server_default=func.now())


