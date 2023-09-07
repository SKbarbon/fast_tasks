import flet



class SubTaskWidget (flet.Container):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    def test (page:flet.Page):
        page.add(SubTaskWidget())
    
    flet.app(target=test)