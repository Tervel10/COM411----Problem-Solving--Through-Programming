from inhabitant import Inhabitant

class Alien(Inhabitant):
  
  def __init__(self, name = "ET", age = 0):

    self.technology = []
    super().__init__(name, age)

  def pickup(self, tech):
    self.technology.append(tech)

  def drop(self, tech):
    self.technology.remove(tech)


if __name__ == "__main__":
  et = Alien()

  print(et)