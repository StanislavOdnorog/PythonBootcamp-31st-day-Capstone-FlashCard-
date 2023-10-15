from tkinter import filedialog

from core.logger import logger
from db.db_manager import *
from obj.my_objects import *


class WindowInterface:
    def __init__(self, title="Program", padding=50, bg="white", width=940, height=800):
        self.gui = Tk()
        self.gui.resizable(False, False)

        self.gui.title(title)
        self.gui.geometry(f"{width}x{height}")
        self.gui.config(padx=padding, pady=padding)
        self.gui.config(bg=bg)

        self.objects = {}

        self.current_word = (None, None)

    def start_screen(self):
        self.configure_objects()
        for _, v in self.objects.items():
            v["elem"].grid(
                column=v["col"], row=v["row"], columnspan=v["colspan"], padx=20, pady=10
            )

        self.gui.mainloop()

    def configure_objects(self):
        self.set_object(
            "delete-btn", MyButton("DELETE ALL CARDS", 30, 1, borderwidth=1), 0, 0, 1
        )
        self.set_object("read-btn", MyButton("READ CSV", 30, 1, borderwidth=1), 1, 0, 1)
        self.set_object(
            "show-btn", MyButton("PRESS NEXT to start", 33, 11, borderwidth=1), 0, 1, 2
        )
        self.set_object("next-btn", MyButton("NEXT", 30, 5), 0, 2, 2)

        self.objects["delete-btn"]["elem"].config(command=self.process_deletebtn)
        self.objects["read-btn"]["elem"].config(command=self.process_readbtn)
        self.objects["show-btn"]["elem"].config(command=self.process_showbtn)
        self.objects["next-btn"]["elem"].config(command=self.process_nextbtn)

        self.objects["show-btn"]["elem"].config(font=("Helvetica", 30, "bold"))

    def set_object(self, index, elem, col, row, colspan):
        self.objects[index] = {"elem": elem, "col": col, "row": row, "colspan": colspan}

    def process_deletebtn(self):
        WordsDBManager.delete_words()

    def process_readbtn(self):
        path = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"),))
        if path != "":
            WordsDBManager.save_words(path)

    def process_showbtn(self):
        self.current_word = self.current_word[::-1]
        self.objects["show-btn"]["elem"].config(text=self.current_word[0])

    def process_nextbtn(self):
        self.current_word = WordsDBManager.get_word()
        self.objects["show-btn"]["elem"].config(text=self.current_word[0])


if __name__ == "__main__":
    WindowInterface(title="FlasCards").start_screen()
