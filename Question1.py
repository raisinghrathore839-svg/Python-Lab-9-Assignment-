class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start(self):
        print("The car is starting.")

c = Car("Toyota", "Black")
c.start()
