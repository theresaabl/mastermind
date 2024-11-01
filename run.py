# mock terminal of 80 characters wide and 24 rows high
import random
from tabulate import tabulate
import time
# import colorama module to print color text
import colorama
from colorama import Fore, Style
# initialize module
colorama.init(autoreset=True)


class Screen:
    """
    Creates an instance of Screen
    """
    def __init__(self):
        self.clear_screen()

    def clear_screen(self):
        """
        Clear console
        Code from https://stackoverflow.com/a/50921841
        """
        print("\033c")

    def press_enter(self):
        """
        Continue when user presses enter
        """
        self.user_input("Press ENTER to continue.\n")

    def user_input(self, message):
        """
        Take user input and catch KeyboardInterrupt
        if user inputs exit, call exit_application
        """
        while True:
            try:
                while True:
                    user_input = input(message)
                    # If user types exit at any point, call exit_application
                    if user_input.lower().strip() == "exit":
                        self.exit_application()
                    else:
                        return user_input
            except KeyboardInterrupt:
                # Checks whether user wants to exit
                # If not, continue to take user input again
                if not self.handle_exit_request():
                    continue

    def handle_exit_request(self):
        """
        Control what happens when user presses Crtl + C
        """
        while True:
            user_input = self.user_input(
                "\nAre you sure you want to exit the application?\n"
                f"Enter {Fore.GREEN}y{Fore.RESET} for yes or "
                f"{Fore.RED}n{Fore.RESET} for no.\n"
                )

            # Validate input for y and n
            # If valid: break
            if self.validate_y_n(user_input):
                break
            else:
                continue

        if user_input == "y":
            self.exit_application()
        else:
            print("\nContinuing application ...\n")
            time.sleep(1)
            # return False indicates that user does not want to quit
            return False

    def exit_application(self):
        """
        Print good bye message and exit
        """
        print("\nExiting application ...")
        time.sleep(1)
        self.clear_screen()
        print("\nGood bye!\n")
        time.sleep(2)
        self.clear_screen()
        exit()

    def validate_y_n(self, input):
        """
        Validates whether input is y or n, nothing else
        Returns True if valid, False otherwise
        """
        while True:

            # Check that choice is not empty
            if len(input) == 0:
                print(f"{Fore.RED}\nYour choice is empty.\n")
                return False

            # Check that choice is y or n
            if len(input) != 1 or input.lower() not in "yn":
                print(f"{Fore.RED}\nYour choice '{input}' is not valid.\n")
                return False

            # If choice is valid, return True
            return True

    def print_logo(self, plain_text):
        """
        Print Ascii art of logo
        or plain text for plain text mode
        """
        if plain_text:
            # plain text mode
            print(f"{Fore.BLUE}{Style.BRIGHT}MASTERMIND\n")
        else:
            print(
                Fore.BLUE
                + Style.BRIGHT
                + r"    __  __         _                 _         _ "
                )
            print(
                Fore.BLUE
                + Style.BRIGHT
                + r"   |  \/  |__ _ __| |_ ___ _ _ _ __ (_)_ _  __| |"
                )
            print(
                Fore.BLUE
                + Style.BRIGHT
                + r"   | |\/| / _` (_-<  _/ -_) '_| '  \| | ' \/ _` |"
                )
            print(
                Fore.BLUE
                + Style.BRIGHT
                + r"   |_|  |_\__,_/__/\__\___|_| |_|_|_|_|_||_\__,_|"
                )
            print("")

    def print_instructions(self):
        """
        Show game instructions until user presses key
        """
        self.clear_screen()
        if self.plain_text:
            print("\nMASTERMIND\n")
        else:
            self.print_logo(self.plain_text)
        print(
            # Important: Change numbers to letters if letters are used
            # for secret code elements in colors list
            # Adapt rules to the difficulty levels available
            f"""
Welcome to {Fore.BLUE}{Style.BRIGHT}Mastermind{Style.RESET_ALL}!

Objective:
- Your goal is to guess a secret code within a limited number of rounds.
- The code consists of a sequence of colors, represented by numbers.

Rules:
1. The code is made up of 3 - 5 color slots, depending on the level of
   difficulty chosen. Each slot contains one of 4 - 8 possible colors.
2. Colors may (or may not) repeat, depending on the level chosen.
3. For each guess, you will receive feedback to help you get closer
   to the correct code.

Levels:
There are three distinct levels to choose from:
  1 - Easy
  2 - Classic
  3 - Hard

Feedback:
- "Hits": The number of colors in your guess that are correct in both
          color and position.
- "Close": The number of colors in your guess that are correct in color
           but placed in the wrong slot.

Winning:
If you match all colors in the correct positions before finishing the
final round, you win!

Tips:
- Use the feedback to adjust your guesses strategically.
- With each try, aim to get more colors in the correct position.

Exiting the Game:
You can exit the game at any point by entering EXIT in an input field.

Good luck, and have fun cracking the code!
    """
        )
        self.press_enter()

    def show_start_screen(self):
        """
        Show plain text start screen to ask user whether
        they want plain text mode or not
        For accessibility, to avoid ascii art,
        formatted tables etc. for screen readers
        """
        print(f"\nWelcome to {Fore.BLUE}{Style.BRIGHT}MASTERMIND\n")
        time.sleep(1)
        print("A Python console game\n")
        time.sleep(1)
        self.plain_text = self.plain_text_request()
        if self.plain_text:
            print("\nPlain text mode selected.\n")
            self.press_enter()
            return True
        else:
            self.clear_screen()
            self.print_logo(False)
            time.sleep(1)
            return False

    def plain_text_request(self):
        """
        Take user input on whether plain text mode is wanted or not
        """
        while True:
            plain_text = self.user_input(
                "Would you like to access the game in "
                f"{Fore.CYAN}plain text mode{Fore.RESET},\n"
                "i.e. with all visual elements removed?\n"
                f"Enter {Fore.GREEN}y{Fore.RESET} for yes or "
                f"{Fore.RED}n{Fore.RESET} for no.\n"
                ).strip()

            # Validate input for y and n
            # If valid: break
            if self.validate_y_n(plain_text):
                break
            else:
                continue

        return True if plain_text == "y" else False


