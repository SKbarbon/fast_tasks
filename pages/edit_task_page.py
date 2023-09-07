from ui_prefabs.subpage import SubPage
import flet, asyncio


class EditTaskPage (flet.Column):
    def __init__ (self, page:flet.Page, task_name:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.task_name = task_name


        self.get_back_appbar_and_floatingbtn = None

        self.task_name_field = flet.TextField(
            hint_text="Task..", 
            border="none", 
            value=""
        )
        self.controls.append(flet.Row([flet.Text(" 💬", size=18), self.task_name_field], alignment=flet.MainAxisAlignment.CENTER))

        self.part_tasks = flet.ListView(height=page.height - 180)
        self.controls.append(self.part_tasks)

        self.controls.append(flet.Text(""))
        
        done_btn = flet.TextButton(content=flet.Container(
            content=flet.Row([flet.Text("Done & Back", color="white", weight=flet.FontWeight.BOLD)], alignment=flet.MainAxisAlignment.CENTER),
            bgcolor=flet.colors.BLACK,
            width=200,
            height=60,
            border_radius=50
        ))
        self.controls.append(flet.Row([done_btn], alignment=flet.MainAxisAlignment.CENTER))

    async def fill_field_animation (self):
        for t in self.task_name:
            self.task_name_field.value = self.task_name_field.value + t
            await self.task_name_field.update_async()
            await asyncio.sleep(0.05)
        
        await self.task_name_field.focus_async()