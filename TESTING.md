# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Python Code Validation

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate my Python file.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/mastermind/main/run.py) | ![screenshot](documentation/validation/validation-pep8.png) | |

## Browser Compatibility

I have tested my deployed project on the following browsers to check for compatibility issues.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)

| Browser | Start Screen | Game Menu | Instructions | Exit App from Menu | Level Menu | Level Introduction | Main Game Page | Game Won | Game Lost | Exit App From Input | Catch Keyboard Interrupt | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-start-screen.png) | ![screenshot](documentation/browsers/browser-chrome-game-menu.png) | ![screenshot](documentation/browsers/browser-chrome-instructions.png) | ![screenshot](documentation/browsers/browser-chrome-exit-goodbye.png) | ![screenshot](documentation/browsers/browser-chrome-level-menu.png) | ![screenshot](documentation/browsers/browser-chrome-level-intro.png) | ![screenshot](documentation/browsers/browser-chrome-main-game-page.png)![screenshot](documentation/browsers/browser-chrome-main-game-page-plain.png) | ![screenshot](documentation/browsers/browser-chrome-win-message.png) | ![screenshot](documentation/browsers/browser-chrome-lose.png) | ![screenshot](documentation/browsers/browser-chrome-exit.png) | ![screenshot](documentation/browsers/browser-chrome-keyboardinterrupt.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-start-screen.png) | ![screenshot](documentation/browsers/browser-firefox-game-menu.png) | ![screenshot](documentation/browsers/browser-firefox-instructions.png) | ![screenshot](documentation/browsers/browser-firefox-exit-goodbye.png) | ![screenshot](documentation/browsers/browser-firefox-level-menu.png) | ![screenshot](documentation/browsers/browser-firefox-level-intro.png) | ![screenshot](documentation/browsers/browser-firefox-main-game-page.png)![screenshot](documentation/browsers/browser-firefox-main-game-page-plain.png) | ![screenshot](documentation/browsers/browser-firefox-win-message.png) | ![screenshot](documentation/browsers/browser-firefox-lose.png) | ![screenshot](documentation/browsers/browser-firefox-exit.png) | ![screenshot](documentation/browsers/browser-firefox-keyboardinterrupt.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-start-screen.png) | ![screenshot](documentation/browsers/browser-edge-game-menu.png) | ![screenshot](documentation/browsers/browser-edge-instructions.png) | ![screenshot](documentation/browsers/browser-edge-exit-goodbye.png) | ![screenshot](documentation/browsers/browser-edge-level-menu.png) | ![screenshot](documentation/browsers/browser-edge-level-intro.png) | ![screenshot](documentation/browsers/browser-edge-main-game-page.png)![screenshot](documentation/browsers/browser-edge-main-game-page-plain.png) | ![screenshot](documentation/browsers/browser-edge-win-message.png) | ![screenshot](documentation/browsers/browser-edge-lose.png) | ![screenshot](documentation/browsers/browser-edge-exit.png) | ![screenshot](documentation/browsers/browser-edge-keyboardinterrupt.png) | Works as expected |

## Responsiveness

