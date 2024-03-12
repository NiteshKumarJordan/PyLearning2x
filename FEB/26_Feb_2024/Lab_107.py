# Encapsulation

class MyClass:

    def __init__(self):  # private methods---variable name can't be accessed directly
        self.name = 'Amit'
        self.age = 29
        self.public_password = "1234567890"
        self.__private_password = "<PASSWORD>"
        self._protected_password = "Protected"

    def public_password1(self):
        print(self.public_password)

    def private_password1(self):
        print(self.__private_password)

    def protected_password1(self):
        print(self._protected_password)


prv = MyClass()

# not callable directly
# prv.public_password
# prv.private_password
# prv.protected_password
prv.private_password1()
prv.public_password1()
prv.protected_password1()
