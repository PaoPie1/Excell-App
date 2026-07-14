import sqlite3

conn = sqlite3.connect("stainless_store.db")
cursor = conn.cursor()

conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
             product_id INTEGER PRIMARY KEY AUTOINCREMENT,
             unit_name TEXT NOT NULL,
             unit_cost REAL NOT NULL,
             selling_price REAL NOT NULL,
             stock_quantity INTEGER NOT NULL
             )
''')

conn.execute('''
        CREATE TABLE IF NOT EXISTS sales (
             sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
             product_id INTEGER,
             sold_to TEXT NOT NULL,
             sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             sale_quantity INTEGER NOT NULL,
             unit_cost REAL NOT NULL,
             selling_price REAL NOT NULL
             )
        ''')

conn.commit()
conn.close()

def execute(query, param=()):
    with sqlite3.connect("stainless_store.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, param)

def update_product_name(prod_id, new_name):
    query = "UPDATE products SET unit_name = ? WHERE product_id = ?"
    execute(query, (new_name, prod_id))

def update_product_cost(prod_id, new_cost):
    query = "UPDATE products SET unit_cost = ? WHERE product_id = ?"
    execute(query, (new_cost, prod_id))

def update_product_selling_price(prod_id, new_sell_price):
    query = "UPDATE products SET selling_price = ? WHERE product_id = ?"
    execute(query, (new_sell_price, prod_id))

def update_product_stock(prod_id, new_stock):
    query = "UPDATE products SET stock_quantity = ? WHERE product_id = ?"
    execute(query, (new_stock, prod_id))