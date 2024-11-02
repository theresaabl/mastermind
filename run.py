import random
import time
# Import tabulate to format table
from tabulate import tabulate
# Import pyfiglet for ascii art logo
import pyfiglet
# Import colorama module to print color text
import colorama
from colorama import Fore, Style
# Initialize module
colorama.init(autoreset=True)


class Screen:
    """
    Create an instance of Screen
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
        self.user_input(" Press ENTER to continue.\n")

    def user_input(self, message):
        """
        Take user input and catch KeyboardInterrupt or user input 'exit'
        Code inspiration to catch KeybaordInterrupt from:
        https://stackoverflow.com/questions/37887624/python-3-keyboardinterrupt-error
        """
        while True:
            try:
                while True:
                    # Add an empty space to input message for format
                    # of deployed site
                    user_input = input(message + " ")
                    # If user types exit at any point, call handle_exit_request
                    if user_input.lower().strip() == "exit":
                        self.handle_exit_request()
                    else:
                        return user_input
            except KeyboardInterrupt:
                # Check whether user wants to exit
                # If not, continue to take user input again
                if not self.handle_exit_request():
                    continue

    def handle_exit_request(self):
        """
        Control what happens when user presses Crtl + C
        Take user input y or n, validate input
        Call exit_application if y, return False if n
        """
        print("\n Are you sure you want to exit the application?")
        while True:
            user_input = self.user_input(
                f" Enter {Fore.GREEN}y{Fore.RESET} for yes or "
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
            print("\n Continuing application ...\n")
            time.sleep(1)
            # Return False indicates that user does not want to quit
            return False

    def exit_application(self):
        """
        Print good bye message and exit
        """
        print("\n Exiting application ...")
        time.sleep(1)
        self.clear_screen()
        print("\n Good bye!\n")
        time.sleep(2)
        self.clear_screen()
        # Exit application
        exit()

    def validate_y_n(self, input):
        """
        Validate whether input is y or n and nothing else
        Return True if valid, False otherwise
        """
        while True:

            # Check that choice is not empty
            if len(input) == 0:
                print(f"{Fore.RED}\n Your choice is empty.\n")
                return False

            # Check that choice is y or n
            if len(input) != 1 or input.lower() not in "yn":
                print(
                    f"{Fore.RED}\n Your choice '{input}' contains "
                    "invalid characters.\n"
                )
                return False

            # If choice is valid, return True
            return True

    def show_start_screen(self):
        """
        Show plain text start screen to ask user whether they want plain text
        mode or not. This is for better accessibility, especially to avoid
        ascii art, formatted tables etc. for screen readers.
        Inspiration taken from:
        https://dev.to/baspin94/two-ways-to-make-your-command-line-interfaces-more-accessible-541k
        Return True if plain text mode selected and False otherwise
        """
        print(f" Welcome to {Fore.BLUE}{Style.BRIGHT}MASTERMIND\n")
        time.sleep(1)
        print(" A Python console game\n")
        time.sleep(1)
        # Call plain_text_request to take user input
        self.plain_text = self.plain_text_request()
        if self.plain_text:
            print("\n Plain text mode selected.\n")
            self.press_enter()
            # Show plain text mode logo for 1 second before continues
            self.clear_screen()
            self.print_logo(True)
            time.sleep(1)
            return True
        else:
            # Show logo for 1 second before continues
            self.clear_screen()
            self.print_logo(False)
            time.sleep(1)
            return False

    def plain_text_request(self):
        """
        Take user input on whether plain text mode is wanted or not
        Validate for y or n
        Return True if plain text mode selected or False if not
        """
        print(
            f" Would you like to access the game in {Fore.CYAN}plain text mode"
            f"{Fore.RESET},\n i.e. with all visual elements removed?"
        )
        while True:
            plain_text = self.user_input(
                f" Enter {Fore.GREEN}y{Fore.RESET} for yes or "
                f"{Fore.RED}n{Fore.RESET} for no.\n"
                ).strip()

            # Validate input for y and n
            # If valid: break
            if self.validate_y_n(plain_text):
                break
            else:
                continue

        return True if plain_text == "y" else False

    def print_logo(self, plain_text):
        """
        Print Ascii art logo
        or plain text for plain text mode
        """
        if plain_text:
            # Plain text mode
            print(f"{Fore.BLUE}{Style.BRIGHT} MASTERMIND\n")
        else:
            logo = pyfiglet.figlet_format("    Mastermind", font="small")
            print(f"{Fore.BLUE}{Style.BRIGHT}{logo}")

    def take_menu_choice(self, options):
        """
        Take user input menu choice out of {options} options, validate it
        and return it once it is valid
        """
        while True:
            choice = self.user_input(
                f" Choose from options 1 - {options}: \n"
                ).strip()

            # Check that choice is not empty
            if len(choice) == 0:
                print(f"{Fore.RED}\n Your choice is empty.\n")
                continue

            # Check that choice is single digit between 1 and {options}
            # Create string containing all menu options
            options_string = ""
            for digit in range(1, options + 1):
                options_string += str(digit)

            if len(choice) != 1 or choice not in options_string:
                print(f"{Fore.RED}\n Your choice '{choice}' is not valid.\n")
                continue

            # If choice is valid, break
            break

        return choice

    def color_secret_code(self, code):
        """
        Add colorama colors for each digit in numeric secret code
        Important: For alphabetic secret code would need to set up depending on
        characters chosen
        Return a string of secret code containing colorama color code
        """
        color_code = ""
        for char in code:
            if char == "1" or char == "7":
                color_char = Fore.MAGENTA
            elif char == "2" or char == "8":
                color_char = Fore.RED
            elif char == "3" or char == "9":
                color_char = Fore.YELLOW
            elif char == "4":
                color_char = Fore.CYAN
            elif char == "5":
                color_char = Fore.GREEN
            elif char == "6":
                color_char = Fore.BLUE

            char = f"{color_char}{Style.BRIGHT}{char}"
            color_code += char

        color_code += f"{Style.RESET_ALL}"
        return (color_code)

    def print_instructions(self):
        """
        Show game instructions until user presses ENTER
        """
        self.clear_screen()
        self.print_logo(self.plain_text)

        # Important: Change numbers to letters if letters are used
        # for secret code elements in colors list
        # Important: Adapt rules to the difficulty levels available (if change)
        instructions = f"""
 Welcome to {Fore.BLUE}{Style.BRIGHT}Mastermind{Style.RESET_ALL}!

 {Fore.MAGENTA}{Style.BRIGHT}Objective{Style.RESET_ALL}:
 - Your goal is to {Fore.CYAN}guess a secret code{Fore.RESET} within a \
