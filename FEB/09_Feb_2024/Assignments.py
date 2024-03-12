#TASK 1 :- Leap Year Question
# Create a program that determines whether a given year is a leap year.
#
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
#
#
# Input = 2024
# Output = Leap year
year = int(input("Year"))
if year % 4 ==0 and year % 100 != 0 or year % 400 ==0:
    print("Leap year")

else:
    print("Not a leap year")


#TASK 2-- triangle question
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

side1 = float(input("Enter the first number \n"))
side2 = float(input("Enter the second number \n "))
side3 = float(input("Enter the third number \n"))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")

else:
    print("Scalene triangle")



