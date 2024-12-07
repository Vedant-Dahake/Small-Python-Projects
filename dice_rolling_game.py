import random


def play_game() -> tuple:
    # dice_values = [1, 2, 3, 4, 5, 6]
    while True:
        choice = input("Roll the dice? (y/n): ").lower()
        
        if choice == 'y':
            # print((random.choice(dice_values), random.choice(dice_values)))
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f'({die1}, {die2})')
        elif choice == 'n':
            print("Thanks for playing!")
            print("Game Exited!\n")
            break
        else:
            print("Invalid Choice.")
    
print("Play game with rolling only 2 dice.")
play_game()




# Modification where user specifies no. of dices rolled. Not necessarily 2. And also has a counts how many times the dice are rolled.
def play_game_with_numerous_dice():
    counter = 0
    no_of_dice = int(input("Enter no. of dice: "))
    while True:
        choice = input("Roll the dice? (y/n): ").lower()
        
        dice_values = []

        if choice == 'y':
            for i in range(no_of_dice):
                dice_values.append(random.randint(1,6))
            print(tuple(dice_values))
            counter += 1
        elif choice == 'n':
            print("No. of times dice were rolled: ", counter)
            print("Thanks for playing!\nGame Exited.\n")
            break
        else:
            print("Invalid choice.")

print("Play game with numerous dice:")
play_game_with_numerous_dice()