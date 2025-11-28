from PythonFunction import my_function
from PythonIfStatement import number


def  my_funtion(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias","Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_funtion(*numbers):
    if len(numbers) ==0:
        return None
    max_num = number[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3,7,2,9))


def my_funtion(**myvar):
    print("Type: ", type(myvar))
    print("Name: ", myvar["name"])
    print("Age: ", myvar["age"])
    print("All data : ", myvar)

my_funtion(name = "Tobias", age = 30, city = "Bergen")




