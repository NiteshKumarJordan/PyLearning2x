# OOps

class Person():
    name = None
    age = 0
    gender = None
    address = None

    def person_name(self):
        print("My name is", self.name)

    def person_age(self):
        print("My age is", self.age)

a = Person()
a.name = "Rajesh"
a.age = 29
print("My name is", a.name)
print("My age is", a.age)