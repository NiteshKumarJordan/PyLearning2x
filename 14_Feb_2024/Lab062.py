# FACTORIAL PROGRAM USING FUNCTIONS --ASSIGNMNETS

# 5 factorial- 5*4*3*2*1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # 5*4*3*2*1


enter_number = int(input("Enter a number for factorial"))
Result = factorial(enter_number)
print(Result)




