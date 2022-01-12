"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
CELERY = {
    "broker_url": os.getenv("CELERY_BROKER_URL"),
    "result_backend": os.getenv("CELERY_RESULT_BACKEND_URL"),
}

ROOT_URL =  "http://192.168.1.39:5001"

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
# upload path img
UPLOAD_IMG = '{}/media/img'.format(PROJECT_HOME)
UPLOAD_SIGNED_CONTRACT = '{}/media/signed-docs'.format(PROJECT_HOME)
UPLOAD_STAFF_PHOTO = '{}/media/org-staff-photo'.format(PROJECT_HOME)
UPLOAD_STAFF_CERTIFICATE = '{}/media/org-staff-certificates'.format(PROJECT_HOME)
UPLOAD_STAFF_ACHIEVEMENT = '{}/media/org-staff-achievements'.format(PROJECT_HOME)