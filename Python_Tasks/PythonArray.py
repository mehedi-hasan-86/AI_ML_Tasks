cars = ["Frod" ,"Volvo", "BMW"]

print(cars)


x = cars[0]
print(x)

cars[0] = "Toyta"
print(cars[0])

print(len(cars))

for x in cars:
    print(x)

cars.append("Honda")
for x in cars:
    print(x)

cars.pop(1)

cars.remove("Volvo")