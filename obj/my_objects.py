from tkinter import *


class MyLabel(Label):
    def __init__(self, bg="white", pady=5, **kwargs):
        super().__init__(background=bg, pady=pady, **kwargs)


class MyButton(Button):
    def __init__(self, text, width, height, bg="white", **kwargs):
        super().__init__(background=bg, text=text, width=width, height=height, **kwargs)


class MyCanvas(Canvas):
    def __init__(
        self, width=800, height=600, bg="white", highlightthickness=1, **kwargs
    ):
        super().__init__(
            width=width,
            height=height,
            background=bg,
            highlightthickness=highlightthickness,
            **kwargs,
        )