limited number of rounds.
 - The code consists of a {Fore.CYAN}sequence of colors{Fore.RESET}, \
represented by numbers.

 {Fore.MAGENTA}{Style.BRIGHT}Rules{Style.RESET_ALL}:
 1. The code is made up of {Fore.CYAN}3 - 5 color slots{Fore.RESET}, \
depending on the level of
    difficulty chosen. Each slot contains one of {Fore.CYAN}4 - 8 possible \
colors{Fore.RESET}.
 2. Colors {Fore.CYAN}may (or may not) repeat{Fore.RESET}, depending on the \
level chosen.
 3. For each guess, you will receive {Fore.CYAN}feedback{Fore.RESET} to help \
you get closer to
    the correct code.

 {Fore.MAGENTA}{Style.BRIGHT}Levels{Style.RESET_ALL}:
 There are three distinct levels to choose from:
   1 - {Fore.GREEN}Easy{Fore.RESET}
   2 - {Fore.YELLOW}Classic{Fore.RESET}
   3 - {Fore.RED}Hard{Fore.RESET}

 {Fore.MAGENTA}{Style.BRIGHT}Feedback{Style.RESET_ALL}:
 - {Fore.GREEN}"Hits"{Fore.RESET}:  The number of colors in your guess that \
are correct in
            both {Fore.CYAN}color and position{Fore.RESET}.
 - {Fore.YELLOW}"Close"{Fore.RESET}: The number of colors in your guess that \
