import matplotlib.pyplot as plt

def display(x,y):
  plt.plot(x,y)
  plt.show()

def run():
  print("Running......")
  x_values = [1,2,3,4,5]
  y_values=[1,4,9,16,25]
  display(x_values,y_values)

run()


###########
###############


import matplotlib.pyplot as plt

def large():
  x = [1,1,6,6,1]
  y = [1,6,6,1,1]

  plt.plot(x,y,'b-p')
  
def small():
  x = [3,3,4,4,3]
  y = [3,4,4,3,3]
  plt.plot(x,y, 'r:o')

def medium():
  x = [2,2,5,5,2]
  y = [2,5,5,2,2]
  plt.plot(x,y, 'g--s')

  
large()
small()
medium()
plt.show()


##########################
########################


import matplotlib.pyplot as plt

def coordinate():
  print("please enter an 'x' value: ")
  x=int(input())

  print("please enter an 'y' value: ")
  y =  int(input())
  return (x,y)
  

def path():
  print("retreving path...")
  x_values = []
  y_values = []
  for count in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return [x_values,y_values]


def run():
  values = path()
  plt.plot(values[0], values[1], 'r--o')
  plt.show()
run()



