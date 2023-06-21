from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
import db



class ReportWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Отчеты')
        self.geometry('500x500')

        self.label = Label(self, text='Отчеты')
        self.select = Combobox(self, values=db.get_reports())

        self.btn = Button(self, text='Сгенерировать', command=lambda: print('click'))

        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.select.grid(row=0, column=1, padx=5, pady=5)
        self.btn.grid(row=1, column=2, padx=5, pady=5)
