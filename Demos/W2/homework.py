# input data and output data


print("whats your name human")
name = input()

print("How old are you")
age = int(input())

print("How tall you are")
height = float(input())

print("whats your weight")
weight = int(input())


print("Your name is \n"  , name)
print("your age is \n" , age)
print("your height is\n " , height)
print("your weight is\n" , weight)
print("{} you are {} years old and your bmi is {}.".format(name,age,weight / (height**2)))




#biger or smaller nummber
print("first number is")
first_number = int(input())
print("second number is ")
second_number = int(input())


if (first_number > second_number):
    print("First is bigger!")
else:
    print("First is equal or smaller!")

print("Done!")


#declare variable
print("Please enter activity to be performer")
activity = input()
if (activity == "calculate"):
  print("performing clculation")
print("activity complete")


#lerning beep to paint
print("Please enter activity to be performer")
paint = input()
if (paint == "up"):
  print("I am painting in the upward direction!")
elif (paint == "down"):
  print("I am painting in the down direction!")
elif (paint == "left"):
  print("I am painting in the left direction!")
elif (paint == "right"):
  print("I am painting in the righy direction!")
print("activity complete")


#even or odd numbers

print("enter the number")
num = int(input())
if (num %2 == 0):
  print("even")
else:
  print("is odd")



  #again


  
num = int(input("Enter a number: "))
if (num % 2) == 0:
  print("{0} is Even number". format(num))
else:
  print("{0} is Odd number". format(num)) 



  # calculate addition of 1 to 100 all together

  print("Calculating the sum of first hundred numbers")

summation = 0
i = 1

while(i<=100):
  summation = summation + i #  add value of i into summation --- also work    summation    i = i + 1
  i += 1

print(f"Done the answer is {summation}")