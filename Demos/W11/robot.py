from inhabitant import Inhabitant

class Robot(Inhabitant):

  laws = "Protect, Obey and Survive"
  
  @staticmethod
  def the_laws():
    print(Robot.laws)

  def __init__(self, name="Robot", age=0):
    super().__init__(name,age)

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}."

  def __repr__(self):
    return f"Robot(name = {self.name}, age = {self.age}, energy = {self.energy})"

  def display(self):
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  robot = Robot("Beep-o", 5)
  Robot.the_laws()
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))
  robot.eat(20)
  print(repr(robot))