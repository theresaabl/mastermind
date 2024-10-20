#mock terminal of 80 characters wide and 24 rows high
import random

class Game:
    """
    Create instance of Game
    """
    def __init__(self, colors = [f"{i}" for i in range(1, 7)], code_length = 4, max_attempts = 12):
        self.colors = colors
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.secret_code = self.create_code()
    
    def create_code(self):
        """
        Randomly choose {self.code_length} items from the colors list
        Create secret code as a string
        """
        code_array = random.choices(self.colors, k = self.code_length)
        code = "".join(code_array)
        return code
    
    def run_game(self):
        """
        Run game
        """
        print("\nMASTERMIND\n")
        print("Welcome to a game of Mastermind.\n")
        print(self.secret_code + "\n")
        # Create new guess
        latest_guess = Guess(self.secret_code)
        print(f"\nYou guessed: {latest_guess.guessed_code}\n")


class Guess:
    """
    Create instance of Guess
    """
    def __init__(self, secret):
        self.secret = secret
        self.guessed_code = self.take_guess()

    def take_guess(self):
        return input("Enter your guess as a 4-digit number: \n")


# Run game
game = Game()
game.run_game()


