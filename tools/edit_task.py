import os, json



def edit_task_state (task_name:str):
    documents_path = os.path.expanduser("~/Documents")
    user_tasks_file = os.path.join(documents_path, "tasks.json")

    tasks = json.loads(open(user_tasks_file, encoding="utf-8").read())['tasks']

    new_tasks = []
    
    for t in tasks:
        if str(t['name']) == str(task_name):
            if t['done'] == True: t['done'] = False
            else: t['done'] = True
            new_tasks.append(t)
        else:
            new_tasks.append(t)
    
    file_content = json.loads(open(user_tasks_file, encoding="utf-8").read())
    file_content['tasks'] = new_tasks

    open(user_tasks_file, "w+", encoding="utf-8").write(json.dumps(file_content))