# Computer Vision RPS

Table of Contents:
converted_keras: This folder contains the keras_model.h5 file and labels.txt file. These contain the structure and parameters of a deep learning model. These are to be used in the python file as part of this project.

Project Description:
To use a combination of machine learning and python programming to develop a game of rock, paper, scissors.
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

Useage instructions: Run the camera_rps.py file in the activated conda environment. Ensure the correct terminal is used - This can be done by pressing Ctrl + Shift + P and then searching for 'Python Interpreter'. Ensure the one with the activated conda environment is selected, for example: mycondaenv.
Now you can run the file and follow the instructions displayed in the terminal. An image will be captured of you with a hand gesture to be taken as your choice. This will be compared with the computers choice and a user decided. First to 3 wins, wins!

File structure of the project:
converted_keras: This folder contains the keras_model.h5 file and labels.txt file. These contain the structure and parameters of a deep learning model. These are to be used in the python file as part of this project.

manual_rps.py: This file contains the code to run a manual game of rock paper scissors, whereby the computer chooses a random option and the user inputs an option. Then a winner/loser is decided and displayed. If it is a tie, then the result is displayed as a tie.

model_check.py: This file contains the code to verify that the imported impage model project works correctly.

camera_rps.py: Fully developed game of Rock, Paper, Scissors whereby the webcam is used to capture the users hand gesture and translate it into the users guess, and the computer randomly picks an option. The rounds are played until 3 wins are recorded for the winner!

README.md: File containing the documentation and experience of the project.
