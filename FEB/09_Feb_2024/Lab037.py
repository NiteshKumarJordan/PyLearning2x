# EXERISES
# 1. Find tha max between 3 numbers:-

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

# max_num = max(num1, num2, num3)
# print("the max number is:",max_num)

# Using normal
if num1 > num2 and num1 > num3:
    print("max is first:",num1)

elif num2 > num3 and num2 > num1:
    print("max is second :",num2)

else:
    print("max is 3rd ",num3)
