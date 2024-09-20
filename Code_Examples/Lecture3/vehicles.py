class Vehicle:

    max_speed = 100 # Field with a default value

    # Special initialization function
    def __init__(self, velocity = 0, heading = 0, position = [0, 0, 0]):
        self.velocity = velocity # Setting up default fields
        self.heading = heading
        self.position = position

    # Methods
    def turn(self, heading):
        self.heading += heading

    def move(self, position):
        self.position[0] += position[0]
        self.position[1] += position[1]
        self.position[2] += position[2]
    
    def gas(self):
        if self.velocity != self.max_speed:
            self.velocity += 5

# Class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, velocity = 0, heading = [0, 0, 0], position = [0, 0, 0]):
        super().__init__(velocity, heading, position) # calling __init__ of the parent class
        self.max_speed = 150

    def open_trunk(self):
        print("Opened trunk")

    def close_trunk(self):
        print("Closed trunk")

class Truck(Vehicle):
    parcels = []

    def load_parcels(self, parcels):
        self.parcels.extend(parcels)
        print("Loaded parcels: " + str(parcels))

    def unload_parcel(self):
        p = self.parcels.pop()
        print("Unloaded parcel: " + str(p))
        return p

car = Car(position=[1,2,3]) # An instance of car
truck = Truck()

car.open_trunk()
car.close_trunk()
car.gas()

truck.turn(10)
truck.move([8, 3, 5])

truck.load_parcels(["book1", "book2", "book3"])
truck.unload_parcel()

print("Car velocity is " + str(car.velocity))
print("Truck heading angle is " + str(truck.heading))
print("Truck position is " + str(truck.position))