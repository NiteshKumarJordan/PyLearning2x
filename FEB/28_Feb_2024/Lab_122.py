# Inheritance==Polymorphism

# Overridding

class Animal:
    def sound(self):
        print("Animal sound")


class Dog:
    def sound(self):
        print("Dog sound")


d = Dog()
print(d.sound())

a = Animal()
a.sound
print(a.sound())
