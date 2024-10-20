# mock terminal of 80 characters wide and 24 rows high
import random
from tabulate import tabulate


class GameMenu:
    """
    Create instance of GameMenu
    """
    def __init__(self):
        pass

    def show_menu(self):
        """
        Print the menu choices
        """
        print("\nMASTERMIND\n")
        print("Menu\n")
        print("1 - Play Game\n")
        print("2 - Show Instructions\n")
        print("3 - Exit\n")

    def take_choice(self):
        """
        Take user input menu choice, validate it
        and return it if valid
        """
        while True:
            choice = input("Choose from options 1 - 3: \n").strip()

            # Check that choice is not empty
            if len(choice) == 0:
                print("\nYour choice is empty.\n")
                continue

            # Check that choice is numeric and of length 1
            if len(choice) != 1 or choice not in "123":
                print(f"\nYour choice '{choice}' is not valid.\n")
                continue

            # If choice is valid, break
            break

        return choice

    def show_instructions(self):
        """
        Show game instructions until user presses key
        """
        print("\nInstructions to write ...\n")
        input("Press enter to continue\n")

    def handle_menu_choice(self, menu_choice):
        """
        Check which option user chose and call functions accordingly
        """
        if menu_choice == "1":
            game = Game()
            game.run_game()
            # controls whether menu shows again or not
            return True

        if menu_choice == "2":
            self.show_instructions()
            # controls whether menu shows again or not
            return True

        else:
            print("\nGood bye!\n")
            # controls whether menu shows again or not
            return False

    def run_menu(self):
        """
        Outer loop, displays menu, takes user choice and
        controls what happens next: run game, show instructions
        or exit the game
        """
        while True:
            self.show_menu()
            menu_choice = self.take_choice()
            # handles menu choice, calls appropriate functions
            # and controls whether menu shows again or not
            if self.handle_menu_choice(menu_choice):
                continue
            else:
                break


class Game:
    """
    Create instance of Game
    """
    def __init__(
            self, colors=[f"{i}" for i in range(1, 7)],
            # max rounds 4 for quicker testing
            code_length=4, max_rounds=12
            ):
        self.colors = colors
        self.code_length = code_length
        self.max_rounds = max_rounds
        self.secret_code = self.create_code()

    def create_code(self):
        """
        Randomly choose {self.code_length} items from the colors list
        Create secret code as a string
        """
        code_array = random.choices(self.colors, k=self.code_length)
        code = "".join(code_array)
        return code

    def game_won(self, score, attempts):
        if score[0] == self.code_length:
            print(
                "\nCongratulations, you cracked the secret code "
                f"'{self.secret_code}' in {attempts} "
                f"{'rounds' if attempts != 1 else 'round'}.\n"
                )
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
        print("Welcome to a game of Mastermind. ... Instructions ...")
        print(f"You have {self.max_rounds} attempts.\n")
        # Give description of secret code, generalised to colors list
        # consisting of numbers or alphabetic characters
        print(
            f"The secret code consists of {self.code_length} "
            f"{'digits' if self.colors[0].isnumeric() else 'characters'} "
            f"out of {self.colors}\n"
            )
        print(f"For testing: secret code: {self.secret_code}\n")

    def run_game(self):
        """
        Run game
        """
        self.welcome_message()
        # Create board
        board = Board()
        # Reset to first round (1st attempt)
        attempts = 1
        # game loop
        while True:
            print(f"\nRound {attempts}:\n")
            # Create new guess, pass secret code and colors list
            # to be able to check guess against secret
            latest_guess = Guess(self.secret_code, self.colors)
            print(f"\nYou guessed: {latest_guess.guessed_code}\n")
            # Check guess against secret and save score
            latest_score = latest_guess.score
            print(
                f"You have {latest_score[0]} hits and "
                f"{latest_score[1]} close.\n"
                )
            # Show board
            board.append_guess(latest_guess)
            board.show(attempts)

            # check break conditions
            if self.game_won(latest_score, attempts):
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
    def __init__(self):
        pass

    # Initialize list of guesses and include board headers
    guess_list = [["Guess:", "Hits:", "Close:"]]

    def append_guess(self, guess):
        """
        Append latest guess to the board
        """
        self.guess_list.append(
            # Improve formatting of guess in board
            [" ".join(list(guess.guessed_code)), \
                guess.score[0], guess.score[1]]
            )

    def show(self, rounds):
        """
        Print the board with nice formatting
        Code inspiration from:
        https://learnpython.com/blog/print-table-in-python/
        """
        rowIDs = [i for i in range(1, rounds + 1)]
        print(tabulate(
            self.guess_list, headers='firstrow',
            tablefmt='rounded_outline', showindex=rowIDs
            ))


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
        if guess is of correct length and
        contains only valid characters return it
        """
        while True:

            guess = input("Enter your guess: \n").strip()

            # Check that guess is not empty
            if len(guess) == 0:
                print("\nYour guess is empty.\n")
                continue

            # Check that guess has correct length
            if len(guess) != len(self.secret):
                print(f"\nYour guess '{guess}' is not the right length.\n")
                continue

            # Check that guess only contains valid characters
            # according to colors list
            characters_valid = True
            for char in guess:
                if char.lower() not in \
                        [color.lower() for color in self.colors]:
                    # Compare lowercase strings so that it works for general
                    # colors list inGame class, which can contain letters
                    print(
                        f"\nYour guess '{guess}' contains "
                        "invalid characters.\n"
                        )
                    characters_valid = False
                    break

            if characters_valid is True:
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
                secret_checked = secret_checked[:i] + "." \
                    + secret_checked[i + 1:]
        # check for close
        for char in guess_checked:
            if char in secret_checked:
                close += 1
                # replace checked character in secret by . so don't count twice
                secret_checked = secret_checked.replace(char, ".", 1)
        return [hits, close]


# Create and run game menu
menu = GameMenu()
menu.run_menu()
