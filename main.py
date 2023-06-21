from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Notebook, Treeview
import sys
import datetime
import sqlite3



conn = sqlite3.connect('orders.db') # подключение к базе данных
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                appliance TEXT,
                master TEXT,
                phone TEXT,
                passport_series TEXT,
                passport_num TEXT,
                status TEXT,
                breakdown TEXT,
                payment TEXT,
                datetime TEXT)''')

conn.commit() # сохранение изменений
conn.close() # закрытие соединения

def submit():
    name = name_tf.get()
    appliance = appliance_cb.get()
    master = masters_cb.get()
    phone = phonenumber_tf.get()
    passport_series = passports_tf.get()
    passport_num = passportn_tf.get()
    status = status_cb.get()
    breakdown = breakdown_tf.get("1.0",END)
    payment = payment_cb.get()
    datetimenow = datetime.datetime.now()
    datetimewp = datetimenow.strftime("%d.%m.%Y %H:%M:%S")
    pathfile = r'F:\Проект\orders.txt' #'F:\Проект\orders.txt'
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO orders(name, appliance, master, phone, passport_series, passport_num, status, breakdown, payment, datetime)
                VALUES(?,?,?,?,?,?,?,?,?,?)''',
                (name, appliance, master, phone, passport_series, passport_num, status, breakdown, payment, datetimewp))
    conn.commit()
    conn.close()
    with open("orders.txt", "a") as file:
        file.write(f"ФИО заказчика: {name}\n")
        file.write(f"Номер телефона заказчика: {phone}\n")
        file.write(f"Серия паспорта заказчика:{passport_series}\n")
        file.write(f"Номер паспорта заказчика:{passport_num}\n")
        file.write(f"ФИО Мастера: {master}\n")
        file.write(f"Тип техники: {appliance}\n")
        file.write(f"Описание поломки: {breakdown}")
        file.write(f"Статус ремонта: {status}\n")
        file.write(f"Статус оплаты: {payment}\n")
        file.write(f"Дата обращения: {datetimewp}\n")
        file.write("===================================\n")
        messagebox.showinfo("Результат", f"Здравствуйте, {name}! Ваша заявка на ремонт {appliance.lower()} принята. Ваш мастер {master.lower()}")



window = Tk()
window.title('Ремонт бытовой техники')
window.geometry('1920x1080')

window.option_add("*tearOff", FALSE)

main_menu = Menu()