are correct in
            {Fore.CYAN}color{Fore.RESET} but wrong in postition.

 {Fore.MAGENTA}{Style.BRIGHT}Winning{Style.RESET_ALL}:
 If you {Fore.CYAN}match all colors{Fore.RESET} in the correct positions \
 before finishing the
 final round, you win!

 {Fore.MAGENTA}{Style.BRIGHT}Tips{Style.RESET_ALL}:
 - Use the {Fore.CYAN}feedback{Fore.RESET} to adjust your guesses \
strategically.
 - With each try, aim to get more colors in the correct position.

 {Fore.MAGENTA}{Style.BRIGHT}Exiting the Game{Style.RESET_ALL}:
 You can exit the game at any point by entering {Fore.CYAN}EXIT{Fore.RESET}.

 {Fore.MAGENTA}{Style.BRIGHT}Good luck, and have fun cracking the code!
    """
        print(instructions)
        self.press_enter()


class GameMenu:
    """
    Create an instance of GameMenu
    """
    def __init__(self):
        # Create instance of Screen when GameMenu is initialised
        self.screen = Screen()
        # Show start screen and save viewing mode
        self.plain_text = self.screen.show_start_screen()

    def show_menu(self):
        """
        Print the menu choices
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.plain_text)
        print(" Game Menu\n")
        print(" 1 - Play Game\n")
        print(" 2 - Show Instructions\n")
        print(" 3 - Exit\n")

    def handle_menu_choice(self, menu_choice):
        """
        Check which option user chose and call functions accordingly
        Return True if want menu to show again
        """
        if menu_choice == "1":
            # Create new ChooseLevel instance and pass Screen instance
            level = ChooseLevel(self.screen)
            level.run_choose_level()
            # Show menu again
            return True

        elif menu_choice == "2":
            self.screen.print_instructions()
            # Show menu again
            return True

        elif menu_choice == "3":
            self.screen.exit_application()

    def run_menu(self):
        """
        Outer loop: display menu, take user choice and
        control what happens next: run game, show instructions
        or exit the game
        """
        while True:
            # While loop broken from inside functions
            self.show_menu()
            # Pass number of menu options
            menu_choice = self.screen.take_menu_choice(3)
            # Handle menu choice, call appropriate functions
            # Show menu until user chooses exit
            self.handle_menu_choice(menu_choice)


