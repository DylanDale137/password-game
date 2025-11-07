from GameFrame import RoomObject, Globals
import pygame
import random

class Wall(RoomObject):

    def __init__(self, room, x, y, can_summon):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("wall.png")
        self.set_image(image,64,64)
        self.width = 64
        self.height = 64
        self.can_summon = can_summon
        
    def key_pressed(self):
        if Globals.current_direction == "up":
            self.y += Globals.character_speed 
        elif Globals.current_direction == "down":
            self.y -= Globals.character_speed
        elif Globals.current_direction == "left":
            self.x += Globals.character_speed
        elif Globals.current_direction == "right":
            self.x -= Globals.character_speed 
    def creating_room(self):
        if self.can_summon:
            random_direction = random.choice(["up"])
            if random_direction == "up":
                self.room.add_room_object(Wall(self.room, self.x, self.y + self.height, False))
                self.room.add_room_object(Wall(self.room, self.x, self.y + (self.height*2), True))
                self.room.add_room_object(Wall(self.room, self.x + (self.width*2), self.y + self.height, False))
                self.room.add_room_object(Wall(self.room, self.x - (self.width*2), self.y + (self.height*2), False))