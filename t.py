import flet as ft
import flet

def main(page: ft.Page):
    c = flet.ListView(height=500)
    page.add(c)

    page.add(flet.Text("gg"))

ft.app(target=main)