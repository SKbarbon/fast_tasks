import flet



class SubPage (flet.Column):
    """A subpage used to open page as a custom navigation."""
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.parent_stack = None
        self.back_function = None
    
    def prepare (self, main_stack, back_function):
        self.parent_stack = main_stack
    

    def back_to_root (self):
        if self.back_function != None:
            self.back_function()