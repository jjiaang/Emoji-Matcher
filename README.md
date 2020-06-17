# Emoji-Matcher
A simple game made for CPSC 231 \
![alt text](https://i.gyazo.com/54e96a8ace78f11492fb410078211f8a.png)

The game functions as a basic match 3 game, each emoji itself has a value of 1 point. Match 3 you get 3 points, a match of 4 nets you 4 points, etc.

You're given 15 turns, and you must score about 75 points to win. The game doesn't stop when you reach 75 points, as it only stops when you run out of turns. This is implemented so the player can try and get a high score.

# Overview
Requires the library stddraw and pygame to be installed by the user in order to run
```
python -m pip install -U pygame --user
```
# Installation guide for the booksite library (pygame, stddraw)
Download the booksite library provided the Princeton University. This will be provided in the respository, download this to your **downloads** folder. \
Extract the folder to the downloads folder on your computer, then open it 

Shift + right click in your extracted folder to open up this window, select **Open a command window here** 

![alt text](https://i.gyazo.com/aa05eecfb01da0c6d039adacc4c7ebf4.png) 

Then type in the command line
```
python setup.py install --user
```

To test that no errors have occured in the installation, open a new command prompt window and type the following commands.

First, load python by typing 
```
python
```
Then follow with
```
import stdio
```
If no errors have occured, you have successfully installed the booksite library correctly. 

# How to install
-Somehow get all of these files into the same directory.

# How to run 
-First, open up your command prompt or terminal, whichever one you use \
-Then, cd your directory of where the files are located
-Run the "Game.py" file through your command line, such as 
```
python game.py
```
