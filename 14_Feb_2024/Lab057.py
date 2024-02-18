# # FUNCTIONS
# # BLOCK OF CODES
# # They can return something------
# # They can't return something - Non return types
#
# # They have parameters
# # They don't have parameters
#
# Non return type/non parameter/no arguments
def say_hello():
    print("Hello")


say_hello()


#
#
# # non return type/ parameter/arguments
#
def say_hello(name):
    print("Hello " + name)


say_hello("Nitesh")


#
#
# # non return type/ more than one parameter/
#
def say_hello(name, age):
    print("Hello " + name + " " + str(age))


say_hello("Rajesh", 29)


# function with default arguments
def say_hello(name="Shaktimaan"):
    print("Hello " + name)


say_hello()


# # function with return type
def calculator(a, b, c, d):
    sum = a + b + c + d
    sub = a - b
    mul = a * b * c * d
    div = a / b
    return sum, sub, mul, div


result = calculator(10, 20, 30, 40)

print(result)
