
marker = False

name1 = input("Enter 1st player's name:")
name2 = input("Enter 2nd player's name:")

while marker == False:
    p1 = input("Enter your bet [(R)ROCK / (P)PAPER/ (S)SCISSORS]: ")
    p2 = input("Enter your bet [(R)ROCK / (P)PAPER/ (S)SCISSORS]: ")

    if p1.upper() == p2.upper():
        print("It's a Tie!!\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "R" and p2.upper() == "P":
        print(name2.upper() + " wins (Rock against Paper)\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "R" and p2.upper() == "S":
        print(name1.upper() + " wins (Rock against Scissors)\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "P" and p2.upper() == "R":
        print(name1.upper() +" wins (Paper against Rock)\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "P" and p2.upper() == "S":
        print(name2.upper() + " wins (Paper against Scissors)\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "S" and p2.upper() == "R":
        print(name2.upper() + " wins (Scissors against Rock)\n")
        ask = input("Want to play again? [Y / N]:")
    elif p1.upper() == "S" and p2.upper() == "P":
        print(name1.upper() + " wins (Scissors against Paper)\n")
        ask = input("Want to play again? [Y / N]:")
    else:
        print("Invalid Input!! You did not enter 'R' for Rock, 'S' for Scissors or 'P' for Paper!!")

    if ask.upper() == "Y":
        marker = False
    elif ask.upper() == "N":
        marker = True
    else:
        marker = True

print("Thank you for playing! ")