from tkinter import Label

class Label(Label):

    def __init__(self, text, column, row):
        super().__init__()
        self.grid(column=column, row=row)
        self.config(text=text)
