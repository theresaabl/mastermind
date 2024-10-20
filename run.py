#mock terminal of 80 characters wide and 24 rows high

class Game:
    def __init__(self, colors = [f"{i}" for i in range(1, 7)], code_length = 4, max_attempts = 12):
        self.colors = colors
        self.code_length = code_length
        self.max_attempts = max_attempts
    
    def run_game(self):
        print("\nMASTERMIND\n")
        print("Welcome to a game of Mastermind.\n")


# Run game
game = Game()
game.run_game()
