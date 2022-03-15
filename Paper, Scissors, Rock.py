import random
# Program Written by Thomas Wilson 15/03/2022


def full_check(choice_):
    if choice_.upper() == "P":
        full_choice = "Paper"
    elif choice_.upper() == "S":
        full_choice = "Scissors"
    elif choice_.upper() == "R":
        full_choice = "Rock"
    else:
        return "You hacker there is no way to get to this option without changing the code"
    return full_choice


# Main routine
print("Welcome to Paper, Scissors, Rock\n")
computer_choice_list = ["Paper", "Scissors", "Rock"]
name = input("What is your name: ")
computer_quote_win = [f"I knew someone with the name {name} couldn't stand a chance", f"Woah, {name} sucks to be you you just lost to a computer program\nHow bad does it feel?", f"I just memorized a new definition for the word {name}\nit means loser", f"At least you were better than the person before you, wait\nThere was nobody before you", f"Losers deserve nothing and you {name} are a loser", f"I WON {name.upper()} HAHA loser\n\nI really need some irl friends rn", "You seem like one of those kids who dropped out at kindergarten\nYou couldn't even beat a simple program"]
computer_quote_lose = [f"The only way you could of won is of changed the code", "You must of given me a virus for you to be able to win", f"Just kidding the win was obviously a prank\nIt was right\nSome sick prank", f"You {name} won fare and square and I accept your win\nNOPE\nYou cheated didn't you?", f"Wow I accept the win thank you {name} for willingly donating me 3 points\nI won yay\nI need to get a new life don't I", f"Congrats {name} you bet a ROBOT wow good on you", "You bet me\nA pre-programmed ROBOT or program whatever you want to call me :l"]
game_finished = False
computer_points = 0
player_points = 0
print(f"Welcome {name} to Paper, Scissors, Rock")
while game_finished is False:
    choice = input("(P): Paper   (S): Scissors   (R): Rock\nChoice: ")
    if choice.upper() == "P" or choice.upper() == "S" or choice.upper() == "R":
        full_choice_ = full_check(choice)
        computer_choice = random.choice(computer_choice_list)
        if full_choice_ == computer_choice:
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("It's a tie")
        elif full_choice_ == "Paper" and computer_choice == "Rock":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("You gained one point")
            player_points = player_points + 1
        elif full_choice_ == "Paper" and computer_choice == "Scissors":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("The computer gained one point")
            computer_points = computer_points + 1
        elif full_choice_ == "Scissors" and computer_choice == "Paper":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("You gained one point")
            player_points = player_points + 1
        elif full_choice_ == "Scissors" and computer_choice == "Rock":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("The computer gained one point")
            computer_points = computer_points + 1
        elif full_choice_ == "Rock" and computer_choice == "Paper":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("The computer gained one point")
            computer_points = computer_points + 1
        elif full_choice_ == "Rock" and computer_choice == "Scissors":
            print(f"You chose {full_choice_} and computer chose {computer_choice}")
            print("You gained one point")
            player_points = player_points + 1
        else:
            print(f"You chose a option that wasn't coded please report this to Thomas\nYou {full_choice_} Computer {computer_choice}")
        print(f"\nComputer: {computer_points}\nYou: {player_points}\n")
    else:
        print("Please choose a valid option")
    if computer_points > 2:
        print(f'Computer: " {random.choice(computer_quote_win)} "')
        game_finished = True
        exit("You lost")
    if player_points > 2:
        print(f'Computer: "{random.choice(computer_quote_lose)} "')
        game_finished = True
        exit("You won")
