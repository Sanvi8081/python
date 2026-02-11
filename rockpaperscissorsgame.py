import random

print("WINNING RULES OF THE GAME ARE:\n"
      + "Rock VS Paper -> Paper Wins.\n"
      + "Rock VS Scissors -> Rock Wins.\n"
      + "Paper VS Scissors -> Scissors Wins.\n")

while True:

    print("Enter the choice:\n"
          + "1.Rock\n" + "2.Paper\n" + "3.Scissors\n")

    choice = int(input("Enter your choice: "))

    # Validate input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please: "))

    # Assign user choice name
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determine winner
    if choice == comp_choice:
        print("<== It's a tie! ==>")

    elif (choice == 1 and comp_choice == 2) or \
         (choice == 2 and comp_choice == 3) or \
         (choice == 3 and comp_choice == 1):
        print("<== Computer wins! ==>")

    else:
        print("<== User wins! ==>")

    # Play again?
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

print("Thanks for playing!")


