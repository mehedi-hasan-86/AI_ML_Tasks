#Demonstrates a functin with a positional argument

print("Hello, World")

#Demonstrates a function with a positional argument and a return value

name = input("What's your name  ?\n")
print("Hello, ")
print(name)

#Demonstrates concatenation of strings

name = input("What's your name? \n")
print("Hello, " + name)


#Demonstrates a function with two positional arguments

name = input("What's your name? ")
print("hello, ", name)

# Demonstrates a function with a positional argument and a named argument

name = input("What's your name? ")
print("Hello, ", end="")
print(name)

#Demonstrates a format string

name = input("What's your name? ")
print(f"hello, {name}")

#Demonstrates str functions

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {last}")

#Demonstrates addition 

x = 1
y = 2

z = x+y
print(z)

#Demonstrates (unintended) concatenation of strings

# Prompt user for two integers
#Demonstrates conversion from str to int
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = int(x)+int(y)
print(z)

#Demonstrates conversion of str to float
#Demonstrates rounding to nearest int
#Demonstrates fromating with commas
#demonstrates division
#Demonstrates formatting after the decimal place

m = float(input("What's m? "))
n = float(input("What's n? "))

o = round(m+n)
print(o)
print(round(m+n))
print(f"{o:,}")

b = round(m/n, 2)
print(b)
c = m/n
print(f"{c:2f}")


# Demonstrates defining a function without parameters

def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

#Demonstrates defining a function with a parameter

def hello(to):
    print("hello, ", to)

name = input("What's your name? ")
hello(name)

# Demonstrates defining a function with a parameter with a default value

def hello(to="world"):
    print("hello, ", to)

hello()
name = input("What's your name? ")
hello(name)

# Demonstrates defining a main function

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello, ", to)

main()

# Demonstrates defining a function with a return value

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()