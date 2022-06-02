import random

# ROCK PAPER SCISSORS CLI GAME

options = ["R", "P", "S"]


def start_game():
    print("Rock Paper Scissors Game Enjoy!!!")
    player1 = 0
    player2 = 0

    # make player1 choose from options
    player1_choice = random.choice(options)

    def check():
        player2_choices = input("Select R or P or S: ")
        while player2_choices != "R" or player2_choices != "S" or player2_choices != "P":
            do = player2_choices.upper()
            player2_choices = do
            if do == "R" or do == "S" or do == "P":
                print(do)
                break
            else:
                player2_choices = input("please select only 'R' or 'P' or 'S': ")
        return player2_choices

    player2_choice = check()

    while player1_choice == player2_choice:
        if player1_choice == "R" and player2_choice == "S":
            player1 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        elif player1_choice == "S" and player2_choice == "P":
            player1 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        elif player1_choice == "P" and player2_choice == "R":
            player1 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        elif player2_choice == "R" and player1_choice == "S":
            player2 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        elif player2_choice == "S" and player1_choice == "P":
            player2 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        elif player2_choice == "P" and player1_choice == "R":
            player2 += 1
            print("You" + "(" + player2_choice + ") : " + "Computer" + "(" + player1_choice + ")")
            break
        else:
            print("it's a tie")
            check()

    if player1 > player2:
        return "computer wins"
    elif player2 > player1:
        return "You win"


print(start_game())
