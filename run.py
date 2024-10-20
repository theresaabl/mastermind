#mock terminal of 80 characters wide and 24 rows high
import random

class Game:
    def __init__(self, colors = [f"{i}" for i in range(1, 7)], code_length = 4, max_attempts = 12):
        self.colors = colors
        self.code_length = code_length
        self.max_attempts = max_attempts
    
    def create_code(self):
        code_array = random.choices(self.colors, k = 4)
        code = "".join(code_array)
        return code
    
    def run_game(self):
        print("\nMASTERMIND\n")
        print("Welcome to a game of Mastermind.\n")
        secret_code = self.create_code()
        print(secret_code+"\n")


# Run game
game = Game()
game.run_game()
