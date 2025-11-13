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

class Hacker(RoomObject):

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
        self.register_collision_object("Door_1")
        self.register_collision_object("Ytroom")
        self.can_collide = True
        self.can_reset = False
        self.hacking = False

        # set image
        frames = []                                 # list to hold image frames
        for index in range(self.total_frames):      # load each image frame from the Hacker_frames folder
            frames.append(
                self.load_image(f"Hacker_frames\hacker_image{index:03}.png")
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
        self.set_image(self.image_frames[self.direction][self.current_frame], 50, 49)   # set the new image
        self.set_timer(self.frame_rate, self.update_image)                              # reset the timer to call this method again after frame_rate game frames
    '''def reset_moving(self, can_reset):
        if can_reset:
            self.hacking = False
            self.y += 256
            print("reset password")'''
    
        
    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        if other_type == "Wall":
            if self.direction == "down":
                
                if self.y < 0:
                    self.y += 5
                elif self.y > Globals.SCREEN_HEIGHT:
                    self.y += 5
                else:
                    self.y -= 5
            elif self.direction == "up":
                if self.y  < 0:
                    self.y -= 5
                elif self.y > Globals.SCREEN_HEIGHT:
                    self.y -= 5
                else:
                    self.y += 5
            elif self.direction == "left":
                if self.x < 0:
                    self.x -= 5
                elif self.x > Globals.SCREEN_WIDTH/1.5:
                    self.x -= 5
                else:
                    self.x += 5
            elif self.direction == "right":
                if self.x < Globals.SCREEN_WIDTH/2.4:
                    self.x += 5
                elif self.x > Globals.SCREEN_WIDTH/1.5:
                    self.x += 5
                else:
                    self.x -= 5
        if other_type == "Door_1":
            if not Globals.got_code:
                self.hacking = True
            '''self.moving = False
            self.direction = "down"
            
            self.update_image()
            self.set_timer(Globals.pas_1_strength, self.reset_moving(True))'''
        if other_type == "Ytroom" and self.hacking:
            self.y += 64
            self.hacking = False
            Globals.first_door = False
            Globals.cracked = True
            self.room.text.set_text()
                
            

                                




                
            
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]: 
               
            self.y += 5
            if Globals.hit_wall == "up":
                self.y -= 5
            if not self.hacking:
                if self.y > Globals.SCREEN_HEIGHT/2 and self.x > Globals.SCREEN_WIDTH/2:
                    self.y -= 3
                    self.x -= 3
                elif self.y > Globals.SCREEN_HEIGHT/2 and self.x < Globals.SCREEN_WIDTH/2:
                    self.y -= 3
                    self.x += 3
                elif self.y > Globals.SCREEN_HEIGHT/2 and self.x == Globals.SCREEN_WIDTH/2:
                    self.y -=3
                self.direction = "up"
                self.moving = True   
                
            else:
                self.y += 300 / Globals.pas_1_strength 
            
        elif key[pygame.K_s]:
            self.y -= 5
            if Globals.hit_wall == "down":
                self.y += 5
            if not self.hacking:
                if self.y < Globals.SCREEN_HEIGHT/2 and self.x > Globals.SCREEN_WIDTH/2:
                    self.y += 3
                    self.x -= 3
                elif self.y < Globals.SCREEN_HEIGHT/2 and self.x < Globals.SCREEN_WIDTH/2:
                    self.y += 3
                    self.x += 3
                elif self.y < Globals.SCREEN_HEIGHT/2 and self.x == Globals.SCREEN_WIDTH/2:
                    self.y +=3
                self.direction = "down"
                self.moving = True  
                
            else:
                self.y += 300 / Globals.pas_1_strength
            


        elif key[pygame.K_a]:
            self.x += 5
            if Globals.hit_wall == "left":
                self.x -= 5
            if not self.hacking:
                if self.x > Globals.SCREEN_WIDTH/2 and self.y > Globals.SCREEN_HEIGHT/2:
                    self.x -= 3
                    self.y -= 3
                elif self.x > Globals.SCREEN_WIDTH/2 and self.y < Globals.SCREEN_HEIGHT/2:
                    self.x -= 3
                    self.y += 3
                elif self.x > Globals.SCREEN_WIDTH/2 and self.y == Globals.SCREEN_HEIGHT/2:
                    self.x -=3
                self.direction = "left"
                self.moving = True
                
            else:
                self.y -= 300 / Globals.pas_1_strength
            
        elif key[pygame.K_d]:
            self.x -= 5
            if Globals.hit_wall == "right":
                self.x += 5
            if not self.hacking:
                if self.x < Globals.SCREEN_WIDTH/2 and self.y > Globals.SCREEN_HEIGHT/2:
                    self.x += 3
                    self.y -= 3
                
                elif self.x < Globals.SCREEN_WIDTH/2 and self.y < Globals.SCREEN_HEIGHT/2:
                    self.x += 3
                    self.y += 3
                elif self.x < Globals.SCREEN_WIDTH/2 and self.y == Globals.SCREEN_HEIGHT/2:
                    self.x +=3
                self.direction = "right"
                self.moving = True
                
            else:
                self.y += 300 / Globals.pas_1_strength
            
        else:
            if not self.hacking:
                if self.x == Globals.SCREEN_WIDTH/2 and self.y == Globals.SCREEN_HEIGHT/2:
                    self.moving = False
                    self.current_frame = 0

                elif self.x > Globals.SCREEN_WIDTH/2 and self.y > Globals.SCREEN_HEIGHT/2:
                    self.x -= 3
                    self.y -= 3
                elif self.x < Globals.SCREEN_WIDTH/2 and self.y > Globals.SCREEN_HEIGHT/2:
                    self.x += 3
                    self.y -= 3

                elif self.x > Globals.SCREEN_WIDTH/2 and self.y < Globals.SCREEN_HEIGHT/2:
                    self.x -= 3
                    self.y += 3
                elif self.x < Globals.SCREEN_WIDTH/2 and self.y < Globals.SCREEN_HEIGHT/2:
                    self.x += 3
                    self.y += 3
                elif self.x < Globals.SCREEN_WIDTH/2 and self.y == Globals.SCREEN_HEIGHT/2:
                    self.x +=3
                elif self.x > Globals.SCREEN_WIDTH/2 and self.y == Globals.SCREEN_HEIGHT/2:
                    self.x -=3
                elif self.y < Globals.SCREEN_HEIGHT/2 and self.x == Globals.SCREEN_WIDTH/2:
                    self.y +=3
                elif self.y > Globals.SCREEN_HEIGHT/2 and self.x == Globals.SCREEN_WIDTH/2:
                    self.y -=3
            else:
                self.y += 300 / Globals.pas_1_strength