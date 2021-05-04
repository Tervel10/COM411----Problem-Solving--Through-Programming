#THe function
def great_user():
  print("please enter your name")
  name = input()
  print("hello", name)

# Call the functuion
great_user()
great_user()
great_user()



#Asking for a sound
def listen():
  #ask user put a sound
  print("What sound did i hear")
  sound = input()
  
  # Dispay the message
  print("\n That was a loud", sound)

#Call the function
listen()





# other function by definition
def identify():
  print("what lies before us")
  response = input()
  
  if(response == "a large boulder"):
    print("it`s time to run")
  else:
    print("we will be fine")

identify()


#how to call function

def escape_by(plan):

  if (plan == "jumping over" ):
    print("We Cannot escape that way, the boulder is too big")
  elif(plan == "running around"):
    print("we cannot escape that way, the boulder is moving too fast")
  elif(plan == "going deeper"):
    print(" Thats moght work, lest go deeper")
  else:
    print("not sure about the plan")
  

  #calling the function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("lets listen")