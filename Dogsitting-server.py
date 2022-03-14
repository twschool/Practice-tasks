import time
# Program Written by Thomas Wilson 14/03/2022
day_cost = 22.50
print("Welcome to the dog sitting service")
time.sleep(2)
looping = True
dog_list = ["Dog", "Boy", "Doggy", "Charlie", "Fluffy"]
while looping:
    days = 0
    dog_amount = 0
    bad_answer = False
    choice = input(f"Would you like to\n(a): Drop off a dog\n(b): Pick up a dog\n(c): List all staying dogs\n(d): Calculate staying costs\n(e): Exit the program\nResponse: ").lower()
    if choice == "a":
        dogs_name = input("Name of dog to drop off:\n")
        dog_list.append(dogs_name.title())
    elif choice == "b":
        dogs_name = input("Name of dog to pick up:\n").title()
        if dogs_name in dog_list:
            dog_list.remove(dogs_name)
            print("Dog has been picked up and removed from the system")
        else:
            print("Dog's name not found in system\nPlease check the list of dog's in the start menu using option (c)")
    elif choice == "c":
        for item in range(len(dog_list)):
            print(dog_list[item])
    elif choice == "d":
        print(f"{day_cost} per dog per day")
        try:
            dog_amount = float(input("How many dogs will be staying:\n"))
        except ValueError:
            bad_answer = True
            print("Invalid answer: Please provide a number")
        try:
            days = float(input("How many days will your dog(s) be staying:\n"))
        except ValueError:
            bad_answer = True
            print("Invalid answer: Please provide a number")
        if bad_answer:
            print("Due to one or more invalid answers the total could not be calculated")
            time.sleep(3.5)
        elif not bad_answer:
            dog_amount = (dog_amount, 0)
            print(f"The total for {dog_amount:.0f} dog(s) for {days:.0f} days\n= {days * day_cost * dog_amount:.2f}")
            time.sleep(3.5)
    elif choice == "e":
        print("Exiting program")
        looping = False
    else:
        print("Please select a valid option")
    if choice != "e":
        print("\nReturning to main menu\n")
    time.sleep(1)
