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

print(colours)
print(colors)

# unuin - joining two sorted

set1 = colours.union(colors) # if you have set2 = {1,2,3,4,} add union(colors,set2)
print(set1)


# intersection = finding common elements
set2 = colours.intersection(colors)
print(set2)