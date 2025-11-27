from PythonList import fruits

fruits = ["apple", "banna", "cherry"]
for x in fruits:
    print(x)


for x in "banna":
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banna":
     break


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)