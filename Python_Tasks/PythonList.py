mylist = ["apple", "banna", "cherry"]
print(mylist)
print(len(mylist))

list1 = [1,2,3,4,5]
list2 = [True, False, False]
list3 = ["abc", 34, True,"male"]
print(list3)

print(type(mylist))

thisList = list(("apple","banna", "cherry"))
print(thisList)


thisList[1] ="blackcurrant"
print(thisList)


thisList = ["apple", "banna","banna", "cherry","banna", "apple"]
thisList.remove("banna")
print(thisList)
thisList.pop(1)
print(thisList)
thisList.pop()
print(thisList)
del thisList[0]
print(thisList)
# del thisList full list are deleted
thisList.clear()
print(thisList)
#
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x :
        newlist.append(x)

        print(newlist)


        fruits.sort()
        print(fruits)


thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thisList)
# thislist.sort()
# print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


list1 = ["a", "b","c"]
list2 = [1,2,3]
list3 = list1+ list2
print(list3)


list1 = ["a","b","c"]
list2 = [1,2,3]

for x in list2 :
    list1.append(x)

    print(list1)

list1.extend(list2)
print(list1)
