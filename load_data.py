import psycopg2
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env(".env")

try:
    connection = psycopg2.connect(
        dbname=env("DB_NAME"),
        user=env("DB_USER"),
        password=env("DB_PASSWORD"),
        host="127.0.0.1",
        port="5432"
    )
    connection.autocommit = True
except Exception as e:
    print(f"An error occurred: {e}")

cursor = connection.cursor()

def insert_warehouse_material():
    global cursor
    # delete all rows from the warehouse_material table and reset id
    cursor.execute("TRUNCATE TABLE warehouse_material RESTART IDENTITY CASCADE")
    # insert new rows into warehouse_material table
    postgres_insert_query = """ INSERT INTO warehouse_material (title)  VALUES (%s)"""
    records_to_insert = ['Mato', 'Ip', 'Tugma', 'Zamok']
    for record in records_to_insert:
        cursor.execute(postgres_insert_query, (record,))

def insert_warehouse_product():
    global cursor
    # delete all rows from the warehouse_product table and reset id
    cursor.execute("TRUNCATE TABLE warehouse_product RESTART IDENTITY CASCADE")
    # alter guid data type to uuid and set default uuid generator
    cursor.execute("ALTER TABLE warehouse_product ALTER COLUMN guid TYPE uuid")
    cursor.execute("ALTER TABLE warehouse_product ALTER COLUMN guid SET DEFAULT gen_random_uuid()")
    # insert new rows into warehouse_product table
    postgres_insert_query = """ INSERT INTO warehouse_product (title)  VALUES (%s)"""
    records_to_insert = ['Koylak', 'Shim']
    for record in records_to_insert:
        cursor.execute(postgres_insert_query, (record,))

def insert_warehouse_productmaterial():
    global cursor
    # delete all rows from the warehouse_product_material table and reset id
    cursor.execute("TRUNCATE TABLE warehouse_productmaterial RESTART IDENTITY")
    # insert new rows into warehouse_product_material table
    postgres_insert_query = """ INSERT INTO warehouse_productmaterial (quantity, material_id_id, product_id_id, quantity_type)  VALUES (%s, %s, %s, %s)"""
    cursor.execute(postgres_insert_query, ('0.8', 1, 1, 'MTSQ'))
    cursor.execute(postgres_insert_query, ('5', 3, 1, 'PC'))
    cursor.execute(postgres_insert_query, ('10', 2, 1, 'MT'))
    cursor.execute(postgres_insert_query, ('1.4', 1, 2, 'MTSQ'))
    cursor.execute(postgres_insert_query, ('15', 2, 2, 'MT'))
    cursor.execute(postgres_insert_query, ('1', 4, 2, 'PC'))

def insert_warehouse_warehouse():
    global cursor
    # delete all rows from the warehouse_warehouse table and reset id
    cursor.execute("TRUNCATE TABLE warehouse_warehouse RESTART IDENTITY")
    # insert new rows into warehouse_warehouse table
    postgres_insert_query = """ INSERT INTO warehouse_warehouse (remainder, price, material_id_id)  VALUES (%s, %s, %s)"""
    cursor.execute(postgres_insert_query, (12, 1500, 1))
    cursor.execute(postgres_insert_query, (200, 1600, 1))
    cursor.execute(postgres_insert_query, (40, 500, 2))
    cursor.execute(postgres_insert_query, (300, 550, 2))
    cursor.execute(postgres_insert_query, (500, 300, 3))
    cursor.execute(postgres_insert_query, (1000, 2000, 4))


insert_warehouse_material()
insert_warehouse_product()
insert_warehouse_productmaterial()
insert_warehouse_warehouse()
print('Success!')

