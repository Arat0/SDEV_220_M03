




#superclass vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
#sub class for vehicle 
class Automobile(Vehicle):
    def __init__(self,vehicle_type, year,make, model,doors,roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Get user input for automobile attributes
vehicle_type = input("Enter vehicle type (e.g., car, truck, plane, boat, broomstick): ")
year = input("Enter year: ")
make = input("Enter make: ")
model = input("Enter model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter type of roof (solid or sun roof): ")

# Create an instance of the Automobile class with user input
car = Automobile(vehicle_type, year, make, model, doors, roof)

# Print the details of the car
print("\nVehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)


    
    
    
    
 