import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [10,15.5,18.2,20,25,36,40]

plt.xlabel("age")
plt.ylabel("score")

plt.plot(x,y,"gD-")

plt.show()


############
#############

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,10.5]
y = [10,15.5,18.2,20,25,36,40,40.7]

plt.xlabel("age")
plt.ylabel("height")

plt.step(x,y,"gD-")

plt.show()



########
#############

import matplotlib.pyplot as plt

x = ["Baby","Toddler","Teen","Aduld"]
y = [10,15.5,18.2,20]

plt.xlabel("age")
plt.ylabel("height")

plt.bar(x,y, color = ["m", "g", "r", "b"])
plt.plot(x,y)

plt.show()

########
#######

import matplotlib.pyplot as plt

x = ("Lithuania", "Romania", "Poland", "Bangladesh", "Brazil", "Columbia", "Others")

data = [2,17,1,2,2,2,6]

plt.pie(data, labels = x)

plt.show()

#######
#######

import matplotlib.pyplot as plt

x = ("Lithuania", "Romania", "Poland", "Bangladesh", "Brazil", "Columbia", "Others")

data = [2,17,1,2,2,2,6]

plt.pie(data, labels = x, explode = [0.1,0.2,0.3,0.4,0.5,0.6,0.4])

plt.show()