Since the whole frontend of this project is provided by the [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of the backend application in a modern web browser, it is not very useful to conduct extensive responsiveness testing. The relevant part of this project is the backend application which is displayed in the mock terminal and not the site that provides the mock terminal. 

However, the game is functional across most devices. It can be played without problems on Android mobile devices (even though responsiveness is lacking) but there are known issues with Apple mobile devices. On those, the user cannot input anything in the terminal and therefore the game cannot be played at all. See also the [Open Issues](#open-issues) section.

## Lighthouse Audit

For completeness I have tested my deployed site with the Lighthouse audit tool to check for any major issues. Note that the frontend of this project is not the relevant part.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Entire site | ![screenshot](documentation/lighthouse/lighthouse-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Feature | Expectation | Action | Outcome | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| **Start Screen** | When the page is loaded the start screen with a plain text mode request will open asking the user to enter 'y' or 'n' for plain text mode or not | Load the page | Start screen displayed when page loaded | Test concluded and passed | ![screenshot](documentation/features/feature-start-screen.png) |
| **Plain Text Mode** | When 'y'/'Y' is entered a plain text mode confirmation will be display and the user will be asked to press ENTER to continue the game | Enter 'y'/'Y' | Plain text confirmation displayed when 'y'/'Y' enterd | Test condluded and passed | ![screenshot](documentation/features/feature-plain-text-mode-selected.png) |
|  | When ENTER is pressed the plain text logo will be displayed on top of the screen | Press ENTER | Plain text logo displayed when ENTER is pressed | Test condluded and passed | ![screenshot](documentation/features/feature-logo-plain.png) |
|  | When 'n' or 'N' is entered below the plain text request ascii art logo will be displayed on top of the screen | Enter 'n'/'N' | Ascii art logo displayed when 'n'/'N' entered | Test concluded and passed | ![screenshot](documentation/features/feature-logo.png) |
| **Invalid Input**<br> in Plain Text Mode Request | When empty string is entered an error message will print and the input will be taken again | Enter an empty string | Error message printed and input taken again when empty string entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-plain-text-empty-string.png) |
|  | When letter different than 'y'/'n' is entered an error message will print and the input will be taken again | Enter 'a' | Error message printed and input taken again when different letter entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-plain-text-other-letter.png) |
|  | When number is entered an error message will print and the input will be taken again | Enter '3' | Error message printed and input taken again when number entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-plain-text-number.png) |
|  | When whole word and/or input including blank spaces is entered an error message will print and the input will be taken again | Enter '&nbsp; &nbsp; plain' | Error message printed and input taken again when whole word and/or input including blank spaces entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-plain-text-word.png) |
|  | When special character is entered an error message will print and the input will be taken again | Enter '?' | Error message printed and input taken again when special character entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-plain-text-special-char.png) |
| **Game Menu** | When viewing mode is selected the game menu will show and the user will be asked to choose between options 1 - 3 | Select viewing mode (see details above) | Game menu showed when viewing mode seleceted | Test concluded and passed | ![screenshot](documentation/features/feature-game-menu.png) |
| **Play Game Choice** | When option 1 - Play Game - is chosen ('1' is entered) level menu will show (see below) | Enter '1' | Level menu showed when '1' entered | Text concluded and passed | ![screenshot](documentation/features/feature-level-menu.png) |
| **Instructions Choice** | When option 2 - Show Instructions - is chosen ('2' is entered) the game instructions will be displayed until ENTER is pressed | Enter '2' | Instructions displayed when '2' entered | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-1.png)![screenshot](documentation/features/feature-instructions-2.png) |
|  | When ENTER is pressed game menu will be displayed again | Press ENTER | Game menu displayed again when ENTER pressed | Test concluded and passed | ![screenshot](documentation/features/feature-game-menu.png) |
| **Exit Choice** | When option 3 - Exit - is chosen ('3' is entered) below the game menu a goodbye message will show and the app will terminate | Enter '3' | Goodbye message showed and app terminated when '3' entered | Test concluded and passed | ![screenshot](documentation/features/feature-menu-exit-message.png)![screenshot](documentation/features/feature-good-bye-message.png) | 
| **Invalid Input**<br> in Game Menu Choice | When empty string is entered an error message will print and the input will be taken again | Enter an empty string | Error message printed and input taken again when empty string entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-game-menu-empty-string.png) |
|  | When number outside range 1 - 3 is entered an error message will print and the input will be taken again | Enter '5' | Error message printed and input taken again when number outside of 1 - 3 entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-game-menu-other-number.png) |
|  | When letter is entered an error message will print and the input will be taken again | Enter 'a' | Error message printed and input taken again when letter entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-game-menu-letter.png) |
|  | When whole word and/or input including blank spaces is entered an error message will print and the input will be taken again | Enter '&nbsp; &nbsp; three' | Error message printed and input taken again when whole word and/or input including blank spaces entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-game-menu-word.png) |
|  | When special character is entered an error message will print and the input will be taken again | Enter '?' | Error message printed and input taken again when special character entered | Test concluded and passed | ![screenshot](documentation/defensive-programming/defensive-game-menu-special-char.png) |
| **Level Menu** | When Level Menu is displayed the user will be asked to choose between options 1 - 3 | Choose 'Play Game' | User asked to choose between options 1 - 3 when 'Play Game' chosen | Test concluded and passed | ![screenshot](documentation/features/feature-level-menu.png) |
| **Level Choice 1** | When '1' is entered a level 1 introduction screen will show and the user will be asked to press ENTER | Enter '1' | Level 1 introduction screen shown when '1' entered | Test concluded and passed | ![screenshot](documentation/features/feature-level-menu-choice-confirmation.png)![screenshot](documentation/features/feature-level-intro-easy.png) |
| **Level Choice 2** | When '2' is entered a level 2 introduction screen will show and the user will be asked to press ENTER| Enter '2' | Level 2 introduction screen shown when '2' entered | Test concluded and passed | ![screenshot](documentation/features/feature-level-intro-classic.png) |
| **Level Choice 3** | When '3' is entered a level 3 introduction screen will show and the user will be asked to press ENTER | Enter '3' | Level 3 introduction screen shown when '3' entered | Test concluded and passed | ![screenshot](documentation/features/feature-level-intro-hard.png) |
| **Level Introduction** | When ENTER is pressed main game page will show according to chosen level | Press ENTER | Main game page shown when ENTER pressed | Test concluded and passed | ![screenshot](documentation/features/feature-main-game-page.png) |
| **Main Game Page** | 
| **Plain Text Main Game Page** | 
| **Secret Code description** | 
| **Round Display** | 
| **Board** | 
| **Plain Text Board** | 
| **Guess Input** | 
| **Last Round Warning** |
| **Game Won** | 
| **Game Lost** | 
| **Exit Game** |
| **Catch KeyboardInterrupt** | 
| **Exit Confirmation** |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user, I would like to play a game of mastermind that is functional and easy to control. | ![screenshot](documentation/features/feature-main-game-page.png) |
| As a user, I would like to choose a difficulty level. | ![screenshot](documentation/features/feature-level-menu.png) |
| As a user, I would like to get clear information on the secret code specifications. | ![screenshot](documentation/features/feature-level-intro-classic.png)![screenshot](documentation/features/feature-code-description-classic.png) |
| As a user, I would like to receive clear feedback in case a guess is not valid. | ![screenshot](documentation/defensive-programming/defensive-guess.png) |
| As a user, I would like to receive clear feedback on how close my guess is to the secret code. | ![screenshot](documentation/features/feature-board.png) |
| As a user, I would like to clearly see when I have lost a game. | ![screenshot](documentation/features/feature-lose-page-1.png)![screenshot](documentation/features/feature-lose-page-2.png) |
| As a user, I would like to clearly see when I won a game. | ![screenshot](documentation/features/feature-win-message-easy.png) |
| As a user, I would like to be able to exit the game when I want to. | ![screenshot](documentation/features/feature-menu-exit-message.png)![screenshot](documentation/features/feature-enter-exit.png)![screenshot](documentation/features/feature-catch-keyboard-interrupt.png) |
| As a user, I would like to avoid to accidentally quit the game. | ![screenshot](documentation/features/feature-exit-confirmation-request.png) |
| As a user, I would like to be able to access game instructions. | ![screenshot](documentation/features/feature-instructions-1.png)![screenshot](documentation/features/feature-instructions-2.png) |
| As a user, I would like to be able to select a plain text mode to bypass any visual elements. | ![screenshot](documentation/features/feature-plain-text-mode-selected.png)![screenshot](documentation/features/feature-main-game-page-plain.png) |

