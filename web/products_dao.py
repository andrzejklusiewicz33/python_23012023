from domain import *
import psycopg2
import settings
def get_all():
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute('select * from products')
        data=[Product(*w) for w in cursor]
        return data

def get_one(id):
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute(f"select * from products where product_id={id}")
        return Product(*cursor.fetchone())

def save(product):
    sql=f"insert into products(product_name,price,description,stock) values ('{product.product_name}',{product.price},'{product.description}',{product.stock})"
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute(sql)
        connection.commit()

def delete(id):
    with psycopg2.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'delete from products where product_id={id}')
        connection.commit()

# def get_all():
#     data = []
#     data.append(Product(1, "Bulbulator", 1234, "Urządzenie robiące bul bul", 10))
#     data.append(Product(2, "Przyczłap do bulbulatora", 100, "Takie teges co wiesz, no ten to tam", 0))
#     data.append((Product(3, "Wihajster z dzyndzlem", 20, "Na śróbki lub na gwoździe, zależy czy tak czy nie", 50)))
#     return data