class GameMenu:
    """
    Create instance of GameMenu
    """
    def __init__(self):
        # create instance of Screen when GameMenu is initialised
        self.screen = Screen()
        # show start screen each time and save viewing mode
        self.plain_text = self.screen.show_start_screen()

    def show_menu(self):
        """
        Print the menu choices
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.plain_text)
        print("Game Menu\n")
        print("1 - Play Game\n")
        print("2 - Show Instructions\n")
        print("3 - Exit\n")

    def take_menu_choice(self):
        """
        Take user input menu choice, validate it
        and return it if valid
        """
        while True:
            choice = self.screen.user_input(
                "Choose from options 1 - 3: \n"
                ).strip()

            # Check that choice is not empty
            if len(choice) == 0:
                print(f"{Fore.RED}\nYour choice is empty.\n")
                continue

            # Check that choice is numeric and of length 1
            if len(choice) != 1 or choice not in "123":
                print(f"{Fore.RED}\nYour choice '{choice}' is not valid.\n")
                continue

            # If choice is valid, break
            break

        return choice

    def handle_menu_choice(self, menu_choice):
        """
        Check which option user chose and call functions accordingly
        """
        if menu_choice == "1":
            # pass Screen instance to ChooseLevel instance
            level = ChooseLevel(self.screen)
            level.run_choose_level()
            # menu shows again
            return True

        elif menu_choice == "2":
            self.screen.print_instructions()
            # menu shows again
            return True

        elif menu_choice == "3":
            self.screen.exit_application()

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
            # Show menu until user chooses exit
            self.handle_menu_choice(menu_choice)


class ChooseLevel():
    """
    Creates instance of ChooseLevel
    """
    def __init__(self, screen):
        # pass screen instance
        self.screen = screen

    def show_level_menu(self):
        """
        Print the menu choices
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        print("Level Menu\n")
        print(f"1 - {Fore.GREEN}Easy\n")
        print(f"2 - {Fore.YELLOW}Classic\n")
        print(f"3 - {Fore.RED}Hard\n")

    def take_level_choice(self):
        """
        Take user input level choice, validate it
        and return it if valid
        """
        while True:
            choice = self.screen.user_input(
                "Choose from options 1 - 3: \n"
                ).strip()

            # Check that choice is not empty
            if len(choice) == 0:
                print(f"{Fore.RED}\nYour choice is empty.\n")
                continue

            # Check that choice is numeric and of length 1
            if len(choice) != 1 or choice not in "123":
                print(f"{Fore.RED}\nYour choice '{choice}' is not valid.\n")
                continue

            # If choice is valid, break
            break

        return choice

    def handle_level_choice(self, level_choice):
        """
        Check which option user chose and call functions accordingly
        """
        if level_choice == "1":
            print(f"\nLevel 1 - {Fore.GREEN}Easy{Fore.RESET} - selected\n")
            time.sleep(2)
            game = Game("1", self.screen)
            game.run_game()

        elif level_choice == "2":
            print(f"\nLevel 2 - {Fore.YELLOW}Classic{Fore.RESET} - selected\n")
            time.sleep(2)
            game = Game("2", self.screen)
            game.run_game()

        else:
            print(f"\nLevel 3 - {Fore.RED}Hard{Fore.RESET} - selected\n")
            time.sleep(2)
            game = Game("3", self.screen)
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
    def __init__(self, level, screen):
        self.level = level
        self.set_level()
        self.secret_code = self.create_code()
        # pass instance of screen
        self.screen = screen

    def set_level(self):
        """
        Define the three difficulty levels
        Specify code elements (colors), code length, the maximum amount of
        rounds and whether repetitions are allowed in the code
        """
        if self.level == "1":
            # Can use numbers or letters as code elements
            # They represent the colors in the mastermind game
            # Set up to use numeric code for better accessibility
            self.colors = ["1", "2", "3", "4"]
            # Can change to color-letters, e.g.
            # B - blue, R - red, Y - yellow, P - purple
            # self.colors = ["B", "R", "Y", "P"]
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

    def game_won(self, score, attempts, board):
        """
        Check if game is won
        """
        if score[0] == self.code_length:
            self.screen.clear_screen()
            self.screen.print_logo(self.screen.plain_text)
            print(
                f"\nCongratulations, you {Fore.YELLOW}{Style.BRIGHT}WON!\n"
                f"{Style.RESET_ALL}\nYou cracked the secret code "
                f"{Fore.YELLOW}{self.secret_code}{Fore.RESET} in {attempts} "
                f"{'rounds' if attempts != 1 else 'round'}.\n"
                )
            board.show(attempts)
            time.sleep(1)
            print("")
            self.screen.press_enter()
            return True
        else:
            return False

    def check_max_rounds(self, attempts):
        """
        Check if has reached maximum attempts
        """
        if attempts == self.max_rounds:
            print(f"{Fore.RED}\nYou have run out of attempts.\n")
            time.sleep(1)
            self.screen.press_enter()
            return True
        else:
            return False

    def game_welcome_message(self):
        """
        Print welcome message when game starts
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        level_strings = ["Easy", "Classic", "Hard"]
        print(f"Welcome to a game of {Fore.BLUE}{Style.BRIGHT}Mastermind.\n")
        time.sleep(1)
        level_name = level_strings[int(self.level)-1]
        # Set up color printing for level names
        if level_name == "Easy":
            level_name_color = Fore.GREEN
        elif level_name == "Classic":
            level_name_color = Fore.YELLOW
        elif level_name == "Hard":
            level_name_color = Fore.RED
        print(f"Level {self.level} - {level_name_color}{level_name}\n")
        time.sleep(1)
        print(
            f"The goal is to crack a secret code within "
            f"{Fore.CYAN}{self.max_rounds} rounds{Fore.RESET}.\nThe code "
            f"consists of {Fore.CYAN}{self.code_length} "
            f"{
                'digits' if self.colors[0].isnumeric() else 'characters'
            }{Fore.RESET} "
            f"{f'between {Fore.CYAN}{self.colors[0]} and {self.colors[-1]}'
                if self.colors[0].isnumeric()
                else f'out of {Fore.CYAN}{", ".join(self.colors)}'},\n"
            f"{Fore.RESET}where {Fore.CYAN}repetitions{Fore.RESET} are "
            f"{Fore.CYAN}{'' if self.repetitions else 'not '}allowed.\n"
        )
        time.sleep(1)
        self.screen.press_enter()

    def secret_code_description(self):
        """
        Give description of secret code, generalised to colors list
        consisting of numbers or alphabetic characters
        """
        print(
            f"Secret code:\n"
            f"- {Fore.CYAN}{self.code_length} "
            f"{'digits' if self.colors[0].isnumeric() else 'characters'} "
            f"{Fore.RESET}{
                f'between {Fore.CYAN}{self.colors[0]} and {self.colors[-1]}'
                if self.colors[0].isnumeric()
                else f'out of {Fore.CYAN}{", ".join(self.colors)}'
            }{Fore.RESET},\n"
            f"- repetitions {'' if self.repetitions else '{Fore.CYAN}not '}"
            f"{Fore.RESET}allowed\n"
            f"- {Fore.CYAN}{self.max_rounds} rounds\n"
        )
        # Remove after testing ###############################################
        print(f"For testing: secret code: {self.secret_code}\n")

    def run_game(self):
        """
        Run game
        """
        self.game_welcome_message()
        # Reset to first round (1st attempt)
        attempts = 1
        # Create board
        board = Board(self.screen)
        # game loop
        while True:
            self.screen.clear_screen()
            self.screen.print_logo(self.screen.plain_text)
            self.secret_code_description()
            print(f"{Fore.CYAN}Round {attempts}:\n")
            if attempts > 1:
                board.show(attempts - 1)
            # Create new guess, pass secret code, colors list and screen
            # to be able to check guess against secret and take user_input()
            latest_guess = Guess(self.secret_code, self.colors, self.screen)
            # Check guess against secret and save score
            latest_score = latest_guess.score
            hits = latest_score[0]
            close = latest_score[1]
            print(
                f"\nYour guess {latest_guess.guessed_code} has "
                f"{hits} hit{'' if hits == 1 else 's'} "
                f"and {close} close."
                )
            # Show board
            board.append_guess(latest_guess)

            # check break conditions
            if self.game_won(latest_score, attempts, board):
                break
            if self.check_max_rounds(attempts):
                break
            else:
                # increment attempts
                attempts += 1

            time.sleep(2)


class Board:
    """
    Create instance of Board
    """
    def __init__(self, screen):
        # Initialize list of guesses and include board headers
        self.guess_list = [["Guess:", "Hits:", "Close:"]]
        # pass instance of Screen
        self.screen = screen

    def append_guess(self, guess):
        """
        Append latest guess to the board
        """
        self.guess_list.append(
            # Improve formatting of guess in board
            [
                " ".join(list(guess.guessed_code)),
                guess.score[0], guess.score[1]
            ]
            )

    def show(self, rounds):
        """
        Print the board with nice formatting or for plain text mode
        Code inspiration from:
        https://learnpython.com/blog/print-table-in-python/
        """
        if self.screen.plain_text:
            # printing for plain text mode
            headings = self.guess_list[0]
            for line in self.guess_list[1:]:
                print(
                    f"{headings[0]} {line[0]}, "
                    f"{Fore.RED}{headings[1]} {line[1]}, {Fore.RESET}"
                    f"{headings[2]} {line[2]}"
                )
        else:
            # nicely formatted table
            rowIDs = [i for i in range(1, rounds + 1)]
            print(tabulate(
                self.guess_list, headers='firstrow',
                tablefmt='rounded_outline', showindex=rowIDs
                ))


class Guess:
    """
    Create instance of Guess
    """
    def __init__(self, secret, colors, screen):
        self.secret = secret
        self.colors = colors
        self.guessed_code = self.take_guess(screen)
        self.score = self.check_guess()

    def take_guess(self, screen):
        """
        Take a guess from the user and check for valid input
        if guess is of correct length and
        contains only valid characters return it
        """
        while True:

            # Take user input, strip of empty spaces in beginning and end
            # Convert it to uppercase string
            guess = screen.user_input("\nEnter your guess: \n").strip().upper()

            # Check that guess is not empty
            if len(guess) == 0:
                print(f"{Fore.RED}Your guess is empty.\n")
                continue

            # Check that guess has correct length
            if len(guess) != len(self.secret):
                print(
                    f"{Fore.RED}\nYour guess '{guess}' is "
                    "not the right length.\n"
                )
                continue

            # Check that guess only contains valid characters
            # according to colors list
            characters_valid = True
            for char in guess:
                if char not in [color for color in self.colors]:
                    print(
                        f"{Fore.RED}\nYour guess '{guess}' contains "
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
