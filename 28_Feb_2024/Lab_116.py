# Inheritance--- Hierarchical

class Vehicles:
    def info(self):
        print("This is a vehicle")


class Car(Vehicles):
    def info(self):
        print("This is a car")


class Bicycle(Vehicles):
    def info(self):
        print("This is a bicycle")


car = Car()
bicycle = Bicycle()

print(car.info())

