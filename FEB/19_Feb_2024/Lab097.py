# Anagram String
# Count vowels and constants in String
# Find a substring in a string

class Car:
    name= None
    color= None
    brand = None
    speed = None
    engine = None


    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

    def drive(self):
        print("Driving")

    def who_is_driving(self):
        print("i am driving", self.name)

tesla_obj_ref = Car()
tesla_obj_ref.name = "tesla"

tesla_obj_ref.color = "blue"

tesla_obj_ref.brand = "tesla"
tesla_obj_ref.speed = 200
tesla_obj_ref.engine = 100

tesla_obj_ref.who_is_driving()
print(tesla_obj_ref.color)
