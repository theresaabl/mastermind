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

    def take_menu_choice(self):
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
            level = ChooseLevel()
            level.run_choose_level()
            # menu shows again
            return True

        elif menu_choice == "2":
            self.show_instructions()
            # menu shows again
            return True

        else:
            print("\nGood bye!\n")
            # menu does not show again
            return False

    def run_menu(self):
        """
        Outer loop, displays menu, takes user choice and
        controls what happens next: run game, show instructions
        or exit the game
        """
        while True:
            self.show_menu()
            menu_choice = self.take_menu_choice()
            # handles menu choice, calls appropriate functions
            # and controls whether menu shows again or not
            if self.handle_menu_choice(menu_choice):
                continue
            else:
                break


class ChooseLevel():
    """
    Creates instance of ChooseLevel
    """
    def __init__(self):
        pass

    def show_level_menu(self):
        """
        Print the menu choices
        """
        print("\nChoose a level\n")
        print("1 - Easy\n")
        print("2 - Classic\n")
        print("3 - Hard\n")

    def take_level_choice(self):
        """
        Take user input level choice, validate it
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

    def handle_level_choice(self, level_choice):
        """
        Check which option user chose and call functions accordingly
        """
        if level_choice == "1":
            print("\nLevel 1 selected\n")
            game = Game("1")
            game.run_game()

        elif level_choice == "2":
            print("\nLevel 2 selected\n")
            game = Game("2")
            game.run_game()

        else:
            print("\nLevel 3 selected\n")
            game = Game("3")
            game.run_game()

    def run_choose_level(self):
        """
        Show level choice menu, take user input
        and start game accordingly
        """
        while True:
            self.show_level_menu()
            level_choice = self.take_level_choice()
            break

        # handle level choice and start game
        self.handle_level_choice(level_choice)


class Game:
    """
    Create instance of Game
    """
    def __init__(self, level):
        self.level = level
        self.set_level()
        self.secret_code = self.create_code()

    def set_level(self):
        if self.level == "1":
            self.colors = ["1", "2", "3", "4"]
            self.code_length = 3
            self.max_rounds = 12
            self.repetitions = True

        elif self.level == "2":
            self.colors = ["1", "2", "3", "4", "5", "6"]
            self.code_length = 4
            self.max_rounds = 12
            self.repetitions = True

        else:
            self.colors = ["1", "2", "3", "4", "5", "6", "7", "8"]
            self.code_length = 5
            self.max_rounds = 12
            # no repetitions allowed
            self.repetitions = False

    def create_code(self):
        """
        Randomly choose {self.code_length} items from the colors list
        Create secret code as a string
        Account for repetitions allowed or not
        """
        if self.repetitions:
            # repetition allowed
            code_array = random.choices(self.colors, k=self.code_length)
            code = "".join(code_array)

        else:
            # no repetition
            code_array = random.sample(self.colors, k=self.code_length)
            code = "".join(code_array)
        return code

    def game_won(self, score, attempts):
        """
        Check if game is won
        """
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
        """
        Check if has reached maximum attempts
        """
        if attempts == self.max_rounds:
            print("\nYou have run out of attempts.\n")
            return True
        else:
            return False

    def welcome_message(self):
        print("\nMASTERMIND\n")
        print("Welcome to a game of Mastermind. ... Instructions ...\n")
        # Give description of secret code, generalised to colors list
        # consisting of numbers or alphabetic characters
        print(
            f"The secret code consists of {self.code_length} "
            f"{'digits' if self.colors[0].isnumeric() else 'characters'} "
            f"{f'between {self.colors[0]} and {self.colors[-1]}'
                if self.colors[0].isnumeric()
                else f'out of {self.colors}'}, "
            "where repetitions are "
            f"{'' if self.repetitions else 'not '}allowed."
            f"\nYou have {self.max_rounds} attempts to crack the code.\n"
            )
        print(f"For testing: secret code: {self.secret_code}\n")

    def run_game(self):
        """
        Run game
        """
        self.welcome_message()
        # Reset to first round (1st attempt)
        attempts = 1
        # Create board
        board = Board()
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
        # Initialize list of guesses and include board headers
        self.guess_list = [["Guess:", "Hits:", "Close:"]]

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
