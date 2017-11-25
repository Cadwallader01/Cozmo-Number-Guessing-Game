# Cozmo-Number-Guessing-Game
This project uses a robot by Anki named Cozmo. Cozmo asks the user if they can guess a number he is thinking of from 1-10 and gives them three tries. Cozmo will use his cubes to show the user how many guesses they have left by initializing his cubes to the color blue but then changing each one red after every failed guess by the user as well as changing his face to show a big 'X' mark. Once all the cubes are red the game is over.

If the user guesses the correct number before the amount of tries they have are all gone then Cozmo will tell them they are correct, change his face to display a check mark, and do a little celebratory dance as well as make all his cubes change colors multiple times. At the very end he will raise his lift to the upmost position and all his cubes will turn green.

Currently, the SDK must be used to program with Cozmo so the SDK installation has to be downloaded as well as the Android/iPhone app for Cozmo before program will run.

The Setup:
1. Download the Android/iPhone app as well as the SDK from the following link http://cozmosdk.anki.com/docs/initial.html
2. Save the pictures "check_rightAnswer" and "x_wrongAnswer" to a directory that will be used to display a checkmark or a 'X' on Cozmo's
   face when the user response is right or wrong.
