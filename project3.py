# =====================================
# Airline Reservation System
# Inheritance + Polymorphism
# =====================================

# Parent Class
class Ticket:

    def __init__(self, passenger_name, flight_no, source, destination):
        self.passenger_name = passenger_name
        self.flight_no = flight_no
        self.source = source
        self.destination = destination

    def calculate_price(self):
        return 0

    def display_ticket(self):
        print("\n========== TICKET ==========")
        print("Passenger  :", self.passenger_name)
        print("Flight No  :", self.flight_no)
        print("From       :", self.source)
        print("To         :", self.destination)


# Child Class
class Economy(Ticket):

    def calculate_price(self):
        return 300


# Child Class
class Business(Ticket):

    def calculate_price(self):
        return 600


# Child Class
class FirstClass(Ticket):

    def calculate_price(self):
        return 1000


# ============================
# Main Program
# ============================

print("================================")
print(" Airline Reservation System")
print("================================")

name = input("Passenger Name: ")
flight = input("Flight Number: ")
source = input("Departure City: ")
destination = input("Arrival City: ")

print("\nSelect Ticket Class")
print("1. Economy")
print("2. Business")
print("3. First Class")

choice = int(input("Enter Choice: "))

if choice == 1:
    ticket = Economy(name, flight, source, destination)

elif choice == 2:
    ticket = Business(name, flight, source, destination)

elif choice == 3:
    ticket = FirstClass(name, flight, source, destination)

else:
    print("Invalid Choice")
    exit()

# Polymorphism
ticket.display_ticket()
price = ticket.calculate_price()

print("Ticket Type :", ticket.__class__.__name__)
print("Price       : $", price)
print("\nTicket Booked Successfully!")