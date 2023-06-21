from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
import db
import orders_view

class EditOrderWindow(Toplevel):
    def __init__(self, order_id):
        super().__init__()
        self.title('Редактировать заказ')
        self.geometry('500x500')
        data = db.get_order(order_id) # получаем данные заказа по его ID

        # создаем форму с полями для редактирования данных заказа
        self.name_label = Label(self, text='ФИО заказчика')
        self.name_entry = Entry(self, width=30)
        self.name_entry.insert(0, data[1]) # устанавливаем текущее имя заказчика в поле ввода

        self.appliance_label = Label(self, text='Тип техники')
        self.appliance_combobox = Combobox(self, values=['Холодильник', 'Стиральная машина', 'Посудомоечная машина'])
        # self.appliance_combobox.current(data[2]-1) # устанавливаем текущий тип техники в комбобокс

        self.master_label = Label(self, text='Мастер')
        self.master_combobox = Combobox(self, values=['Иванов', 'Петров', 'Сидоров'])
        # self.master_combobox.current(data[3]-1) # устанавливаем текущего мастера в комбобокс

        self.phone_label = Label(self, text='Номер телефона')
        self.phone_entry = Entry(self, width=20)
        self.phone_entry.insert(0, data[4]) # устанавливаем текущий номер телефона в поле ввода

        self.passport_series_label = Label(self, text='Серия паспорта')
        self.passport_series_entry = Entry(self, width=10)
        self.passport_series_entry.insert(0, data[5]) # устанавливаем текущую серию паспорта в поле ввода

        self.passport_num_label = Label(self, text='Номер паспорта')
        self.passport_num_entry = Entry(self, width=10)
        self.passport_num_entry.insert(0, data[6]) # устанавливаем текущий номер паспорта в поле ввода

        self.status_label = Label(self, text='Статус ремонта')
        self.status_combobox = Combobox(self, values=['Принят', 'Выполняется', 'Завершен'])
        # self.status_combobox.current(data[7]-1) # устанавливаем текущий статус ремонта в комбобокс

        self.breakdown_label = Label(self, text='Описание поломки')
        self.breakdown_text = Text(self, width=40, height=5)
        self.breakdown_text.insert(END, data[8]) # устанавливаем текущее описание поломки в текстовое поле

        self.payment_label = Label(self, text='Статус оплаты')
        self.payment_combobox = Combobox(self, values=['Оплачен', 'Не оплачен'])
        # self.payment_combobox.current(data[9]-1) # устанавливаем текущий статус оплаты в комбобокс

        self.save_button = Button(self, text='Сохранить', command=lambda: self.save_changes(order_id))

        # размещаем форму на экране
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.appliance_label.grid(row=1, column=0, padx=5, pady=5)
        self.appliance_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.master_label.grid(row=2, column = 0, padx=5, pady=5)
        self.master_combobox.grid(row = 2, column = 1, padx=5, pady=5)
        self.phone_label.grid(row = 3, column = 0, padx=5, pady=5)
        self.phone_entry.grid(row = 3, column = 1, padx=5, pady=5)
        self.passport_series_label.grid(row = 4, column = 0, padx=5, pady=5)
        self.passport_series_entry.grid(row = 4, column = 1, padx=5, pady=5)
        self.passport_num_label.grid(row=5, column=0, padx=5, pady=5)
        self.passport_num_entry.grid(row = 5, column = 1, padx=5, pady=5)
        self.status_label.grid(row = 6, column = 0, padx=5, pady=5)
        self.status_combobox.grid(row = 6, column = 1, padx=5, pady=5)
        self.breakdown_label.grid(row = 7, column = 0, padx=5, pady=5)
        self.breakdown_text.grid(row = 7, column = 1, padx=5, pady=5)
        self.payment_label.grid(row = 8, column = 0, padx=5, pady=5)
        self.payment_combobox.grid(row = 8, column = 1, padx=5, pady=5)
        self.save_button.grid(row = 9, column = 1, padx=5, pady=5)
    def save_changes(self,order_id):
        values = (
           self.name_entry.get(),
           self.appliance_combobox.current(0),
           self.master_combobox.current(0),
           self.phone_entry.get(),
           self.passport_series_entry.get(),
           self.passport_num_entry.get(),
           self.status_combobox.current(0),
           self.breakdown_text.get("1.0",END),
           self.payment_combobox.current(0)
       )
        print(f'values for upd {values}')
        print(f'order_id {order_id}')
        db.put_order(order_id, values)
        orders_view.show_orders()
        self.destroy()
