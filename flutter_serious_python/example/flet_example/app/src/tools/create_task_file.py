import os, json





def create_task_file ():
    documents_path = os.path.expanduser("~/Documents")
    user_tasks_file = os.path.join(documents_path, "tasks.json")

    template = {
        "tasks" : [
            {
                "name" : "Understand the app",
                "done" : False,
                "parts" : [
                    {
                        "name" : "Create a task.",
                        "done" : False
                    },
                    {
                        "name" : "Click to check a task.",
                        "done" : False
                    },
                    {
                        "name" : "Add a new task part.",
                        "done" : False
                    }
                ]
            }
        ]
    }

    open(user_tasks_file, "w+", encoding="utf-8").write(json.dumps(template))