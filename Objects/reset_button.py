from GameFrame import RoomObject, Globals
import pygame
import random

class reset_button(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.width = 64
        self.height = 64
        self.handle_key_events = True
        self.register_collision_object("Character")
        Globals.total_walls += 1
        self.update_image()
    def update_image(self):
        if Globals.got_code:
            image = self.load_image("reset_button.png")
            self.set_image(image, 320 , 200)
        else:
            image = self.load_image("grey_background.png")
            self.set_image(image, 1, 1)
        
    def key_pressed(self, key):
        if key[pygame.K_w]:
            if Globals.hit_wall == "up":
                self.y -= 20
                Globals.num_of_walls_moved += 1
            elif Globals.current_direction == "up":
                self.y += Globals.character_speed
                
        if key[pygame.K_s]:
            if Globals.hit_wall == "down":
                self.y += 20
                Globals.num_of_walls_moved += 1
            elif Globals.current_direction == "down":
                self.y -= Globals.character_speed

        if key[pygame.K_a]:
            if Globals.hit_wall == "left":
                self.x -= 20
                Globals.num_of_walls_moved += 1
            elif Globals.current_direction == "left":
                self.x += Globals.character_speed

        if key[pygame.K_d]:
            if Globals.hit_wall == "right":
                self.x += 20
                Globals.num_of_walls_moved += 1
            elif Globals.current_direction == "right":
                self.x -= Globals.character_speed