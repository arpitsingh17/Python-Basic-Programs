class Vehicle:
    def __init__(self,parking_spots = [], license_plate = "",spots_needed = 0, vehicle_size = 0):
        self.parking_spots = parking_spots
        self.license_plate = license_plate
        self.spots_needed = spots_needed
        self.vehicle_size = vehicle_size

class Bus(Vehicle):
    def __init__(self):
        self.spots_needed = 5
        self.vehicle_size = 2

class Car(Vehicle):
     def __init__(self):
        self.spots_needed = 2
        self.vehicle_size = 1

class Bike(Vehicle):
     def __init__(self):
        self.spots_needed = 1
        self.vehicle_size = 0

class parkingLot:
    def __init__(self,vehicle,spot_size=0,spot_number=0):
        self.vehicle = vehicle
        self.spot_size = spot_size
        self.spot_number = spot_number

    def isAvailable(self,spotnumber):
        if self.vehicle == None:
            return "Available"







print Bus().spots_needed
print Bus().vehicle_size

