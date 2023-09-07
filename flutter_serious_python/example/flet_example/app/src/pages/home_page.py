from ui_prefabs.subpage import SubPage
from utils.get_user_tasks import get_user_tasks
from ui_prefabs.task_widget import TaskWidget
from tools.edit_task import edit_task_state
import flet, asyncio



class HomePage (SubPage):
    def __init__(self, check_animation_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.check_animation_function = check_animation_function

        self.sub_title = flet.Text("", height=10)
        self.controls.append(self.sub_title)

        self.tasks_column = flet.Column()
        self.controls.append(self.tasks_column)
        self.refresh_tasks()
        
    
    def refresh_tasks (self):
        def on_check_task (task_name, action:str):
           if action == "open_page":
               print("open_page")
           elif action == "check_as_done":
               edit_task_state(task_name)
               self.refresh_tasks()
               asyncio.create_task(self.tasks_column.update_async())
               asyncio.create_task(self.check_animation_function())


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