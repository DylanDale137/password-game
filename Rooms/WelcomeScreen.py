from GameFrame import Level, Globals
from Objects.Title import Title
from Objects.Character import Character
from Objects.Walls import Wall
import pygame
from pygame.mixer import Sound


class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Start_frames\start000.png")
        
        # add title object
        self.add_room_object(Title(self, 0, 0))
        
        # load sounds
'''
# ...existing code...
class WelcomeScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.frame_rate = 0.2
        self.current_frame = 0
        self.total_frames = 8
        self.running = False

        self.image_frames = []
        for index in range(self.total_frames):
            self.image_frames.append(
                self.load_image(f"Start_frames\start{index:03}.png")
            )
        self.update_image()
        # don't call self.update_image() here — only start timer when animation begins

        self.handle_key_events = True

    def update_image(self):
        if self.running:
            if self.current_frame == 7:                              # reset the timer to call this method again after frame_rate game frames
                self.running = False
                self.set_timer(120, None)
            else:
                self.current_frame = (self.current_frame + 1) % self.total_frames                 # increment the frame number
        self.set_background_image(self.image_frames[self.current_frame])   # set the new image
        self.set_timer(self.frame_rate, self.update_image) # set the new image

    def key_pressed(self, key):
        # If your main loop passes pygame event objects:
        if key[pygame.K_SPACE]:
            if not self.running:
                self.running = True
                self.update_image()'''
# ...existing code...
'''class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.frame_rate = 1                         # frames change every 4 game frames
        self.current_frame = 0                   # start at frame 0
        self.total_frames = 8                    # total number of frames
        self.running = False

        # set image
        self.image_frames = []                                  # list to hold image frames
        for index in range(self.total_frames):                  # load each image frame from the Start_frames folder
            self.image_frames.append(
                self.load_image(f"Start_frames\start{index:03}.png")
            )                                           # dictionary to hold image frames by direction
        self.update_image()

        # register events
        self.handle_key_events = True

    def update_image(self):
        if self.running:
            self.current_frame = (self.current_frame + 1) % self.total_frames                 # increment the frame number
        self.set_background_image(self.image_frames[self.current_frame])   # set the new image
        self.set_timer(self.frame_rate, self.update_image)
        if self.current_frame == 7:                              # reset the timer to call this method again after frame_rate game frames
            self.running = False
            
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """

        if key[pygame.K_SPACE]:         
            self.running = True                 
        # set background image
        
        # add title object
        #self.add_room_object(Title(self, 240, 200))
        # load sounds'''
        