class ChooseLevel():
    """
    Create an instance of ChooseLevel
    """
    def __init__(self, screen):
        # Pass screen instance
        self.screen = screen

    def show_level_menu(self):
        """
        Print the menu choices
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        print(" Level Menu\n")
        print(f" 1 - {Fore.GREEN}Easy\n")
        print(f" 2 - {Fore.YELLOW}Classic\n")
        print(f" 3 - {Fore.RED}Hard\n")

    def handle_level_choice(self, level_choice):
        """
        Check which option user chose and call the functions that
        start the game accordingly
        """
        if level_choice == "1":
            print(f"\n Level 1 - {Fore.GREEN}Easy{Fore.RESET} - selected\n")
            time.sleep(2)
            game = Game("1", self.screen)
            game.run_game()

        elif level_choice == "2":
            print(
                f"\n Level 2 - {Fore.YELLOW}Classic{Fore.RESET} - selected\n"
            )
            time.sleep(2)
            game = Game("2", self.screen)
            game.run_game()

        else:
            print(f"\n Level 3 - {Fore.RED}Hard{Fore.RESET} - selected\n")
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
            # Pass number of menu options
            level_choice = self.screen.take_menu_choice(3)
            break

        # Handle level choice and start game
        self.handle_level_choice(level_choice)


class Game:
    """
    Create an instance of Game
    """
    def __init__(self, level, screen):
        self.level = level
        # Call set_level method when Game is initialised
        self.set_level()
        # Create a secret code when Game is initialised
        self.secret_code = self.create_code()
        # Pass instance of screen
        self.screen = screen

    def set_level(self):
        """
        Define the three difficulty levels
        Specify code elements (colors), code length, the maximum amount of
        rounds and whether repetitions are allowed in the code
        """
        if self.level == "1":
            # This project works for numbers or letters as code elements
            # They represent the colors in the mastermind game
            # Here: set up to use numeric code for better accessibility
            self.colors = ["1", "2", "3", "4"]
            # Can change to color-letters, e.g.
            # B - blue, R - red, Y - yellow, P - purple
            # Option: self.colors = ["B", "R", "Y", "P"]
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
            # No repetitions allowed
            self.repetitions = False

    def game_welcome_message(self):
        """
        Print welcome message when game starts
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        level_strings = ["Easy", "Classic", "Hard"]
        print(f" Welcome to a game of {Fore.BLUE}{Style.BRIGHT}Mastermind.\n")
        time.sleep(1)
        level_name = level_strings[int(self.level)-1]
        # Set up color printing for level names
        if level_name == "Easy":
            level_name_color = Fore.GREEN
        elif level_name == "Classic":
            level_name_color = Fore.YELLOW
        elif level_name == "Hard":
            level_name_color = Fore.RED
        print(f" Level {self.level} - {level_name_color}{level_name}\n")
        time.sleep(1)
        print(
            f" The goal is to crack a secret code within "
            f"{Fore.CYAN}{self.max_rounds} rounds{Fore.RESET}.\n The code "
            f"consists of {Fore.CYAN}{self.code_length} "
            f"{
                'digits' if self.colors[0].isnumeric() else 'characters'
            }{Fore.RESET} "
            f"{f'between {Fore.CYAN}{self.colors[0]} and {self.colors[-1]}'
                if self.colors[0].isnumeric()
                else f'out of {Fore.CYAN}{", ".join(self.colors)}'},\n"
            f" {Fore.RESET}where {Fore.CYAN}repetitions{Fore.RESET} are "
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
            f" Secret code:\n"
            f" - {Fore.CYAN}{self.code_length} "
            f"{'digits' if self.colors[0].isnumeric() else 'characters'} "
            f"{Fore.RESET}{
                f'between {Fore.CYAN}{self.colors[0]} and {self.colors[-1]}'
                if self.colors[0].isnumeric()
                else f'out of {Fore.CYAN}{", ".join(self.colors)}'
            }{Fore.RESET}\n"
            f" - repetitions {'' if self.repetitions else f'{Fore.CYAN}not '}"
            f"{Fore.RESET}allowed\n"
            f" - {Fore.CYAN}{self.max_rounds} rounds\n"
        )

    def create_code(self):
        """
        Randomly choose {self.code_length} items from the colors list
        Create secret code as a string
        Account for repetitions allowed or not
        Return secret code string
        """
        if self.repetitions:
            # Repetition allowed
            code_array = random.choices(self.colors, k=self.code_length)
            code = "".join(code_array)

        else:
            # No repetition
            code_array = random.sample(self.colors, k=self.code_length)
            code = "".join(code_array)

        return code

    def game_won(self, score, attempts, board):
        """
        Check if game is won and call win_message if yes
        Return True if all colors match the secret code and False otherwise
        """
        # Check if as many hits as code is long
        if score[0] == self.code_length:
            self.win_message(score, attempts, board)
            return True
        else:
            return False

    def win_message(self, score, attempts, board):
        """
        Print win message
        """
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        board.show(attempts)
        print(
            f"\n {Fore.CYAN}{Style.BRIGHT}Congratulations, you WON!\n"
            f"{Style.RESET_ALL}\n You cracked the secret code "
            f"{self.screen.color_secret_code(self.secret_code)} in "
            f"{attempts} {'rounds' if attempts != 1 else 'round'}.\n"
        )
        time.sleep(1)
        print("")
        self.screen.press_enter()

    def check_max_rounds(self, attempts, board):
        """
        Check if has reached maximum attempts and call lose_message if yes
        Return True if lost and False if not
        """
        if attempts == self.max_rounds:
            self.lose_message(attempts, board)
            return True
        else:
            return False

    def lose_message(self, attempts, board):
        self.screen.clear_screen()
        self.screen.print_logo(self.screen.plain_text)
        board.show(attempts)
        print(f"{Fore.RED}\n You have run out of attempts.\n")
        time.sleep(1)
        print(
            " The secret code was "
            f"{self.screen.color_secret_code(self.secret_code)}.\n"
            )
        time.sleep(1)
        print("")
        self.screen.press_enter()

    def run_game(self):
        """
        Run game
        """
        self.game_welcome_message()
        # Reset to first round (1st attempt)
        attempts = 1
        # Create board instance
        board = Board(self.screen)
        # Game loop
        while True:
            self.screen.clear_screen()
            self.screen.print_logo(self.screen.plain_text)
            self.secret_code_description()
            # Print round number
            print(f" {Fore.CYAN}Round {attempts}:\n")
            # Show board
            if attempts > 1:
                board.show(attempts - 1)
            # If last round: show warning
            if attempts == self.max_rounds:
                print(f"\n {Fore.RED}Warning: This is your last chance!")
            # Create new guess, pass secret code, colors list, screen and
            # repetitions, take user_input() and check guess against secret
            latest_guess = Guess(
                self.secret_code,
                self.colors,
                self.screen,
                self.repetitions
            )
            # Save score
            latest_score = latest_guess.score
            # Add latest  guess to board
            board.append_guess(latest_guess)

            # Check break conditions
            if self.game_won(latest_score, attempts, board):
                break
            if self.check_max_rounds(attempts, board):
                break
            else:
                # Increment attempts
                attempts += 1


