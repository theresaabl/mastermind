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
        # Create new guess, pass secret code and colors list to be able to check guess against secret
        latest_guess = Guess(self.secret_code, self.colors)
        print(f"\nYou guessed: {latest_guess.guessed_code}\n")


class Guess:
    """
    Create instance of Guess
    """
    def __init__(self, secret, colors):
        self.secret = secret
        self.colors = colors
        self.guessed_code = self.take_guess()

    def take_guess(self):
        """
        Take a guess from the user and check for valid input
        if guess is of correct length and contains only valid characters return it
        """

        while True:

            guess = input(f"Enter your guess as a {len(self.secret)}-digit number: \n")

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
        Check guess against the secret code
        """
        return
        


# Run game
game = Game()
game.run_game()


