#The class i.e blueprint for my objects
class Person:
  #Class attribute -> constant, visible to all objects of the class
  MAX_ENERGY = 100 # if something wont be changed use large latters
  # Initialiser (special instance method, invoked only once at creation)
  def __init__(self, name, age = 0, weight = 8, energy = 100):
    self.name = name
    self.age = age
    self.weight = weight
    if energy > 100:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy

  def hello(self):
    print(f"Hello my name is {self.name}. Im {self.age} years old and I weight {self.weight}kg. nice to meet you !")

  def grow(self):
    self.age += 2

  def eat(self, food, weight):
    self.weight += weight
    print(f"{self.name}  have eaten {food} and now weight is {self.weight}")

if __name__ == "__main__":
  Piotr = Person("Piotr", 66, 81, 65)
  Anca = Person("Anca", 18) 
  Mihai = Person("Mihai")
  Tim = Person("Tim", weight = 87)


# print(f"The age of Piotr is {Piotr.age}, where as the age of Anca is {Anca.age}, with Tim being {Tim.age} years old ")
  Anca.hello()
  Tim.hello()
  Mihai.hello()
  Piotr.hello()

  Anca.grow()
  Mihai.grow()

  Tim.eat("lasagne", 2)