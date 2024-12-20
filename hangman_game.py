import random
import string
from words import words

# # Initialising all the variables:
# alphabets = string.ascii_uppercase  # List of all the alphabets in uppercase.
# user_guessed_letters = set()    # THe set of all the characters guessed by the user
# computer_chosen_word = random.choice(words).upper()     # The random word chosen by the computer
# lives = 5   # The number of wrong guesses allowed, after which the game terminates, and the player loses.
# displayed_word = []

# def main_game():

#     while lives > 0:
#         # print the chosen word as blank spaces and update when a correct letter is guessed by the user.
#         print("The word is: ",end='')
#         for letter in computer_chosen_word:
#             if letter in user_guessed_letters:
#                 print(displayed_word.append())
        
#         print()
#         # Print the used letters (user guessed letters)
#         print("You have already guessed: ", user_guessed_letters)

#         # To check if the guessed character is a letter, if it is; then was it already guessed; if not then add it to the set of guessed letters.
#         while True:
#             current_user_guess = input("Guess an alphabet: ").upper()

#             if current_user_guess not in alphabets:
#                 print("Invalid input. Please enter a correct alphabet.\n")
#             elif current_user_guess in user_guessed_letters:
#                 print("You already guessed this alphabet.\nGuess a different alphabet.\n")
#             else:
#                 user_guessed_letters.add(current_user_guess)
#                 break

        

# main_game()


def play_hangman_game():

    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|   Let's play a game of Hangman!                            |
|   Get Ready! Try to guess the word within 5 tries.         |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
          """)

    chosen_word = random.choice(words).upper()
    letters_in_chosen_word = set(chosen_word)
    guessed_letters = []

    alphabets_list = string.ascii_uppercase
    print(alphabets_list)
    lives = 5

    while len(letters_in_chosen_word) > 0 and lives > 0:
        
        displaying_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                displaying_word = displaying_word + letter + ' '
            else:
                displaying_word = displaying_word + '_ '

        # Another way to write the above code using 'ternary operations'.
        # displaying_word = displaying_word + (letter if letter in guessed_letters else '_ ' for letter in chosen_word)

        print("The word is: ", displaying_word)
        print("Alphabets you have used: ", ' '.join(guessed_letters[::-1]))
        print(f"Lives left: {lives}")
        guess = input("Guess a single alphabet: ").upper()

        if guess == "":
            print("INVALID INPUT. GUESS A SINGLE ALPHABET.\n")
        elif guess in alphabets_list:
            if guess in guessed_letters:
                print(f"'{guess}' HAS ALREADY BEEN USED'. TRY ANOTHER ALPHABET.")
            else:            
                if guess in letters_in_chosen_word:
                    letters_in_chosen_word.remove(guess)
                    print("CORRECT GUESS!")
                else:
                    print("WRONG GUESS. TRY AGAIN.")
                    lives -= 1
                guessed_letters.append(guess)
            print()    
        else:
            print("INVALID INPUT. GUESS A SINGLE ALPHABET.\n")

    if lives == 0:
        print(f"Lives left: {lives}")
        print(f"THE WORD WAS: {chosen_word}")
        print("BETTER LUCK NEXT TIME!")
    else:    
        print("CONGRATULATIONS! YOU GUESSED THE WORD:", chosen_word)
        print(f"THAT TOOK YOU {len(guessed_letters)} TRIES.")

play_hangman_game()