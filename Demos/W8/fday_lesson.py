import matplotlib.pyplot as plt

x = [0,2,4,6,8,10,12]
y = [0,20,40,60,80,100,-20]

plt.xlabel("hight value")
plt.ylabel("y value")
plt.plot(x,y,"*")
plt.bar(x,y)
plt.show()
