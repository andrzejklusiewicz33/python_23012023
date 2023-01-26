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