import sqlite3


def get_order(id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM orders WHERE id={id}')
    data = cursor.fetchone()
    conn.close()
    return data

def get_orders():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM orders''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def put_order(order_id, values):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute(f"""Update orders set
                      name = ?,
                      appliance = ?,
                      master = ?,
                      phone = ?,
                      passport_series = ?,
                      passport_num = ?,
                      status = ?,
                      breakdown = ?,
                      payment = ?
                      where id = {order_id}""", values)
        conn.commit()

def get_reports():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT id, name, master FROM orders''')
    rows = cursor.fetchall()
    conn.close()
    return rows
