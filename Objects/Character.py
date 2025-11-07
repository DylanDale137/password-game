from GameFrame import RoomObject, Globals
import pygame
'''
class Character(RoomObject):

    def __init__(self, room, x, y):
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        self.frame_rate = 4
        self.current_frame = 0
        self.total_frames = 16
        self.num_frames = 4
        self.direction = "down"
        self.moving = False

        frames = []
        for i in range(self.total_frames):
            frames.append(
                self.load_image(f"Character_frames\character{i:03}.png")
            )

        self.image_frames = {
            "down": frames[0:4],
            "up": frames[4:8],
            "left": frames[8:12],
            "right": frames[12:16],
        }
        self.update_image()

        self.handle_key_events = True

    def update_image(self):
        if self.moving:
            self.current_frame = (self.current_frame + 1) % self.num_frames
        else:    
            self.current_frame = 0
        self.set_image(self.image_frames[self.direction][self.current_frame], 100, 98)
        self.set_timer(self.frame_rate, self.update_image)
    
    def key_pressed(self, key):
        if key == pygame.K_w or key == pygame.K_UP:
            self.direction = "up"
            self.moving = True
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.direction = "down"
            self.moving = True
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.direction = "left"
            self.moving = True
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.direction = "right"
            self.moving = True
        else:
            self.moving = False
            self.current_frame = 0
'''

class Character(RoomObject):

    def __init__(self, room, x, y):
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set animation values
        self.frame_rate = 4                         # frames change every 4 game frames
        self.current_frame = 0                      # start at frame 0
        self.total_frames = 16                      # total number of frames
        self.num_frames = 4                         # total number of frames per direction
        self.direction = "down"                     # initial direction
        self.moving = False
        self.register_collision_object("Wall")
        

        # set image
        frames = []                                 # list to hold image frames
        for index in range(self.total_frames):      # load each image frame from the Character_frames folder
            frames.append(
                self.load_image(f"Character_frames\character{index:03}.png")
            )
        self.image_frames = {
            "down": frames[0:4],
            "up": frames[4:8],
            "left": frames[8:12],
            "right": frames[12:16]
        }                                           # dictionary to hold image frames by direction
        self.update_image()

        # register events
        self.handle_key_events = True

    def update_image(self):
        if self.moving:
            self.current_frame = (self.current_frame + 1) % self.num_frames                 # increment the frame number
        self.set_image(self.image_frames[self.direction][self.current_frame], 100, 98)   # set the new image
        self.set_timer(self.frame_rate, self.update_image)                              # reset the timer to call this method again after frame_rate game frames
     
    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        if other_type == "Wall":
            if Globals.current_direction == "up":
                Globals.hit_wall = "up"
            elif Globals.current_direction == "down":
                Globals.hit_wall = "down"
            elif Globals.current_direction == "left":
                Globals.hit_wall = "left"
            elif Globals.current_direction == "right":
                Globals.hit_wall = "right"
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """

        if key[pygame.K_w]:         
            self.moving = True                          # character is moving
            self.direction = "up"                       # set direction to up
            Globals.current_direction = "up"
            
        elif key[pygame.K_s]:
            self.moving = True                          # character is moving
            self.direction = "down"                     # set direction to down
            Globals.current_direction = "down"

        elif key[pygame.K_a]:
            self.moving = True                          # character is moving
            self.direction = "left"                     # set direction to left
            Globals.current_direction = "left"

        elif key[pygame.K_d]:
            self.moving = True                          # character is moving
            self.direction = "right"                     # set direction to right
            Globals.current_direction = "right"
            
            
        else:
            self.moving = False                         # no movement
            self.current_frame = 0                      # reset to first frame
            Globals.current_direction = None
           