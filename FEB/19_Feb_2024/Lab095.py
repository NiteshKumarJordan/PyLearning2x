class Person:
    name = None
    age = 0
    gender = None
    address = None

    def person_name(self):
        print("My name is", self.name)

    def person_age(self):
        print("My age is", self.age)

    def person_gender(self):
        print("My gender is", self.gender)

    def person_address(self, address):
        print("My address is", self.address)


p = Person()
p.name ="Rajesh"
print("My name is", p.name)
p.age= 29
print("My age is", p.age)
p.gender="Male"
print("My gender is", p.gender)
p.address = "Ranchi, Jharkhand"
print("My address is", p.address)

# p.person_name()
# p.person_age()
# p.person_gender()
# p.person_address()


