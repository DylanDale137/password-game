from GameFrame import RoomObject, Globals
import pygame

class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Start_frames\start008.png")
        self.set_image(image,1460,880)
        
        # register for key events
        self.handle_key_events = True 
        
    def key_pressed(self, key):
        """
        If the key pressed is space the game will start
        """
       
        if key[pygame.K_SPACE]:
            self.room.running = False
        
    