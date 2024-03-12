# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

num = int(input("enter the number"))
if num >= 90 and num <= 100:
    print(" Grade is A")
elif num >= 80 and num <= 89:
    print(" grade is B")
elif num >= 70 and num <= 79:
    print(" Grade is C")
elif num >= 60 and num <= 69:
    print(" Grade is D")
elif num >= 50 and num <= 59:
    print(" Grade is E")

else:
    print("Fail")
