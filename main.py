print("What is your name")
n = input()
print("Do you have a dog? (Type True or False)")
dog = input()
#bool is boolean datatyoe - inly stores True/False

if len(n) > 9 and dog == "True":
  print("You have a very looong name!")
  print("Your name contains {} letters".format(len(n)))
else:
  print("Your name is quite okay")
print("This is the end of the program")