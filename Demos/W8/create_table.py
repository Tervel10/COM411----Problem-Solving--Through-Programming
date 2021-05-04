import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)
plt.show()


######
#########

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)
plt.show()


##############
###########

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)


x = ["Poland", "Romania", "Bulgaria"]
y = [2,17,2]
y2 = [5,6,12]
y3 = [1,1,3]

axes[0,0].bar(x,y)
axes[0,1].pie(y2,labels = x)
axes[1,1].plot(x,y3)

plt.tight_layout()
plt.show()