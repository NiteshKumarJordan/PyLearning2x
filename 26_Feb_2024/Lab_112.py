# Multilevel Inheritance

class GrandFather:
    def Home1(self):
        print("Home 1")

    def LuxuryCar(self):
            print("Luxury Car-BMW")

    def LaandProperty(self):
            print("Laand Property-10 acres")


class Father(GrandFather):
    def Home2(self):
        print("Home 2")


class Son(Father):
    def Home3(self):
        print("Home 3")

son = Son()
son.Home1()
son.Home2()
son.Home3()
son.LuxuryCar()
son.LaandProperty()
