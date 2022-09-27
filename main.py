from settings import Settings
from player import Player
from game import Game
import os
import sys

"""
MAIN FILE
- execute this file
- for VSC: template includes launch.json file which includes line '"program": "main.py",' -> always launch this file
"""

if __name__ == "__main__":
    os.chdir(sys.path[0]) # changes current working directory to file directory

    # define some settings
    settings_default = Settings()
    settings_slow = Settings(speed=1)

    

    # create game object and play
    game = Game(settings_default)
    game.play()
