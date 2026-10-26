# pr 7: Vehicle Rental System
class Vehicle:
    def __init__(self, name, model, rent):
        self.name = name
        self.model = model
        self.rent = rent

    def calculate_rent(self, days):
        return self.rent * days

vehicles = [
    Vehicle("Car", "Swift Dzire", 2000),
    Vehicle("Bike", "Royal Enfield Classic 350", 500),
    Vehicle("Van", "Maruti Eeco", 3000)
]
print("--- Sagarsuman Manjhi ---")
print("Vehicle Rental System")

for i, v in enumerate(vehicles, 1):
    print(f"{i}. {v.name} - {v.model} - Rs. {v.rent}/day")

choice = int(input("Choose vehicle (1-3): "))
days = int(input("Enter rental days: "))

if 1 <= choice <= len(vehicles) and days > 0:
    vehicle = vehicles[choice - 1]
    total = vehicle.calculate_rent(days)

    print("\n--- RENTAL DETAILS ---")
    print("Vehicle:", vehicle.name)
    print("Model:", vehicle.model)
    print("Rental Days:", days)
    print("Daily Rent: Rs.", vehicle.rent)
    print("Total Rent: Rs.", total)
else:
    print("Invalid choice or rental days")

""" 
# Example 1: Class and Object

class Vehicle:
    def display(self):
        print("Welcome to Vehicle Rental System")

v = Vehicle()
v.display()


# Example 2: Constructor

class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Vehicle:", self.name)
        print("Rent per day: Rs.", self.price)

v = Vehicle("Car", 2000)
v.display()


# Example 3: Vehicle Rental

class Vehicle:
    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

    def calculate_rent(self, days):
        return self.rent * days

car = Vehicle("Car", 2000)
bike = Vehicle("Bike", 500)

print("Car Rent:", car.calculate_rent(3))
print("Bike Rent:", bike.calculate_rent(3))


# Example 4: Inheritance

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()


# Example 5: Encapsulation

class Vehicle:
    def __init__(self, rent):
        self.__rent = rent

    def get_rent(self):
        return self.__rent

    def set_rent(self, rent):
        if rent > 0:
            self.__rent = rent

v = Vehicle(1500)

print("Rent:", v.get_rent())
v.set_rent(2000)
print("Updated Rent:", v.get_rent())


# Example 7: Method Overriding

class Vehicle:
    def rent(self):
        return 1000

class Car(Vehicle):
    def rent(self):
        return 2000

class Bike(Vehicle):
    def rent(self):
        return 500

print("Car Rent:", Car().rent())
print("Bike Rent:", Bike().rent())
 """