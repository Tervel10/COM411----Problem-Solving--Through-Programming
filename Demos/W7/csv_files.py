import csv

lista = []

with open("fold1/fold2/data.csv") as d:
  reader = csv.reader(d,delimiter = ",", quotechar = "'")
  #for row in reader:
  #  print(row)

  for row in reader:
    lista.append(row)

print(lista)