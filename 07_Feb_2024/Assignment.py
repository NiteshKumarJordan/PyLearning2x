# Task #1
# Explain the difference between the = operator and the == operator in Python.
# What does the ** operator do in Python, and how is it used?
# What does the ^ operator do in Python, and in what context is it commonly used?

# Solution:- 1. = operator is used for assigning values to any variable whether its int or string & == operator is
# used to compare the values eg. a=10, b= 20 and a==b then it will return the result as false.
# 2. ** operator is used for Exponentiation as eg. 2 to power of 2 answer will be 4

# 3. ^ operator is bitwise operator i.e XOR Sets each bit to 1 if only one of two bits is 1 and it will compare both
#the digits eg. 2 ^ 2 if both numbers are same then result will be 0 based on the Truth table

# Task #2

# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie  as 3.14)
# Create a program that takes two numbers as input and prints whether the first number is greater than,  less than, or equal to the second number.
# Develop a Python script that calculates the square and cube of a given number.

# Area of circle
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
print("Area of circle:", area)

# compare the numbers
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if num1>num2:
    print("num1 is greater than num 2")
elif num1<num2:
    print("num1 is less than num 2")
elif num1 == num2:
    print("num1 is equal to num 2")

else:
    print("Something went wrong")

# Square and cube of a given number
#SQUARE
num = int(input("Enter the number for square: "))
print(num ** 2)

#CUBE
num2 = int(input("Enter the number for cube: "))
print(num2 ** 3)





