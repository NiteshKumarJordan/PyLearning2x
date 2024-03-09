# Encapsulation

# we can use Private and Protected methods to hide the data members
# only public variavles should be allowed to access outside the class.

class Car:
    name = ''
    password = ''

    def __init__(self):
        self.name = "name_Jordan"
        self.__password = "password@123"
        self.public_var = "public"
        self.__private_var = "private"
        self.__protected_var = "protected"



    def printName(self):
        print("Nitesh password is ", self.__password)

c = Car()
print(c.name)
print(c.password)
c.printName()
