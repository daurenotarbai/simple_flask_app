FLASK_ENV=development
FLASK_APP=task_manager_api.app:create_app
SECRET_KEY=changeme
DATABASE_URI=postgres://postgres:*****@localhost:5432/task_manager_db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
