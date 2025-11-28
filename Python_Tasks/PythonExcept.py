from typing import final

x = 10/0
try:
    print(x)
except:
    print("An exception orrured")


    try:
        print(x)
    except NameError:
        print("Varialbe x is not defined")
    except:
        print("Something else went wrong")



try:
    print("Hello")
except:
    print("Somethins went wrong")
else:
    print("Nothing went wrong")


try :
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except :
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


x = -1
if x<0:
    raise Exception("Sorry, no number below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

