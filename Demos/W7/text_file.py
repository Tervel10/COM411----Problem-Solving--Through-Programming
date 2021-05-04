name = input ("Enter file name")

name += ".txt"


f1 = open("john.txt")
f2 = open("harry.txt")

for i in range(3):
  print(f"\033[92mJohn: {f1.readline()}\033[0m ", end = "")
  print(f"\033[96mHarry: {f2.readline()}\033[0m ", end = "")
  
f1.close()
f2.close()