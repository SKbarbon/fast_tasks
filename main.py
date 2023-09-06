from ui_prefabs.subpage import SubPage

from pages.home_page import HomePage

import flet, asyncio

class Main:
    def __init__ (self):
        flet.app(target=self.app, assets_dir="assets")

    async def app (self, page:flet.Page):
        self.page = page
        self.controls_to_fill_bound = [] # All controls's bound will be as the page bound.

        page.title = "Fast task"
        page.on_resize = self.on_page_resize
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.scroll = flet.ScrollMode.ALWAYS
        page.padding = 0
        page.appbar = flet.AppBar(
            title=flet.Text("Home")
        )

        self.main_stack = flet.Stack()

        self.home_page = HomePage()

        await page.add_async(flet.SafeArea(content=self.main_stack))
        await self.open_subpage(self.home_page)

        await page.update_async()

    
    async def open_subpage (self, subpage:SubPage):
        def go_back_function ():
            self.main_stack.controls.remove(the_element)
            asyncio.create_task(self.main_stack.update_async())
        
        subpage.prepare(main_stack=self.main_stack, back_function=go_back_function)
        the_element = flet.Row([subpage], alignment=flet.MainAxisAlignment.CENTER)
        self.main_stack.controls.append(the_element)
        await self.main_stack.update_async()
        self.controls_to_fill_bound.append(subpage)
    
    async def on_page_resize (self, e):
        for cont in self.controls_to_fill_bound:
            cont.width = self.page.width
            cont.height = self.page.height - 80
            await cont.update_async()

    async def alert (self, title:str, content:str):
        pass


Main()