import random

def difficulty(mode):
    lifes_numbers = {}
    test = []
    if mode == "easy" or mode == "medium" or mode == "hard":
        lifes_numbers["lifes"] = 7
        lifes_numbers["number_to_guess"] = random.randint(0,10)
        if mode == "medium":
            lifes_numbers["lifes"] = 5
            lifes_numbers["number_to_guess"] = random.randint(0,100)
        elif mode == "hard":
            lifes_numbers["lifes"] = 3
            lifes_numbers["number_to_guess"] = random.randint(0,1000)
    for v in lifes_numbers.values():
        test.append(v)
    return test

def hint(actual_number, your_number):
    if your_number > actual_number:
        return f"The number is below {your_number}."
    else:
        return f"The number is above {your_number}."

def game(mode):
    lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
    print(lifes, number_to_guess)
    text_0 = "-- Guess the number --"
    text_0 += "\nPlease, enter your number: "
    want_continue = "Do you want to play again? 'y/n' "
    play_again = "Wich difficulty do you want to play? (easy, medium, hard): "
    while lifes != 0:
        your_number = int(input(text_0))
        if number_to_guess != your_number:
            print(f"WRONG!!{hint(number_to_guess, your_number)}")
            lifes -= 1
            if lifes == 0:
                print("GAME OVER")
                want_continue = (input(want_continue))
                if want_continue == "n":
                    lifes = 0
                else:
                    play_again = input(play_again)
                    difficulty(mode)
                    lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
        else:
            print("Nice, you guessed the number")
            want_continue = (input(want_continue))
            if want_continue == "n":
                lifes = 0
            else:
                play_again = input(play_again)
                difficulty(mode)
                lifes, number_to_guess = difficulty(mode)[0], difficulty(mode)[1]
    return "Thanks for playing!!"

welcome = "Welcome to the game. "
welcome += "\nWich difficulty do you want to play? (easy, medium, hard): "
choose_difficulty = input(welcome)

print(game(choose_difficulty))