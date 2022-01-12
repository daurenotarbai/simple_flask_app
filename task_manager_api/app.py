from flask import Flask
from task_manager_api import api
from task_manager_api.commons.get_media import image_blueprint
from task_manager_api.extensions import apispec
from task_manager_api.extensions import db
from task_manager_api.extensions import jwt
from task_manager_api.extensions import migrate, celery
from flask_cors import CORS


def create_app(testing=False):

    app = Flask("task_manager_api")
    app.config.from_object("task_manager_api.config")

    if testing is True:
        app.config["TESTING"] = True

    CORS(app)
    configure_extensions(app)
    configure_apispec(app)
    register_blueprints(app)
    init_celery(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(api.views.blueprint)
    app.register_blueprint(image_blueprint)


def init_celery(app=None):
    app = app or create_app()
    celery.conf.update(app.config.get("CELERY", {}))

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
