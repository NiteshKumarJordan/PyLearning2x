# Try, except and finally


try:
    a = int(input("enter the number 1"))
    b = int(input("enter the number 2"))
    c = (print(a / b))

except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(a / b)

finally:
    print("finally")
