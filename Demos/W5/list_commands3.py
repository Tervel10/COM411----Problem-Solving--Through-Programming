def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Turn Left", 3, "Turn Left", 1]
  return path

def run():
  print("Moving....")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")
  print("stop")

run()





# another list
all_students = [("Gary", 67), ("Uzma", 82), ("Mihai",76)]
print(all_students[1][1])