frame = Frame(
    window,
    padx=10,
    pady=10
)
class OrderWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Список заказов')
        self.geometry('1800x600')

        tv_orders = Treeview(self)
        tv_orders.pack(fill=BOTH, expand=True)
        tv_orders['columns'] = ("ID", "ФИО заказчика","Тип техники","Мастер", "Номер телефона", "Серия паспорта","Номер паспорта","Статус ремонта","Описание поломки","Статус оплаты")
        tv_orders.heading("#0", text="", anchor=W)
        tv_orders.column("#0", width=0, stretch=NO)
        tv_orders.heading("ID", text="ID", anchor=W)
        tv_orders.column("ID", width=50, stretch=NO)
        tv_orders.heading("ФИО заказчика", text="ФИО заказчика", anchor=W)
        tv_orders.column("ФИО заказчика", width=200, stretch=NO)
        tv_orders.heading("Тип техники", text="Тип техники", anchor=W)
        tv_orders.column("Тип техники", width=150)
        tv_orders.heading("Мастер", text="Мастер", anchor=W)
        tv_orders.column("Мастер", width=150)
        tv_orders.heading("Номер телефона", text="Номер телефона", anchor=W)
        tv_orders.column("Номер телефона", width=150)
        tv_orders.heading("Серия паспорта", text="Серия паспорта", anchor=W)
        tv_orders.column("Серия паспорта", width=130)
        tv_orders.heading("Номер паспорта", text="Номер паспорта", anchor=W)
        tv_orders.column("Номер паспорта", width=130)
        tv_orders.heading("Статус ремонта", text="Статус ремонта", anchor=W)
        tv_orders.column("Статус ремонта", width=160)
        tv_orders.heading("Описание поломки", text="Описание поломки", anchor=W)
        tv_orders.column("Описание поломки", width=200)
        tv_orders.heading("Статус оплаты", text="Статус оплаты", anchor=W)
        tv_orders.column("Статус оплаты", width=150)


        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM orders''')
        rows = cursor.fetchall()
        for row in rows:
            tv_orders.insert("", END, text="", values=row)
        conn.close()

notebook = Notebook(window)
#notebook.pack(anchor = "nw") -  я не знаю что эт и для чего,на прогу вроде не влияет

def show_orders():
    OrderWindow()

orders_btn = Button(
    window,
    text="Заказы",
    command = show_orders
)
orders_btn.pack(pady=5,anchor = NW)

file_menu = Menu()
file_menu.add_command(label="Открыть бд",command = lambda: show_orders())
file_menu.add_separator()
file_menu.add_command(label="Добавить запись")
file_menu.add_command(label="Редактировать бд")
file_menu.add_separator()
file_menu.add_command(label="Закрыть")
file_menu2 = Menu()
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Справка")
file_menu2.add_separator()
file_menu2.add_command(label="Закрыть")


main_menu.add_cascade(label="Работа с БД", menu=file_menu)
main_menu.add_cascade(label="Отчет")
main_menu.add_cascade(label="Справка",menu=file_menu2)

header = Label(
    frame,
    text="Ремонт бытовой техники",bg="grey",fg="white",font=("Helvetica", 24)
)
header.pack(side=TOP, fill=X)
frame.pack(expand=True)

name_lb = Label(
    frame,
    text="Введите ФИО заказчика: ",bg="grey",fg="white"
)
name_lb.pack(pady=10)

name_tf = Entry(
    frame, width = 40
)
name_tf.pack(pady=5)

phonenumber_lb = Label(
    frame,
    text="Введите номер телефона заказчика: ",bg="grey",fg="white"
)
phonenumber_lb.pack(pady=11)
phonenumber_tf = Entry(
    frame,
)
phonenumber_tf.pack(pady=6)

passports_lb = Label(
    frame,
    text= "Введите серию паспорта заказчика: " ,bg="grey",fg="white"
)
passports_lb.pack(pady=11)
passports_tf=Entry(
    frame,
)
passports_tf.pack(pady=6)

passportn_lb = Label(
    frame,
    text= "Введите номер паспорта заказчика: " ,bg="grey",fg="white"
)
passportn_lb.pack(pady=11)
passportn_tf=Entry(
    frame,
)
passportn_tf.pack(pady=6)

appliance_lb = Label(
    frame,
    text="Выберите тип техники: ",bg="grey",fg="white"
)
appliance_lb.pack(pady=10)

appliance_cb = Combobox(
    frame,
    values=["Холодильник", "Плита", "Стиральная машина", "Пылесос"],
    state="readonly"
)
appliance_cb.current(0)
appliance_cb.pack(pady=5)

breakdown_lb = Label(
    frame,
    text= "Описание поломки: ",bg="grey",fg="white"
)
breakdown_lb.pack(pady=10)

breakdown_tf=Text(
    frame,
    width = 40,wrap = WORD, height = 5 , font=("Helvetica",10) # width - ширина,wrap - перенос, heigth - высота
)
breakdown_tf.pack(pady=6)
masters_lb= Label(
    frame,
    text="Назначить мастера: ",bg="grey",fg="white"
)
masters_lb.pack(pady=10)


masters_cb = Combobox(
    frame,
    values=["Иванов А.И","Петров А.Б","Антошин С.И","Степанов Д.П"],
    state="readonly"
)
masters_cb.current(0)
masters_cb.pack(pady=5)

status_lb = Label(
    frame,
    text="Статус ремонта: ",bg="grey",fg="white"
)
status_lb.pack(pady=10)

status_cb=Combobox(
    frame,
    values=["Не начат","В процессе","Ожидает запчастей/материалов","Ожидает решения клиента","Завершён"],
    state = "readonly"
)
status_cb.current(0)
status_cb.pack(pady=5)

payment_lb = Label(
    frame,
    text="Статус оплаты: " ,bg="grey",fg="white"
)
payment_lb.pack(pady=10)

payment_cb = Combobox(
    frame,
    values=["Оплачено полностью","Частичная оплата","Ожидание оплаты","Просроченная оплата","Оплата при получении","Без оплаты"],
    state="readonly"
)
payment_cb.current(0)
payment_cb.pack(pady=5)

submit_btn = Button(
    frame,
    text="Сформировать заявку",
command=submit
)
submit_btn.pack(pady=20)



window.config(menu=main_menu)
window.configure(bg='grey')
window.mainloop()