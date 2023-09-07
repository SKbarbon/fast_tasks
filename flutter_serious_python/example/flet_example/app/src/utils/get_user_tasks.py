from tools.create_task_file import create_task_file
import os, json


def get_user_tasks():
    documents_path = os.path.expanduser("~/Documents")
    user_tasks_file = os.path.join(documents_path, "tasks.json")

    if not os.path.isfile(user_tasks_file):
        create_task_file()
    
    file_content = json.loads(open(user_tasks_file, encoding="utf-8").read())
    all_tasks = file_content['tasks']

    return all_tasks