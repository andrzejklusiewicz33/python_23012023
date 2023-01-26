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
