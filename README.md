# Last Battleship

Last Battleship is a Python terminal game where users can challenge the computer
by destroying all their ships in 10 guesses. Underneath is a live preview.

![Live preview of my project](assets/images/livepreview.png "live preview")

## How to play

Last Battlship is based on the original battleship game but with some diffrences.

In this version a guessing board, showing your guesses is generated for the user and another hidden one is created for the computer. 

You have 10 guesses to shoot down all of the enemy ships and after your game will end.  

If you hit all 5 ships it will print that you won the game and the game will end. 

Misses are marked with * and hits with X 

## Features
- Random board generation
    - Ships are randomly generated on the hidden computer board
    - Guess board generated to show your guesses 
- Rules 
    - Game rules will be printed out on the terminal

![Screenshot of rules](assets/images/rules.png "Rules for the game")

- Play against the computer
- Accepts user inputs

![Screenshot of user input](assets/images/input.png "Asking for input")
- Count guesses and show how many are left 
- Input validation and error-checking
    - Cannot input number larger than 5
    - Must input a number 
    - Can not enter same guess twice  
![Screenshot of error checks](/assets/images/errorchecks.png "Error checks")

- Future Features
    - Make another board user and let computer guess user ship location 
    - User can choose themselves where they want the ships to be 
    
## Running Tests
- Passed the code through PEP8 linter and only problem is trailing whitespace
- Given invalid inputs: same input twice, a string when numbers is expected, out of bounds input 
- Tested in local terminal and the Code Institute Heroku terminal

## Bugs
- My if statment on line 95 I put in the same value as when the rounds were defined and because it supposed to count down from 10 to 0 it didn't work until I switched it to 0.
- Forgot to add a "-" to hidden board on line 84
- Acceptence of empty/invalid input causes the application to crash.

## Validator Testeing
- PEP8
    - Only error showing is trailing whitespace which doesn't seem to affect the functianlity of the code 

## Deployment
I used Code Institute's mock terminal for Heroku to deploy this project.
- Steps for deployment 
    - Go to Heroku and create a new app
    - Choose GitHub as your deployment method
    - Choose your profile and write the name of the repository you want to deploy
    - Click deploy and wait until it has finished building 
    
## Credits 

- Took inspiratons from https://github.com/gbrough/battleship/blob/main/single_player.py for print_board, create_ships and hit_ships functions

