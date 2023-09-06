import flet, random, asyncio



class AnimationsBg (flet.Stack):
    def __init__ (self, emoji:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emoji = emoji

        self.animate_scale = 1000
        self.animate_opacity = 1000

        self.conts = []
        for i in range(0, 100):
            rand_size = random.choice(range(13, 23))
            rot_val = random.choice(range(-20, 21))
            random_duration = random.choice(range(400, 1600))
            c = flet.Container(
                content=flet.Text(f"{emoji}", size=rand_size, weight="bold"),
                animate=random_duration,
                animate_position=random_duration,
                animate_offset=random_duration,
                rotate=flet.Rotate(rot_val),
                top=500,
                left=0,
                opacity=0.0
            )
            self.controls.append(c)
            self.conts.append(c)
    

    async def reSetup (self, emoji=""):
        self.emoji = emoji
        for i in range(0, 100):
            rand_size = random.choice(range(13, 23))
            rot_val = random.choice(range(-20, 21))
            random_duration = random.choice(range(400, 1600))
            c = flet.Container(
                content=flet.Text(f"{self.emoji}", size=rand_size, weight="bold"),
                animate=random_duration,
                animate_position=random_duration,
                animate_offset=random_duration,
                rotate=flet.Rotate(rot_val),
                top=500,
                left=0,
                opacity=0.0
            )
            self.controls.append(c)
            self.conts.append(c)
        
        await self.update_async()
        
        
    async def start_animation (self):
        width = 0
        if self.page != None:
            width = int(self.page.width)
            if width == 0: width = 500
        
        for cc in self.conts:
            cc : flet.Container = cc
            cc.left = random.choice(range(width))
            await cc.update_async()
        
        await asyncio.sleep(0.3)

        for cc in self.conts:
            cc : flet.Container = cc
            cc.opacity = 1.0
            cc.top = -50
            await cc.update_async()

            self.controls.remove(cc)
            self.conts.remove(cc)
    
    def prepare (self, main_stack, back_function):
        self.parent_stack = main_stack
    

    def back_to_root (self):
        if self.back_function != None:
            self.back_function()