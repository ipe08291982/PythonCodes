
marker = False
while marker == False:
    num = int(input("Enter a number: "))
    ans = num % 2

    if ans == 0:
        print("The number is even")
    else:
        print("The number is odd")

    ask = input("Do you want to try again? [Y/N]: ")

    if ask.upper() == "Y":
        marker = False
    else:
        marker = True