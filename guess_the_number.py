import random

def difficulty(mode):
    lifes_and_numbers = []
    mode = mode.lower()
    while mode != "easy" or mode != "medium" or mode != "hard":
        if mode == "easy" or mode == "medium" or mode == "hard":
            lifes_and_numbers = [7, random.randint(0,10)]
            if mode == "medium":
                lifes_and_numbers = [5, random.randint(0,100)]
            elif mode == "hard":
                lifes_and_numbers = [3, random.randint(0,1000)]
            return lifes_and_numbers
        print(f"{mode} is not a valid difficulty.")
        mode = input("Please enter a valid difficulty (easy, medium, hard): ")

def hint(actual_number, your_number):
    if your_number > actual_number:
        return f"The number is below {your_number}."
    else:
        return f"The number is above {your_number}."

def continue_game(prompt):
    if prompt == "n":
        lifes, l = 0, 0
        return lifes, l
    else:
        choose_difficulty = input("Wich difficulty do you want to play? (easy, medium, hard): ")
        ln = difficulty(choose_difficulty)
        return ln

def game(mode):
    results = difficulty(mode)
    lifes, number_to_guess = results[0], results[1]
    while lifes != 0:
        your_number = int(input("-- Guess the number -- \nPlease, enter your number: "))
        if number_to_guess != your_number:
            print(f"WRONG!! {hint(number_to_guess, your_number)}")
            lifes -= 1
            if lifes == 0:
                play_again = (input("~GAME OVER~ \nDo you want to play again? 'y/n' "))
                results = continue_game(play_again)
                lifes, number_to_guess = results[0], results[1]
        else:
            play_again = (input("Congrats!! You guessed the number \nDo you want to play again? 'y/n' "))
            results = continue_game(play_again)
            lifes, number_to_guess = results[0], results[1]
    return "Thanks for playing!!"

welcome = "Welcome to the game. "
welcome += "\nWich difficulty do you want to play? (easy, medium, hard): "
select_difficulty = input(welcome)

print(game(select_difficulty))