class Guess:
    """
    Create an instance of Guess
    """
    def __init__(self, secret, colors, screen, repetitions):
        self.secret = secret
        self.colors = colors
        # Call take_guess and check_guess each time a Guess is initialised
        self.guessed_code = self.take_guess(screen, repetitions)
        self.score = self.check_guess()

    def take_guess(self, screen, repetitions):
        """
        Take a guess from the user and validate for correct length, valid
        characters and repetitions allowed or not
        Return the guess once it is valid
        """
        while True:
            # Take user input, strip of empty spaces in beginning and end
            # Convert it to uppercase string
            guess = screen.user_input("\n Enter your guess: \n").strip().upper()  # noqa

            # Check that guess is not empty
            if not self.validate_guess_empty(guess):
                continue

            # Check that guess has correct length
            if not self.validate_guess_length(guess):
                continue

            # Check that guess only contains valid characters
            if not self.validate_guess_char(guess):
                continue

            # If repetitions are allowed: validation is completed and
            # break out of loop
            if repetitions is True:
                break
            else:
                # For levels where no repetitions allowed: validate for that
                if not self.validate_guess_repeat(guess):
                    continue
                else:
                    break

        return guess

    def validate_guess_empty(self, guess):
        """
        Check if guess is empty and print error message
        Return False if empty and True otherwise
        """
        if len(guess) == 0:
            print(
                f" {Fore.RED}Your guess is empty.\n"
                f" Please enter {len(self.secret)} "
                f"{'digits' if self.colors[0].isnumeric() else 'characters'} "
                f"{
                    f'between {self.colors[0]} and {self.colors[-1]}'
                    if self.colors[0].isnumeric()
                    else f'out of {", ".join(self.colors)}'
                }."
            )
            return False
        else:
            return True

    def validate_guess_length(self, guess):
        """
        Check if guess has correct length and print error message if not
        Return True if correct length and False otherwise
        """
        if len(guess) != len(self.secret):
            short_long = "short" if len(guess) < len(self.secret) else "long"
            print(
                f"{Fore.RED}\n Your guess '{guess}' is too {short_long}.\n"
                f" Please enter a code of length {len(self.secret)}."
            )
            return False
        else:
            return True

    def validate_guess_char(self, guess):
        """
        Check if guess only contains valid characters according to colors list
        Print error message if it contains invalid characters
        Return True if all valid characters and False otherwise
        """
        characters_valid = True
        for char in guess:
            if char not in [color for color in self.colors]:
                print(
                    f"{Fore.RED}\n Your guess '{guess}' contains "
                    f"invalid characters.\n Please enter "
                    f"{'digits' if self.colors[0].isnumeric() else 'characters'} "  # noqa
                    f"{
                        f'between {self.colors[0]} and {self.colors[-1]}'
                        if self.colors[0].isnumeric()
                        else f'out of {", ".join(self.colors)}'
                    }."
                )
                # When one character is invalid break out of loop
                # and return False
                characters_valid = False
                break

        return characters_valid

    def validate_guess_repeat(self, guess):
        """
        Check whether guess contains repeat colors for levels where
        repetitions are not allowed
        Return True if no repetitions and False otherwise
        """
        # Initialise variable repeat
        repeat = False
        guess_check_repeat = guess
        for char in guess:
            # Replace character to check by "." and check whether the
            # character is still contained in the string
            guess_check_repeat = guess_check_repeat.replace(char, ".", 1)
            if char in guess_check_repeat:
                # If a character repeats itself, set repeat to True
                # and break out of loop
                repeat = True
                break
        if repeat is True:
            print(
                f"\n {Fore.RED}Your guess '{guess}' contains repeating colors"
                f"/{'digits' if self.colors[0].isnumeric() else 'characters'}"  # noqa
                ".\n Please enter a code without repetitions."
            )
            return False
        else:
            return True

    def check_guess(self):
        """
        Check guess against the secret code, calculate number of hits and close
        Hit means correct character and position in the code
        Close means correct character but wrong position in the code
        Return hits and close
        """
        # Reset hits and close to 0 each time new guess is checked
        hits = 0
        close = 0
        secret_checked = self.secret
        guess_checked = self.guessed_code
        # Check for hits
        for i, char in enumerate(self.guessed_code):
            # When character is at correct position increment hits
            if char == self.secret[i]:
                hits += 1
                # Remove hits from guess so do not count twice
                guess_checked = guess_checked.replace(char, "", 1)
                # Replace checked character in secret by . so do not count
                # twice and positions of other characters stay the same
                secret_checked = secret_checked[:i] + "." + secret_checked[i + 1:]  # noqa
        # Check for close
        for char in guess_checked:
            if char in secret_checked:
                close += 1
                # Replace checked character in secret by . so don't count twice
                secret_checked = secret_checked.replace(char, ".", 1)

        return [hits, close]


