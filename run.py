
#class Game:
    #def __init__(self, ):
        
    
def instructions():
    """Print instructions to user on how to play the game."""
    print("Can you find the code guarding the secret message?")
    print("It is a 4 digit code with numbers between 1 and 6, no duplications.\n")
    print("You have 10 tries before the message will self-desctruct.\n")
    print("   ! indicates one correct number, placed correct.\n")
    print("   * indicates one correct number, placed wrong.\n")
    print("Good Luck and Hurry Up!\n")
    print("__________________________________________________\n")


def get_username():
    """Asks user for username, validates user input"""
    
    while True:
        username = input("Please enter your name: \n").strip()
        if username != "":
            print(f"\nAha {username}! You want to know the secret message. Let's get started!\n")
            break
        else:
            print("You can't keep it a secret! Please enter your name:")


def guess():
    """Asks user to enter 4 digits, validates for numbers and no duplication."""

    while True:
        user_input = input("Please enter a 4 digit code: ")
        # Validates digits and no other characters
        if not user_input.isdigit():
            print("No, no, no! Digits only!")
        # Validates 4 digits
        elif len(user_input) != 4:
            print("No, no, no! 4 digits please!")
        # Validates duplication
        elif user_input.has_duplication(user_input) == True:
            print("No, no, no! No duplications!")   
        # Prints guess and increments number for each new guess
        else:
            print(f"Guess 1: {user_input}\n")
            break

 def has_duplication(code):
    """Checks for duplication in code"""

    entered_numbers = set()
    for digit in code:
        if digit in entered_numbers:
            return True
            entered_numbers.add(digit)
    return False
        
def main():
    #instructions()
    #get_username()
    guess()

main()

#def end_game():

#def track_score():
