from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
import db
import datetime



class MasterWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Отчеты')
        self.geometry('310x110')

        self.label = Label(self, text='Отчеты')
        self.select = Combobox(self, values=db.get_reports())

        self.btn = Button(self, text='Сгенерировать', command=lambda: self.generate_master())

        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.select.grid(row=0, column=1, padx=5, pady=5)
        self.btn.grid(row=1, column=2, padx=5, pady=5)

    def generate_master(self):
        val = str(self.select.get())
        order_id = int(val.split(" ")[0])
        print(f'Generating report, {order_id}')
        order = db.get_order(order_id)
        with open(f'masters/master_{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt', 'a') as f:
           f.write(f"ФИО заказчика: {order[1]}\n")
           f.write(f"Тип техники: {order[2]}\n")
           f.write(f"Мастер: {order[3]}\n")
           f.write(f"Статус ремонта: {order[7]}\n")
           f.write(f"Описание поломки: {str(order[8]).rstrip().lstrip()}\n")
           f.write(f"Дата обращения: {order[10]}\n")
        messagebox.showinfo('Отчет', 'Отчет сгенерирован')

def show_master():
    MasterWindow()
