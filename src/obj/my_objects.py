from tkinter import *


class MyButton(Button):
    def __init__(self, text, width, height, bg="white", **kwargs):
        super().__init__(background=bg, text=text, width=width, height=height, **kwargs)
