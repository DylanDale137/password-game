from GameFrame import Level, Globals
import pygame
from Objects.Character import Character
from Objects.Walls import Wall
'''
from Objects.Hud import Score, Lives'''

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        print("Here")
        # set background image
        self.set_background_image("grey_background.png")
        self.add_room_object(Character(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2))
        self.add_room_object(Wall(self, 240, 200, True))
        