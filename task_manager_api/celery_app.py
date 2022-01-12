from task_manager_api.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("task_manager_api.tasks.example",)
