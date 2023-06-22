from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview, Button, Entry
import db
from edit_forms import EditOrderWindow


class OrderWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Список заказов')
        self.geometry('1800x600')




        tv_orders = Treeview(self)
        tv_orders.pack(fill=BOTH, expand=True)
        tv_orders['columns'] = ("ID", "ФИО заказчика","Тип техники","Мастер", "Номер телефона", "Серия паспорта","Номер паспорта","Статус ремонта","Описание поломки","Статус оплаты","Дата обращения", 'Удалить')
        tv_orders.heading("#0", text="", anchor=W)
        tv_orders.column("#0", width=0, stretch=NO)
        tv_orders.heading("ID", text="ID", anchor=W)
        tv_orders.column("ID", width=50, stretch=NO)
        tv_orders.heading("ФИО заказчика", text="ФИО заказчика", anchor=W)
        tv_orders.column("ФИО заказчика", width=200, stretch=NO)
        tv_orders.heading("Тип техники", text="Тип техники", anchor=W)
        tv_orders.column("Тип техники", width=110)
        tv_orders.heading("Мастер", text="Мастер", anchor=W)
        tv_orders.column("Мастер", width=100)
        tv_orders.heading("Номер телефона", text="Номер телефона", anchor=W)
        tv_orders.column("Номер телефона", width=120)
        tv_orders.heading("Серия паспорта", text="Серия паспорта", anchor=W)
        tv_orders.column("Серия паспорта", width=100)
        tv_orders.heading("Номер паспорта", text="Номер паспорта", anchor=W)
        tv_orders.column("Номер паспорта", width=100)
        tv_orders.heading("Статус ремонта", text="Статус ремонта", anchor=W)
        tv_orders.column("Статус ремонта", width=150)
        tv_orders.heading("Описание поломки", text="Описание поломки", anchor=W)
        tv_orders.column("Описание поломки", width=150)
        tv_orders.heading("Статус оплаты", text="Статус оплаты", anchor=W)
        tv_orders.column("Статус оплаты", width=150)
        tv_orders.heading("Дата обращения", text="Дата обращения", anchor=W)
        tv_orders.column("Дата обращения", width=150)
        tv_orders.heading("Удалить", text="Удалить", anchor=W)
        tv_orders.column("Удалить", width=50)

        rows = db.get_orders()
        for row in rows:
            row = list(row)
            row.append('x')
            tv_orders.insert("", END, text="", values=row)

        tv_orders.bind('<Double-1>', lambda event : set_cell_value(tv_orders, event))
        def set_cell_value(tv_orders, event): # Double click to enter the edit state
            print(event)
            for item in tv_orders.selection():
                #item = I001
                item_text = tv_orders.item(item, "values")
                print(item_text) # Output the value of the selected row
                column= tv_orders.identify_column(event.x)# column
                row = tv_orders.identify_row(event.y) #row
                print(f'Coloum{column} Row{row}')
            cn = int(str(column).replace('#',''))
            print(cn)
            #rn = int(str(row).replace('I',''))
            if cn == 1:
                return
            if cn == 12:
                db.delete_order(item_text[0])
                for item in tv_orders.get_children():
                    tv_orders.delete(item)
                rows = db.get_orders()
                for row in rows:
                    row = list(row)
                    row.append('x')
                    tv_orders.insert("", END, text="", values=row)
                return
            self.destroy()
            EditOrderWindow(int(item_text[0]))

def show_orders():
    OrderWindow()
