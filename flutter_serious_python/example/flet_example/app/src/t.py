import flet


def main (page:flet.Page):
    stk = flet.Stack()
    page.add(stk)

    stk.controls.append(flet.Text("fff", top=50, left=140))
    stk.update()


flet.app(target=main)