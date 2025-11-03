from GameFrame import Level

import pygame
from pygame.mixer import Sound

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        #self.set_background_image("start.png")
        
        # add title object
        # self.add_room_object(Title(self, 240, 200))
        # load sounds
        

