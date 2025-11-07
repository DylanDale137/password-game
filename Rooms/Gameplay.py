from GameFrame import Level, Globals
'''
from Objects.Hud import Score, Lives'''

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("grey_background.png")
        