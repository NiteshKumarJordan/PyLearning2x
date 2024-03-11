# Overloading

# Overloading conceptually not possible in Python


class MathUnit:
    def add(self,a, b=0, c=0):
        return a + b + c


math = MathUnit()
print(math.add(10, 20, 30))
print(math.add(10, 20))
print(math.add(10))
