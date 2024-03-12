# Inheritance--- Hierarchical

class GrandParents:
    def home(self):
        print("This is a vehicle")


class Father(GrandParents):
    def home(self):
        print("This is a car")


class Brother(GrandParents):
    def home(self):
        print("This is a bicycle")


h = Father()
print(h.home())