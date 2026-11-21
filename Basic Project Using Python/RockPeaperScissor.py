import random

l = ["rock", "scissor", "paper"]

while True:
    ccount = 0
    ucount = 0

    uc = int(input('''
Game Start....
1 Yes
2 No / Exit
Enter your choice: 
'''))

    if uc == 1:

        for a in range(1, 6):

            userInput = int(input('''
1 Rock
2 Scissor
3 Paper

Enter your choice:
'''))

            if userInput == 1:
                uchoice = "rock"

            elif userInput == 2:
                uchoice = "scissor"

            elif userInput == 3:
                uchoice = "paper"

            else:
                print("Invalid choice! Try again.")
                continue

            cchoice = random.choice(l)

            print("\nYour Choice:", uchoice)
            print("Computer Choice:", cchoice)

            if cchoice == uchoice:

                print("Game Draw")
                ucount += 1
                ccount += 1

            elif (uchoice == "rock" and cchoice == "scissor") or \
                 (uchoice == "paper" and cchoice == "rock") or \
                 (uchoice == "scissor" and cchoice == "paper"):

                print("You Win!")
                ucount += 1

            else:

                print("Computer Win!")
                ccount += 1

        print("\n----- Final Score -----")
        print("Your Score:", ucount)
        print("Computer Score:", ccount)

        if ucount > ccount:
            print("Congratulations! You Won the Game.")

        elif ccount > ucount:
            print("Computer Won the Game.")

        else:
            print("Match Draw!")

    elif uc == 2:
        print("Game Exit!")
        break

    else:
        print("Invalid Input! Please select 1 or 2.")
