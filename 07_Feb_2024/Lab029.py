# String concatenation
str1 = "Nitesh"
str2 = "Kumar"
str3 = "Jordan"
str4 = str1 + str2 + str3
print(str4)

# String + Integer = It will give you error(TypeError: can only concatenate str (not "int") to str)

name = "Nitesh"
age = 27

print(name + str(age))
# if we convert age into the string, then it will b possible to concat

# Increment and decrement operator
# ++, --

a = 10
a += 1
print(a)

x = 10
# y = ++x(Not allowed in Python)

y = x + 1
print("x of value of", y)
