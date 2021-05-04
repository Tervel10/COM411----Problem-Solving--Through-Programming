dict1 = {}

dict2 = {"name":"Piotr", "age": 26, "alergy": ["coffee", "hard working"]}

dict2["siblings"] = 2

print(dict2["alergy"][0])
print(dict2)

menu = {1:"Start", 2:"Find Planet", 3:"Enter new Planet"}

print(menu[int(input("enter 1, 2 or 3:\n "))])

print(menu[2])