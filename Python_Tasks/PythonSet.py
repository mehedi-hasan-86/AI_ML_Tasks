myset = {"apple", "banna","cherry","apple", True, 1,2}

print(myset)

print(len(myset))

myset = {False,0}
print(myset)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}



set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

  thisset.add("orange")

  print(thisset)

  thisset = {"apple", "banana", "cherry"}
  tropical = {"pineapple", "mango", "papaya"}

  thisset.update(tropical)

  print(thisset)

  thisset = {"apple", "banana", "cherry"}

  for x in thisset:
      print(x)