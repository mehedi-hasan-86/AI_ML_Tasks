print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello World"
print(a[1])

for x in "banna":
    print(x)

    print(len(a))

    txt = "The best things ini life are free!"
    print("free" in txt)

    if "free" in txt:
        print("YES, 'free' is present")

        print("expensive" not in txt)

        if "expensive" not in txt:
            print("No, 'expensive' is NOT present")


b = "Hello, World"
print(b[2:5])
print(b[:5])
print(b[5:])
print(b[-5:-2])

print((a.upper()))
print(a.lower())

a = " Hello, World "
print(a.strip())

print(a.replace("H","J"))

print((a.split(",")))

age = 21
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)

txt = f"the price is {50*20} dollars"
print(txt)