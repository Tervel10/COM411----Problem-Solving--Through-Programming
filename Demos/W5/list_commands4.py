def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Left"]
  return directions

def menu():
  print("Please select a direction:")
  dirs = directions()

  for index in  range(len(dirs)):
    
    print("{}: {}".format(index, dirs[index]))
    index = int(input())
  return dirs[index]

def run():
  route =[]
  print("workin out escape route..")
  for count in range(5):
    route.append(menu())
  print(f"Escape route: {route}")
run()







# aditional list
def generate_stds():
  print("Enter the name :")
  name = input()
  print("Enter the grate: ")
  grade = input()
  return name, grade



t = generate_stds()
print(t)

