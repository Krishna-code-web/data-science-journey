# Create a Vehicle class with inheritance and method overriding.

# Define a base class Vehicle with attributes name, max_speed, and mileage. Create a child class Bus that inherits from Vehicle and implements a fare() method. The base fare is calculated as seating_capacity * 100. For a Bus, add a 10% maintenance charge to the total fare

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = 50 # by default
    
#     def fare(self):
#         return self.seating_capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         total_fare = super().fare()
#         return total_fare + (total_fare * 0.10)

# # Example Usage
# school_bus = Bus("School Volvo", 180, 12)
# print(f"Total Bus fare is: {school_bus.fare()}")
# # Output: Total Bus fare is: 5500.0
