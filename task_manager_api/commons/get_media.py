from flask import request, Blueprint, send_from_directory
from task_manager_api.config import UPLOAD_IMG,UPLOAD_STAFF_PHOTO,UPLOAD_STAFF_CERTIFICATE,UPLOAD_STAFF_ACHIEVEMENT

image_blueprint = Blueprint("images", __name__, url_prefix="/images")


@image_blueprint.route("/<path:filename>", methods=["GET"])
def get_img_file(filename):
    print(filename)
    return send_from_directory(UPLOAD_IMG, filename, as_attachment=False)

@image_blueprint.route("/staff-img/<path:filename>", methods=["GET"])
def get_staff_img(filename):
    print(filename)
    return send_from_directory(UPLOAD_STAFF_PHOTO, filename, as_attachment=False)

@image_blueprint.route("/staff-certificate/<path:filename>", methods=["GET"])
def get_staff_certificate(filename):
    print(filename)
    return send_from_directory(UPLOAD_STAFF_CERTIFICATE, filename, as_attachment=False)

@image_blueprint.route("/staff-achievement/<path:filename>", methods=["GET"])
def get_staff_achievement(filename):
    print(filename)
    return send_from_directory(UPLOAD_STAFF_ACHIEVEMENT, filename, as_attachment=False)