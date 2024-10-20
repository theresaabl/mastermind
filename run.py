#mock terminal of 80 characters wide and 24 rows high
import random
from pprint import pprint

class Game:
    """
    Create instance of Game
    """
    def __init__(self, colors = [f"{i}" for i in range(1, 7)], code_length = 4, max_rounds = 4):
        self.colors = colors
        self.code_length = code_length
        self.max_rounds = max_rounds
        self.secret_code = self.create_code()
    
    def create_code(self):
        """
        Randomly choose {self.code_length} items from the colors list
        Create secret code as a string
        """
        code_array = random.choices(self.colors, k = self.code_length)
        code = "".join(code_array)
        return code
    
    def game_won(self, score):
        if score[0] == self.code_length:
            print("\nYOU WON!\n")
            return True
        else:
            return False

    def check_max_rounds(self, attempts):
        if attempts == self.max_rounds:
            print("\nYou have run out of attempts.\n")
            return True
        else:
            return False 
    
    def welcome_message(self):
        print("\nMASTERMIND\n")
        print(f"Welcome to a game of Mastermind. ... Instructions ... You have {self.max_rounds} attempts.\n")
        # Give description of secret code, generalised to colors list consisting of numbers or alphabetic characters
        print(f"The secret code consists of {self.code_length} {'digits' if self.colors[0].isnumeric() else 'characters'}.\n")
        print(f"For testing: secret code: {self.secret_code}\n")

    def run_game(self):
        """
        Run game
        """
        attempts = 1
        self.welcome_message()
        # Create board
        board = Board(self.code_length)
        # game loop
        while True:
            print(f"\nRound {attempts}:\n")
            # Create new guess, pass secret code and colors list to be able to check guess against secret
            latest_guess = Guess(self.secret_code, self.colors)
            print(f"\nYou guessed: {latest_guess.guessed_code}\n")
            # Check guess against secret and save score
            latest_score = latest_guess.score
            print(f"You have {latest_score[0]} hits and {latest_score[1]} close.\n")
            # Show board
            board.append_guess(latest_guess)
            board.show()

            # check break conditions
            if self.game_won(latest_score):
                break
            if self.check_max_rounds(attempts):
                break
            else:
                # increment attempts
                attempts += 1
        
class Board:
    """
    Create instance of Board
    """
    def __init__(self, size):
        self.size = size        
    
    guess_list = []

    def append_guess(self, guess):
        self.guess_list.append([guess.guessed_code, guess.score])
    
    def show(self):
        pprint(self.guess_list)
    

class Guess:
    """
    Create instance of Guess
    """
    def __init__(self, secret, colors):
        self.secret = secret
        self.colors = colors
        self.guessed_code = self.take_guess()
        self.score = self.check_guess()

    def take_guess(self):
        """
        Take a guess from the user and check for valid input
        if guess is of correct length and contains only valid characters return it
        """
        while True:

            guess = input(f"Enter your guess: \n")

            # Check that guess has correct length
            if len(guess) != len(self.secret):
                print(f"\nYour guess '{guess}' is not the right length.\n")
                continue
            
            # Check that guess only contains valid characters according to colors list
            characters_valid = True
            for char in guess:
                if char.lower() not in [color.lower() for color in self.colors]:
                    # Compare lowercase strings so that it works for general colors list in Game class, which can contain letters   
                    print(f"\nYour guess '{guess}' contains invalid characters.\n")
                    characters_valid = False
                    break
            
            if characters_valid == True:
                break

        return guess
    
    def check_guess(self):
        """
        Check guess against the secret code and return number of hits and close
        Hit means correct character and position in the code
        Close means correct character but wrong position in the code
        """
        hits = 0
        close = 0
        secret_checked = self.secret
        guess_checked = self.guessed_code
        # check for hits
        for i, char in enumerate(self.guessed_code):
            # When character is at correct position increment hits
            if char == self.secret[i]:
                hits += 1
                # remove hits from guess so don't count twice
                guess_checked = guess_checked.replace(char, "", 1)
                # replace checked character in secret by . so don't count twice
                secret_checked = secret_checked[:i] + "." + secret_checked[i + 1:]
        # check for close
        for char in guess_checked:
            if char in secret_checked:
                close += 1
                # replace checked character in secret by . so don't count twice
                secret_checked =  secret_checked.replace(char, ".", 1)
        return [hits, close]

        


# Run game
game = Game()
game.run_game()


