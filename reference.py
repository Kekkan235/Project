from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
from tkinter import messagebox

class reference(Toplevel):
    def __init__(self):
        #super().__init__()
        messagebox.showinfo("Cправка", f"Здесь вы можете добавлять заказы, редактировать их, а так же посмотреть отчетности ")
def show_reference():
    reference()


class aboutprogramm(Toplevel):
    def __init__(self):
        #super().__init__()
        messagebox.showinfo("О программе", f"Здравствуйте! Это программа,предназначенная для обработки заказов для ремонта бытовой техники.")
def show_about():
    aboutprogramm()
