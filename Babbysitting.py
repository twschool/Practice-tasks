import time
# Program Written by Thomas Wilson 15/03/2022
print("Welcome to the babysitting program")
loop = True
inputs_1 = 0
inputs_2 = 0
age_1 = 0
age_2 = 0
while loop:
    temp_age_1 = 0
    temp_age_2 = 0
    bad_answer = False
    print("Which program is your child attending?\n(1): Fun in the Sun\n(2): Active Kids\n(X): Exit and view average")
    program = input("Response: ")
    if program == "1":
        print("You have selected Fun in the Sun program")
        try:
            temp_age_1 = int(input("Age: "))
        except ValueError:
            bad_answer = True
            print("Please enter a number next time")
        if bad_answer is not True:
            inputs_1 = inputs_1 + 1
    elif program == "2":
        print("You have selected Active Kids program")
        try:
            temp_age_2 = int(input("Age: "))
        except ValueError:
            bad_answer = True
            print("Please enter a number next time")
        if bad_answer is not True:
            inputs_2 = inputs_2 + 1
    elif program.upper() == "X":
        print("You have selected exit program")
        if inputs_1 > 0 and age_1 > 0:
            print(f"Fun in the sun program\nAverage for {inputs_1} kids =\n {age_1 / inputs_1:.0f}")
        if inputs_2 > 0 and age_2 > 0:
            print(f"\n\nActive kids program\nAverage for {inputs_2} kids =\n {age_2 / inputs_2:.0f}")
        loop = False
    else:
        print("Not a valid option")
        temp_age = 0
    if bad_answer is False:
        age_1 = age_1 + temp_age_1
        age_2 = age_2 + temp_age_2
    elif bad_answer is True:
        print("Due to one or more invalid answers we\ncould not add any ages to the average")
    time.sleep(2)
print("Program exited")
