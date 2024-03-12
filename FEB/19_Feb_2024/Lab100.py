class Car:
    color = None
    model = None
    year = None

    def car_details(self):
        print(self.color, self.model, self.year)

car_color = input("Enter car color")
car_model = input("Enter car model")
car_year = int(input("Enter car year"))

car1 = Car()
car1.color = car_color
car1.model = car_model
car1.year = car_year

car1.car_details()

