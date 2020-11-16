import random

def difficulty(mode):
    lifes_and_numbers = {}
    li_nu = []
    mode = mode.lower()
    if mode == "easy" or mode == "medium" or mode == "hard":
        lifes_and_numbers["lifes"] = 7
        lifes_and_numbers["number_to_guess"] = random.randint(0,10)
        if mode == "medium":
            lifes_and_numbers["lifes"] = 5
            lifes_and_numbers["number_to_guess"] = random.randint(0,100)
        elif mode == "hard":
            lifes_and_numbers["lifes"] = 3
            lifes_and_numbers["number_to_guess"] = random.randint(0,1000)
    for v in lifes_and_numbers.values():
        li_nu.append(v)
    return li_nu

def hint(actual_number, your_number):
    if your_number > actual_number:
        return f"The number is below {your_number}."
    else:
        return f"The number is above {your_number}."

def game(mode):
    lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
    introduction = "-- Guess the number --"
    introduction += "\nPlease, enter your number: "
    play_again = "Do you want to play again? 'y/n' "
    choose_difficulty = "Wich difficulty do you want to play? (easy, medium, hard): "
    while lifes != 0:
        your_number = int(input(introduction))
        if number_to_guess != your_number:
            print(f"WRONG!!{hint(number_to_guess, your_number)}")
            lifes -= 1
            if lifes == 0:
                print("GAME OVER")
                play_again = (input(play_again))
                if play_again == "n":
                    lifes = 0
                else:
                    input(choose_difficulty)
                    lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
                    print(lifes, number_to_guess)
        else:
            print("Congrats!! You guessed the number")
            play_again = (input(play_again))
            if play_again == "n":
                lifes = 0
            else:
                input(choose_difficulty)
                lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
    return "Thanks for playing!!"

welcome = "Welcome to the game. "
welcome += "\nWich difficulty do you want to play? (easy, medium, hard): "
select_difficulty = input(welcome)

print(game(select_difficulty))