class Board:
    """
    Create an instance of Board
    """
    def __init__(self, screen):
        # Initialize list of guesses and include board headings
        self.guess_list = [["Guess:", "Hits:", "Close:"]]
        # Pass instance of Screen
        self.screen = screen

    def append_guess(self, guess):
        """
        Append latest guess to the board
        """
        # Format guess for display on board and add color
        format_code = self.screen.color_secret_code(
            " ".join(list(guess.guessed_code))
            )
        # Append formatted guess and score to guess_list
        self.guess_list.append([format_code, guess.score[0], guess.score[1]])

    def show(self, rounds):
        """
        Print the board with nice formatting or for plain text mode
        Code inspiration from:
        https://learnpython.com/blog/print-table-in-python/
        """
        if self.screen.plain_text:
            # Print board for plain text mode
            headings = self.guess_list[0]
            for i, line in enumerate(self.guess_list[1:]):
                print(
                    f" Round {i + 1}{': ' if i < 9 else ':'}"
                    f" {headings[0]} {line[0]}, "
                    f"{headings[1]} {Fore.GREEN}{line[1]}{Fore.RESET}, "
                    f"{headings[2]} {Fore.YELLOW}{line[2]}"
                )
        else:
            # Print nicely formatted table
            rowIDs = [i for i in range(1, rounds + 1)]
            # Copy guess list to add color for score
            color_guess_list = self.guess_list.copy()
            # Loop through rows and add color to hits and close
            for row in color_guess_list[1:]:
                # Skip the headings
                row[1] = f"{Fore.GREEN}{row[1]}{Fore.RESET}"
                row[2] = f"{Fore.YELLOW}{row[2]}{Fore.RESET}"
            # Format list with tabulate and print
            print(tabulate(
                color_guess_list,
                headers='firstrow',
                tablefmt='rounded_outline',
                showindex=rowIDs
                ))


# Create and run game menu
menu = GameMenu()
menu.run_menu()
