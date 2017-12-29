class Vehicle :
    def __init__(self, VIN, weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacurer = manufacurer
    def GetWeight(self):
        return self.weight
    def GetManufacturer(self):
        return self.manufacurer
    def VehicleType(self):
        pass


class Car(Vehicle):
    def __init__ (self, VIN, weight, manufacturer):
        super().__init__( seats, VIN, weight, manufacturer)
        self.seats = seats

g = Car(1, 2, 3, 4)
print (g.vin_number) 