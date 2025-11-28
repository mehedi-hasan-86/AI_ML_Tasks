from pyexpat.errors import messages


def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1-32)*5/9
print(celsius1)

temp1 = 100
celsius1 = (temp1-32)*5/9
print(celsius1)

temp1 = 50
celsius1 = (temp1-32)*5/9
print(celsius1)

temp1 = 150
celsius1 = (temp1-32)*5/9
print(celsius1)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)
print(get_greeting())


def my_function(fname):
    print(fname+ " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_funtion(name):
    print("Hello",name)

my_funtion("Emil")


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Mehedi","Hasan")


# def my_funtion(name = "firend"):
#     print("Hello", name)
#
# my_funtion("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")



def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Bangladesh")


def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + " s name is ", name)

my_function(animal = "dog", name = "Buddy")


def my_function(animal, name):
    print("I have a ", animal)
    print("My", animal + " s name is ", name)

my_function("dog", "Buddy")



def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banna", "cherry"]
my_funtion(my_fruits)


# def my_funtion(person):
#     print("Name: ", person["name"])
#     print("Age: ", person["age"])
#
#     my_person = {"name" :"Emil", "age": 25}
#     my_function(my_person)



def my_function(x,y):
        return x+y
result =  my_function(5,3)
print(result)



def my_funtion():
    return ["apple", "banna", "cherry"]

fruits = my_funtion()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_funtion():
    return  (10,20)
x,y = my_funtion()
print("x: ", x)
print("y: ", y)


def my_funtion(name, /):
    print("Hello", name)

my_funtion("Emil")


def my_funtion(name):
    print("Hello", name)

my_funtion(name = "Emil")

# def my_funtion(name,/):
#     print("Hello", name)
#
# my_funtion(name = "Emil")

# def my_funtion(*, name):
#     print("Hello", name)
#
# my_funtion("Emil")


def my_funtion(a,b,/,*,c,d):
    return  a+b+c+d
result = my_function(5,10,c = 15, d = 20)
print(result)




