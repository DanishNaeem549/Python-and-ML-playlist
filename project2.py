# ==============================
# Ride Booking System
# Inheritance & Polymorphism
# ==============================

# Parent Class
class Ride:
    def __init__(self, rider_name, pickup, destination, distance):
        self.rider_name = rider_name
        self.pickup = pickup
        self.destination = destination
        self.distance = distance

    def calculate_fare(self):
        return 0

    def show_details(self):
        print("\n========== Ride Details ==========")
        print("Rider Name :", self.rider_name)
        print("Pickup     :", self.pickup)
        print("Destination:", self.destination)
        print("Distance   :", self.distance, "km")


# -----------------------------------
# Child Class - Bike Ride
# -----------------------------------
class BikeRide(Ride):

    def calculate_fare(self):
        return self.distance * 2


# -----------------------------------
# Child Class - Car Ride
# -----------------------------------
class CarRide(Ride):

    def calculate_fare(self):
        return self.distance * 5


# -----------------------------------
# Child Class - Luxury Ride
# -----------------------------------
class LuxuryRide(Ride):

    def calculate_fare(self):
        return self.distance * 10


# ==============================
# Main Program
# ==============================

print("===================================")
print("      Ride Booking Application")
print("===================================")

rider = input("Enter Rider Name: ")
pickup = input("Enter Pickup Location: ")
destination = input("Enter Destination: ")
distance = float(input("Enter Distance (km): "))

print("\nSelect Ride Type")
print("1. Bike")
print("2. Car")
print("3. Luxury")

choice = int(input("Enter Choice: "))

if choice == 1:
    ride = BikeRide(rider, pickup, destination, distance)

elif choice == 2:
    ride = CarRide(rider, pickup, destination, distance)

elif choice == 3:
    ride = LuxuryRide(rider, pickup, destination, distance)

else:
    print("Invalid Choice")
    exit()

# ==============================
# Polymorphism
# ==============================

ride.show_details()
fare = ride.calculate_fare()

print("Ride Type  :", ride.__class__.__name__)
print("Total Fare : $", fare)

print("\nBooking Confirmed!")
print("Thank you for choosing our Ride Service.")