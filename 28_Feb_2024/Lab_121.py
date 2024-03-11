# Inheritance---- Hybrid

class A:
    def methodA(self):
        print("This is method A")

class B(A):
    def methodB(self):
        print("This is method B")

class C(A):
    def methodC(self):
        print("This is method C")

class D(B, C):
    def methodD(self):
        print("This is method D")


d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()

