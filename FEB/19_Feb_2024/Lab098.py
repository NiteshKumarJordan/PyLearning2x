# CALCULATOR

class Calculatior:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


a = Calculatior()
print(a.sum(10, 20))
print(a.sub(10, 20))
print(a.mul(10, 20))
print(a.div(10, 20))
