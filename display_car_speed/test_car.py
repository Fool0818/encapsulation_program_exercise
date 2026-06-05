from car import Car

my_car = Car(2024, "Toyota")

print("===================================")
print("        CAR SPEED SIMULATION       ")
print("===================================")
print("Car Model Year:", my_car.get_year_model())
print("Car Make:", my_car.get_make())
print("Starting Speed:", my_car.get_speed(), "km/h")
print("-----------------------------------")

print("\nStarting acceleration...\n")

for i in range(5):
    my_car.accelerate()
    print("Acceleration", i + 1, "-> Current Speed:", my_car.get_speed(), "km/h")

print("\nThe car is now moving faster!")
print("-----------------------------------")

print("\nNow applying the brakes...\n")

for i in range(5):
    my_car.brake()
    print("Brake", i + 1, "-> Current Speed:", my_car.get_speed(), "km/h")

print("\n-----------------------------------")
print("The car has completely stopped.")
print("Final Speed:", my_car.get_speed(), "km/h")
print("===================================")