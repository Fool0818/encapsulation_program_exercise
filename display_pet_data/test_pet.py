from pet import Pet

my_pet = Pet()

print("===================================")
print("          PET PROFILE MAKER        ")
print("===================================")

name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's type ex. Dog, Cat, Bird: ")
age = input("Enter your pet's age: ")

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\n===================================")
print("          PET INFORMATION          ")
print("===================================")
print("Pet Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Pet Age:", my_pet.get_age(), "year/s old")
print("-----------------------------------")
print("Your pet profile has been created successfully!")
print("===================================")