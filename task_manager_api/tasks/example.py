from task_manager_api.extensions import celery


@celery.task
def dummy_task():
    return "OK"
