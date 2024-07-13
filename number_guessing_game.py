from random import randint

lower, upper = 1, 10
random_no = randint(lower,upper)


def start():
    chance = 3            
    while chance > 0:
        try:
            print(chance," chances left")
            guess = int(input("\nGuess the no "))
        except ValueError as e:
            print("Enter valid no\n")
            continue
        chance -= 1
        if guess == random_no:
            print("You guessed the number\n")
            return
        elif guess < random_no:
            print("Your no is smaller\n")
        else:
            print("Your no is larger\n")
            

    if chance == 0:
        print("Try again")

start()
