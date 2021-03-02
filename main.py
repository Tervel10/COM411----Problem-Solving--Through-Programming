<<<<<<< HEAD

print("How many times to print the symbol? ")

x= int(input()) 

# i is a counter - it keeps track of how many times we went through the loop
i = 0

while i < x: # condition for  repeating the code - as lonf as i lower than x
  print("\u27BD", i)
  i = i + 1 # new value of the counter is one more than it used to be 

print("We left the loop")
=======
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
>>>>>>> e281d8a912fb2fb95b0d2a2a2e57673fbba6eea9
