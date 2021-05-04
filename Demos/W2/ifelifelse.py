print("What is your name")
n = input()
#print("Do you have a dog? (Type True or False)")
#dog = input()
#bool is boolean datatyoe - inly stores True/False

if len(n) > 9:
  print("You have a very looong name!")
  print("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print(" Your name is a bit long. consider a nickname")
elif len(n) < 3:
  print("youe name is veery short")
else:
  print("Your name is quite okay")
print("This is the end of the program")