import psycopg2
from domain import *
import settings

def get_all():
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute('select * from employees')
        data=[Employee(*w) for w in cursor]
        return data




def get_one(id):
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute(f"select * from employees where employee_id={id}")
        return Employee(*cursor.fetchone())

#
# def get_one(id):
#     with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
#         cursor=connection.cursor()
#         cursor.execute(f"select * from employees where employee_id={id}")
#         row=cursor.fetchone()
#         return Employee(*row)

#
# def get_one(id):
#     sql=f"select * from employees where employee_id={id}"
#     with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.username, password=settings.password) as connection:
#         cursor=connection.cursor()
#         cursor.execute(sql)
#         row=cursor.fetchone()
#         employee=Employee(*row)
#         return employee




#Employee.query.filter().all()
#SQLAlchemy
#Django ORM

# def get_all():
#     data = []
#     with psycopg2.connect(host="localhost",database="postgres",port=5432, user="aplikacja", password="oracle") as connection:
#         cursor=connection.cursor()
#         cursor.execute('select * from employees')
#         for w in cursor:
#             print(w)
#             data.append(Employee(*w))
#     return data

# def get_all():
#     data = []
#     with psycopg2.connect(host="localhost",database="postgres",port=5432, user="aplikacja", password="oracle") as connection:
#         cursor=connection.cursor()
#         cursor.execute('select * from employees')
#         for w in cursor:
#             print(w)
#             e=Employee(w[0],w[1],w[2],w[3],w[4])
#             data.append(e)
#     return data


# def get_all():
#     data = []
#     e1 = Employee(1, 'Andrzej', 'Klusiewicz', 12345, "programmer z zawodu i pasji")
#     data.append(e1)
#     e2 = Employee(2, 'Marian', 'Paździoch', 8000, "Programista Front-End")
#     data.append(e2)
#     e3 = Employee(3, 'Babka', 'Kiepska', 10000, "Babka dawaj rentę!")
#     data.append(e3)
#     return data
