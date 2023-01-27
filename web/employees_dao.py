from domain import *
def get_all():
    data = []
    e1 = Employee(1, 'Andrzej', 'Klusiewicz', 12345, "programmer z zawodu i pasji")
    data.append(e1)
    e2 = Employee(2, 'Marian', 'Paździoch', 8000, "Programista Front-End")
    data.append(e2)
    e3 = Employee(3, 'Babka', 'Kiepska', 10000, "Babka dawaj rentę!")
    data.append(e3)
    return data
