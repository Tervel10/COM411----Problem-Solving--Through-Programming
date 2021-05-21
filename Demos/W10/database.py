from person import Person # take a information and functions from person.py file

class Database:
  def __init__(self):
    self.name = "Piort`s Database"
    self.people = []
    self.suspended = []

  def add_person(self, person):
    self.people.append(person)

  def display_all(self):
    for person in self.people:
      person.hello()

  def all_eat(self, food, weight):
    for person in self.people:
      person.eat(food, weight)

db = Database()
Daniel = Person("Daniel", 26,77)
Reluca = Person("Reluca", 23, 48, 99)

Piotr = Person("Piotr")
Ivan = Person("Ivan", 42, 150)

db.add_person(Daniel)
db.add_person(Reluca)
db.add_person(Ivan)
db.add_person(Piotr)

db.display_all()
print()
db.all_eat("Lasagne", 3)
print()
db.display_all()