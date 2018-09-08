import random
import math

def prints_greeting():
    """Prints introductory greeting"""
    print "Can you beat the computer at it's own game? I will pick a random number and you will try to guess it before you run out of turns!"

    
def get_player_name():
    """Stores player name"""
    return raw_input("Hi! What is your name? > ")


def ask_to_play(player_name):
    """Asks player if they want to play"""
    play_game = raw_input("Ok, {}! Would you like to challenge me? Enter y to start game or n to exit. > ".format(player_name)).lower()
    if play_game == 'exit' or play_game == 'no' or play_game == "n":
        print "Ok, bye {}!".format(player_name)
        
        return False

    return True


def get_range():
    """Get's user preference for range"""
    while True:
        try:
            return int(raw_input("I will pick a random number between zero and whatever number you tell me.  Enter your choice > "))
        except ValueError:
            print "That isn't a valid range."
            continue


def set_secret_num(num_range):
    """Generates a random number"""
    return random.randrange(0, (num_range + 1))
    

def get_player_guess():
    """Asks user for guess"""
    while True:
        try:
            return int(raw_input("Enter your guess! > "))
        except ValueError:
            print "uh-oh, I don't think that's a valid number. Try again."
            continue


def compare_guess_to_secret_number(player_guess, secret_number, player_name):
    """Evaluates player guess against the randomly generated secret number. Evaluates whether the user won, and if not, informs them if the secret number is higher or lower than their gues"""
    if player_guess < secret_number:
        print "Your guess was {}. The secret number is HIGHER than that.".format(str(player_guess))
        
    elif player_guess > secret_number:
        print "Your guess was {}.  The secret number is LOWER than that.".format(str(player_guess))
     
    elif player_guess == secret_number:
        print "Corect! You win!"
        print "Let's play again."
        
        return True


def create_list_of_guesses(lst, player_guess):
    """Creates a list to capture player's guess history, adds an entry every time a user guesses"""
    lst.append(player_guess)
    
    return lst


def compare_difference_current_and_previous_guess(player_guess, previous_guess, secret_number):
    """Compares the absolute difference between player's current guess and the secret number to the difference between the player's previous guess and the secret number. 
        Informs them if their current guess is closer or farther away from the secret than their previous guess."""
    if (abs(player_guess - secret_number)) > (abs(previous_guess - secret_number)):
        print "Getting colder!"
    elif (abs(player_guess - secret_number)) < (abs(previous_guess - secret_number)):
        print "Getting hotter!"


def decrease_chances(chances):
    """Decreases the amount of turns left to the player"""
    chances -=1
    print "You have {} guesses left!".format(str(chances))
    return chances


def run_game():
    """Main loop"""
    prints_greeting()
    player_name = get_player_name()
    
    while ask_to_play(player_name): 
        """start of single round loop"""
        player_guesses_list = []
        num_range = get_range()
        chances = int(math.ceil(math.log(num_range, 2)))
        print "I have chosen a random number between 0 and {}! You will have {} chances to guess it.".format(str(num_range), str(chances))
        secret_number = set_secret_num(num_range)
        # print secret_number ##for testing
        
        while chances > 0:
            player_guess = get_player_guess()
            if compare_guess_to_secret_number(player_guess, secret_number, player_name) == True:
                break
            
            if player_guess in player_guesses_list:
                print "You have guessed that before. Please try again."

            else:
                chances = decrease_chances(chances)

                if len(player_guesses_list) >= 1:
                    previous_guess = player_guesses_list[-1]
                    compare_difference_current_and_previous_guess(player_guess, previous_guess, secret_number)
                
                create_list_of_guesses(player_guesses_list, player_guess)
            print "You guessed {} previously.".format(player_guesses_list)
        
        
        if chances == 0:
            print "Sorry, {}...you ran out of guesses!".format(player_name)
            print "The number was {}".format(str(secret_number))
            print "Try again with a new number!"



run_game()
    
    
