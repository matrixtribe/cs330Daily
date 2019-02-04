# ###################################################
# guessing game - CS330
# introduce game
# get player name
# get random number
# player has 7 chances to guess a number from 1-10
# player wins or loses
# ###################################################

import random


def main():
    # introduce game
    print("This is a single player guessing game.")
    print("You will have 7 tries to guess a number randomly picked between 1 and 10")

    # get player name
    player = input("What is your name? ").lower()

    # get random number
    number = random.randint(1, 10)

    # player has 7 chances to guess a number from 1-10
    turn = 1
    game = True
    guess_list = []
    while turn <= 7 and game:
        try:
            guess = int(input("What is your guess? "))
            # edge cases duplicate or outside range
            if guess < 0 or guess > 10 or guess in guess_list:
                print("Your guess was a duplicate or outside the acceptable range. Please try again.")
                print("Your guess/es: " + str(guess_list))
            else:
                # player wins or loses
                if guess == number:
                    print("Good job " + player + " you won in " + str(turn) + " guess/es!")
                    game = False
                elif turn == 7:
                    print("Sorry, that was your last guess :-/")
                    print("The correct number was " + str(number))
                    game = False
                else:
                    print("Incorrect guess.")
                    print("you have " + str(7-turn) + " guess/es remaining.")

                turn += 1
                guess_list.append(guess)
                print("Your guess/es: " + str(guess_list))
        except ValueError:
            game = False
            print("Please try again and enter only positive integers between 1 and 10.")

main()
