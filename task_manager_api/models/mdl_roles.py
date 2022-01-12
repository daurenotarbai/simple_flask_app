
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.sql import func

from task_manager_api.extensions import db


class TblRoles(db.Model):
    __tablename__ = 'tbl_roles'
    role_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    role_name_kk = db.Column(db.String(180), nullable=False)
    role_name_ru = db.Column(db.String(180), nullable=False)
    role_key = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime(timezone=True), server_default=func.now())


class TblUsersRole(db.Model):
    __tablename__ = 'tbl_user_roles'
    user_role_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    roles = db.relationship("TblRoles", backref=backref("tbl_roles", uselist=False))
    roles_id = db.Column(UUID(as_uuid=True), db.ForeignKey('tbl_roles.role_id'), nullable=False)
    users_id = db.Column(UUID(as_uuid=True), nullable=False)
    # egov_services = db.relationship("TblEGovServices", backref=backref("tbl_egov_services", uselist=False))
    # egov_services_id = db.Column(UUID(as_uuid=True), db.ForeignKey('tbl_egov_services.egov_service_id'), nullable=False)
    users_fullname = db.Column(db.String(180), nullable=False)
    create_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
