import flet



class TaskWidget (flet.Container):
    def __init__ (self, name:str, done:bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = name

        
        if done:
            txt_color = flet.colors.WHITE38
            mark = "✅"
        else:
            txt_color = flet.colors.BLACK
            mark = ""


        self.content = flet.Row([
            flet.Text(f" {mark} {name}", color=txt_color)
        ])


        # props
        self.border = flet.border.all(0.5, color="black")
        self.height = 50
        self.width = 300
        self.border_radius = 12