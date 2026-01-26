import argparse

parser =  argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# import sys
# if len(sys.argv) == 1:
#     print("Meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in  range(n):
#         print("meow")
# else:
#     print("usage: mewos.py")

# def meow(n: int) -> Str:
#     """"
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line 
#     :rtype: str
#     """
#     return "meow\n" *n
#     # for _ in range(n):
#     #     print("meow")



# number:int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end = "")
# meow(number)

# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat  = Cat()
# cat.meow()

# MEOWS = 3

# MEOWS = 4
# for _ in range(MEOWS):
#     print("meow")
