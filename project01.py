"""
NOTE TO REVIEWER:
- I am aiming for an exceed grade.
- Please reject the project if it doesn't meet all the requirements for extra credit.
- Thank you so much for your time!
"""



import random

# This is the global variable to keep the highest score
high_score = None

# Main function for the game
def start_game():
    
    # Import global variable high_score
    global high_score
    
    # 1. Check if there's any exisiting high_score, if there is, print it.
    if high_score:
        print("")
        print("*" * 9, "THE CURRENT HIGHEST SCORE IS {}".format(high_score), "*" * 9, "\n")
        print("=" * 51)
        
    # Count: variable to keep track of number of attempts
    count = 0
    
    # Generate a random number for the answer
    answer = random.randint(1, 10)
    
    # Game begins
    while True:
        user_input = input("Your guess:\n")
        try:
            # Test if the user_input is a string or integer and raise ValueError if it is a string
            if test_for_string(user_input):
                raise ValueError("Please enter an integer between 1 and 10.")
                
            # Convert user_input into integer
            user_input = int(user_input)
            
            # Check if user_input is our of range (<1 or > 10) and raise a ValueError if it is
            if user_input < 1 or user_input > 10:
                raise ValueError("Your guess is out of range. Enter a number between 1 and 10.")
                
        # Process ValueError:
        except ValueError as err:
            print("Try again!")
            print("({})".format(err))
            
        # If no error, proceed to checking if user_input matches answer
        else:
            count += 1
            if user_input == answer:
                break
            elif user_input < answer:
                print("Your guess is lower than the answer.")
                print("-" * 12)
                continue
            else:
                print("Your guess is higher than the answer.")
                print("-" * 12)
                continue
    finish(count, answer)
    keep_score(count)
    play_again()
    

    
# Function to ask for user input if they want to play again
def play_again():
    print("Do you want to play again? [y]es/[n]o.\n")
    while True:
        user_res = input()
        # Check if user_res is valid, either "y" or "n"
        if user_res != "n" and user_res != "y":
            print("Please enter [y] or [n] only.")
            play_again()
        # If user wants to play again, print out high score and run start_game()
        else:
            print("=" * 51)
            if user_res == "y":
                start_game()
            elif user_res == "n":
                print("See you again!")
                break
            break
        break
    
    
    

# Function to test if argument is a string or integer
# Return True if it's a string, false otherwise
def test_for_string(x):
    num = "0123456789"
    for char in x:
        for digit in num:
            if digit == char:
                break
            else:
                continue
        else:
            return True
    return False
            
            

        
# Function to print out welcome text
def welcome():
    print("-" * 51)
    print("")
    print("*" * 7, "WELCOME TO THE NUMBER GUESSING GAME", "*" * 7)
    print("")
    print("~" * 23, " * ", "~" * 23)
    print("")

    
# Function to print out result of game, with number of attempts and correct answer
def finish(count, answer):
    print("Congratulations! You have guessed it correctly after {} tries.".format(count))
    print("The correct answer is {}.".format(count, answer))
    

# Function to update high_score
def keep_score(count):
    global high_score
    if high_score:
        if count < high_score:
            high_score = count
    else:
        high_score = count
    

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    welcome()
    start_game()