class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


bike1 = Bike("Yamaha R15", "Blue")
bike3 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha FZ", "Red")
print(bike2)
print(str(bike1))

print(bike1 == bike3)
