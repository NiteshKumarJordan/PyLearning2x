# Inheritance

class GrandFather:
    def Grand_Parents_method(self):
        return "Grand Parents Method"


class Father(GrandFather):
    def Father_method(self):
        return "Father Method"


class Son(Father):
    def Son_method(self):
        return "Son Method"


son1 = Son()
print(son1.Grand_Parents_method())
print(son1.Father_method())
print(son1.Son_method())
