from ui_prefabs.subpage import SubPage
from utils.get_user_tasks import get_user_tasks
from ui_prefabs.task_widget import TaskWidget
import flet



class HomePage (SubPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tasks_column = flet.Column()
        self.controls.append(self.tasks_column)
        self.refresh_tasks()
        
    
    def refresh_tasks (self):
        def on_check_task (task_name, action:str):
           if action == "open_page":
               print("open_page")
           elif action == "check_as_done":
               print("check_as_done")

        self.tasks_column.controls.clear()
        tasks = get_user_tasks()

        for t in tasks:
            tw = self.generate_task_wdgt(t=t, on_check_task=on_check_task)
            self.tasks_column.controls.append(flet.Row([tw], alignment=flet.MainAxisAlignment.CENTER))
    
    def generate_task_wdgt(self, t, on_check_task):
        def on_open_page (e):
            on_check_task(t['name'], "open_page")
        def on_long_prs (e):
            on_check_task(t['name'], "check_as_done")
        
        tw = TaskWidget(name=t['name'], done=t['done'])
        return flet.TextButton(content=tw, on_click=on_open_page, on_long_press=on_long_prs)