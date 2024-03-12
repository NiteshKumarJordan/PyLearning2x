
a = int(input("enter the first no\n"))
b = int(input("enter the second no\n"))

try:
    c = a/b
    print("div is",c)

except Exception as e:
    print(e)

print("Zero can divide, pls ingnore")


