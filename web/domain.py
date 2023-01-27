class Fruit:
    name="Banana"
    color="yellow"
    def serialize(self):
        return  {
            "name":self.name,
            "color":self.color
        }

class Author:
    first_name="Andrew"
    last_name="Klusiewicz"
    email="klusiewicz@jsystems.pl"
    def serialize(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email
        }

class Employee:
    def __init__(self,employee_id,first_name,last_name, salary, description):
        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.description=description

    def __str__(self):
        return str(self.__dict__)