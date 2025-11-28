mytuple = ("apple", "banna", "cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


mytuple = ("apple", "banna", "cherry")

for x in mytuple:
    print(x)


mystr = "banna"
for x in mystr:
    print(x)