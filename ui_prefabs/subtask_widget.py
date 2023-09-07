import flet
import flet as ft



class SubTaskWidget (flet.Container):
    def __init__ (self, name:str, done:bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.content = flet.Row(
            controls=[
                ft.Checkbox(
                    value=done
                ),
                ft.Text(
                    value=name
                )
            ]
        )


if __name__ == "__main__":
    def test (page:flet.Page):
        page.add(SubTaskWidget(name="Go fuck yourself", done=True))
    
    flet.app(target=test)