def calculate_area(h = 10,b = 5):
  area = 0.5*h*b
  return area

def run():
  x =calculate_area(4,5)
  x += 1
  print(f"The area of triangle is {x}")


run()