from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
import db


class ReportsOrdersWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Отчет по заказам')
        self.geometry('500x500')