## Bugs

I have tracked my bugs with **GitHub Issues** :

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Atheresaabl%2Fsliding-puzzle%20label%3Abug&label=bugs)](https://github.com/theresaabl/mastermind/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

### Fixed Bugs

[![GitHub closed issues](https://img.shields.io/github/issues-closed/theresaabl/mastermind)](https://github.com/theresaabl/mastermind/issues?q=is%3Aissue+is%3Aclosed)

All previously closed/fixed bugs can be tracked [here](https://github.com/theresaabl/mastermind/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [ValueError when playing again after win](https://github.com/theresaabl/mastermind/issues/1) | Closed |
| [Game starts again automatically in level 1](https://github.com/theresaabl/mastermind/issues/2) | Closed |
| [Wrong level description for chosen level](https://github.com/theresaabl/mastermind/issues/3) | Closed |
| [check_guess is case sensitive for alphabetic secret code](https://github.com/theresaabl/mastermind/issues/4) | Closed |
| [clear_screen method only clears visible part in deployed version](https://github.com/theresaabl/mastermind/issues/5) | Closed |
| [User can still press Crtl + C in deployed application](https://github.com/theresaabl/mastermind/issues/6) | Closed |
| [ModuleNotFound error in deployed version ](https://github.com/theresaabl/mastermind/issues/7) | Closed |
| [UnboundLocalError when calling color_secret_code method to guess_list](https://github.com/theresaabl/mastermind/issues/8) | Closed |
| [User allowed to input repeat colors in level 3](https://github.com/theresaabl/mastermind/issues/9) | Closed |

## Open Issues

[![GitHub issues](https://img.shields.io/github/issues/theresaabl/mastermind)](https://github.com/theresaabl/mastermind/issues)

Remaining open issues can be tracked [here](https://github.com/theresaabl/mastermind/issues).

| Open Issue | Status |
| --- | --- |
| [Crtl + C crashes application when pressed while time.sleep is running](https://github.com/theresaabl/mastermind/issues/10) | Open |

See also the [Responsiveness](#responsiveness) section for a known issue with Apple mobile devices, where the user cannot input anything in the terminal.