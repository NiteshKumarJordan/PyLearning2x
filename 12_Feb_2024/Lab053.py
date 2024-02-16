# Functions
# Blocks of code that will help to execute some tasks.
# 1. Built in functions
# function need to be:
# 1. defined f(n)
# 2. call a f(n)

import math

results = max(2, 3)
print(results)

num = input("Enter the number")
print(num)

result = math.factorial(num)
print(result)


# Non return type of function
def greet():
    print("greetings")

# calling a function required here
greet()


# 3. User defined functions
# def square(num):
#     return num ** 2
#
#
# def cube(num):
#     return num ** 3
