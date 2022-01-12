import os
from task_manager_api.api.helper.config import (
    IMG_ALLOWED_EXTENSIONS
)


def create_new_folder(local_dir):
    new_path = local_dir
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def img_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMG_ALLOWED_EXTENSIONS