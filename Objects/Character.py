from GameFrame import RoomObject, Globals
import pygame

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
                self.load_image(f"Character_frames\character{i:03}.png", True)
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

        
           