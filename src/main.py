from tkinter import *
from obj.my_objects import *

class WindowInterface():
    def __init__(self, title="Program", padding=50, bg="white", width=940, height=800):
        self.gui = Tk()
        self.gui.resizable(False, False)

        self.gui.title(title)
        self.gui.geometry(f"{width}x{height}")
        self.gui.config(padx=padding, pady=padding)
        self.gui.config(bg=bg)

        self.objects = {}

    def start_screen(self):
        self.configure_objects()
        for _, v in self.objects.items():
            v["elem"].grid(column=v["col"], row=v["row"], columnspan=v["colspan"], padx=20, pady=10)

        
        self.gui.mainloop()

    def configure_objects(self):
        self.set_object("show-btn", MyButton("START", 113, 35, borderwidth=1), 0, 0, 2)
        self.set_object("no-btn", MyButton("NO", 30, 5), 0, 1, 1)
        self.set_object("yes-btn", MyButton("YES", 30, 5), 1, 1, 1)

        self.objects["show-btn"]["elem"].config(command=self.process_showbtn)
        self.objects["no-btn"]["elem"].config(command=self.process_nobtn)
        self.objects["yes-btn"]["elem"].config(command=self.process_yesbtn)

    def set_object(self, index, elem, col, row, colspan):
        self.objects[index] = {"elem": elem, "col": col, "row": row, "colspan": colspan}
    
    def process_showbtn(self):
        pass

    def process_nobtn(self):
        pass

    def process_yesbtn(self):
        pass



if __name__ == "__main__":
    WindowInterface(title="FlasCards").start_screen()