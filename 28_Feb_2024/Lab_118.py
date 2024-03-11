# Inheritance- Multiple Inheritance

class A:
    def methodA(self):
        return "This is a method in A"

    def home(self):
        return "This is a fathers home"


class B:
    def methodB(self):
        return "This is a method in B"

    def home(self):
        return "This is a Mothers home"


class C(A, B):
    def methodC(self):
        return "This is a method in C"


c = C()
print(c.home())
