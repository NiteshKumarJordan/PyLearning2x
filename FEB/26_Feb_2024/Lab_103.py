# CONSTRUTOR

class Car:
    def __init__(self, name, color, brand, speed, engine):
        self.name = name
        self.color = color
        self.brand = brand
        self.speed = speed
        self.engine = engine

    def start_engine(self):
        print("starting engine with car", self.name)
        print("starting engine with brand", self.brand)
        print("starting engine with speed", self.speed)
        print("starting engine with engine", self.engine)
        print("starting engine with color", self.color)


l = Car("Land rover", "Rangerover", "360KM/per hour", "V4", "Red")

l.start_engine()

