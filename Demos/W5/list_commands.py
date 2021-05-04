#initialise and empty set

colours = set()
print(type(colours))

# initialise non empty set

colors = {"blue", "red", "yellow"}
print(type(colors))
print(colors)


# adding elements
colors.add("purple")
colours.add("red")
colours.add("green")
colours.add("black")

print(colours)z
print(colors)

# unuin - joining two sorted

set1 = colours.union(colors) # if you have set2 = {1,2,3,4,} add union(colors,set2)
print(set1)


# intersection = finding common elements
set2 = colours.intersection(colors)
print(set2)





#OTHER FUNCTION
def get_fruits():
  fruits = []
  print("how many items do you want to add")
  n = int(input())
  for i in range(n): # we can use [0,4] which is use 0 1 2 3 space or [1,5] which is use 1 2 3 4
    print("Type in the next fruit:")
    fruits.append(input())

  print("yout fruits are {}".format(fruits))


  #Print only few items by slicing

  print(f"sliced list: {fruits[0:5:2]}")

  #print only few items by using negative Index
  print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits() # need to call the function to run it
















