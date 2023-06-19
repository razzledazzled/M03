class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Accept user input for a car
vehicle_type = "car"

year = input("Enter the year of the car: ")
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
doors = input("Enter the number of doors (2 or 4) of the car: ")
roof = input("Enter the type of roof (solid or sun roof) of the car: ")

# Create an instance of the Automobile class with the user input data
car = Automobile(vehicle_type, year, make, model, doors, roof)

# Output the data in an easy-to-read format
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
