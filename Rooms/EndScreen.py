from GameFrame import Level, Globals
from Objects.Title import Title


class EndScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        if Globals.won:    
            self.set_background_image("win_screen.png")
        else:
            self.set_background_image("lose_screen.png")
        self.add_room_object(Title(self, -3000, 0))
        # add title object
