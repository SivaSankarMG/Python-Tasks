from random import choice

def start():

    print("Welcome to game!! Enter \"exit\" to stop")

    valid = [ "stone", "paper", "scissor" ]

    while True:

        ai = choice(valid)
        user = input("Stone Paper Scissor : ").lower()

        if user == "exit":
            return

        if user not in valid:
            print("Invalid move")
            continue

        print("User ",user, "\nAI ",ai)
        print()

        if user == ai:
            print("Tie")
        elif user == "stone" and ai == "paper":
            print("You won")
        elif user == "stone" and ai == "scissor":
            print("You won")
        elif user == "scissor" and ai == "paper":
            print("You won")
        elif user == "paper" and ai == "stone":
            print("You won")
        else:
            print("AI won")
        

start()
        
