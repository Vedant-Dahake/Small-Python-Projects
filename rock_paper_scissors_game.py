import random

def play_rock_paper_scissors():
    options = ('r', 'p', 's')
    emojis = {
                'r' : '🥌',
                'p' : '📃',
                's' : '✂'
             }


    while True:
        user_choice = input("Choose - Rock, Paper, or Scissors?  (r/p/s): ").lower()
        if user_choice not in options:
            print("Invalid choice.")
            continue

        computer_choice = random.choice(options)
        print(f'Your choice: {emojis[user_choice]}\n    v/s\nComputers Choice: {emojis[computer_choice]}')
        
        if user_choice == 'r':
            if computer_choice == 's':
                print("You win!")
            elif computer_choice == 'p':
                print("Computer Wins!")
            else:
                print("It is a draw.")
        elif user_choice == 'p':
            if computer_choice == 'r':
                print("You win!")
            elif computer_choice == 's':
                print("Computer Wins!")
            else:
                print("It is a draw.")
        elif user_choice == 's':
            if computer_choice == 'r':
                print("Computer wins!")
            elif computer_choice == 'p':
                print("You win!")
            else:
                print("It is a draw.")
        else:
            print("Invalid input!")


        # if user_choice == computer_choice:
        #     print("Tie!")
        # elif (
        #     (user_choice == 'r' and computer_choice == 's') or
        #     (user_choice == 'p' and computer_choice == 'r') or
        #     (user_choice == 's' and computer_choice == 'p')):
        #     print("You Win!")
        # else:
        #     print("Computer Wins. Better Luck Next Time!")

        quit = input("Continue? Enter 'n' to exit: ").lower()
        if quit=='n':
            print("Thanks for playing!")
            print("Exited!")
            break


play_rock_paper_scissors()