from turtle import up
from GameFrame import Level, Globals
import pygame
from Objects.Character import Character
from Objects.Walls import Wall
import random
from Objects.Hacker import Hacker
from Objects.Ytroom import Ytroom
'''
from Objects.Hud import Score, Lives'''

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("grey_background.png")
        
        # Add player character
        self.add_room_object(Hacker(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/1.5))
        self.add_room_object(Character(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2))
        
        # Create maze walls (64x64 tiles)
        # Vertical walls (True)
        wall_positions = []
        
        start_block_y = 700
        start_block_x = 440
        most_recent_direction = None
        repeat = 1
        for x in range(4):
            for i in range(10):
                random_direction = random.choice(["up","left","right"])

                if random_direction == "up":
                    if most_recent_direction == "up" or most_recent_direction is None:
                        wall_positions.append((start_block_x, start_block_y + 64))
                        wall_positions.append((start_block_x, start_block_y + 128))
                        wall_positions.append((start_block_x, start_block_y + 192))
                        wall_positions.append((start_block_x + 192, start_block_y + 64))
                        wall_positions.append((start_block_x + 192, start_block_y + 128))
                        wall_positions.append((start_block_x + 192, start_block_y + 192))
                        start_block_y += 192

                    elif most_recent_direction == "left":
                        wall_positions.append((start_block_x, start_block_y + 64))
                        wall_positions.append((start_block_x, start_block_y + 128))
                        wall_positions.append((start_block_x, start_block_y + 192))
                        wall_positions.append((start_block_x - 192, start_block_y + 64))
                        wall_positions.append((start_block_x - 192, start_block_y + 128))
                        wall_positions.append((start_block_x - 192, start_block_y + 192))
                        wall_positions.append((start_block_x - 192, start_block_y))
                        wall_positions.append((start_block_x - 192, start_block_y-64))
                        wall_positions.append((start_block_x - 192, start_block_y-128))
                        wall_positions.append((start_block_x - 192, start_block_y-192))
                        wall_positions.append((start_block_x - 128, start_block_y-192))
                        wall_positions.append((start_block_x - 64, start_block_y-192))
                        start_block_y +=192
                        start_block_x -=192

                    elif most_recent_direction == "right":
                        wall_positions.append((start_block_x, start_block_y + 64))
                        wall_positions.append((start_block_x, start_block_y + 128))
                        wall_positions.append((start_block_x, start_block_y + 192))
                        wall_positions.append((start_block_x + 192, start_block_y+64))
                        wall_positions.append((start_block_x + 192, start_block_y+128))
                        wall_positions.append((start_block_x + 192, start_block_y+192))
                        wall_positions.append((start_block_x + 192, start_block_y))
                        wall_positions.append((start_block_x + 192, start_block_y-64))
                        wall_positions.append((start_block_x + 192, start_block_y-128))
                        wall_positions.append((start_block_x + 192, start_block_y-192))
                        wall_positions.append((start_block_x + 128, start_block_y-192))
                        wall_positions.append((start_block_x + 64, start_block_y-192))
                        start_block_y +=192

                    most_recent_direction = "up"

                if random_direction == "left":
                    if most_recent_direction == "up" or most_recent_direction is None:
                        wall_positions.append((start_block_x - 64, start_block_y))
                        wall_positions.append((start_block_x - 128, start_block_y))
                        wall_positions.append((start_block_x - 192, start_block_y))
                        wall_positions.append((start_block_x - 64, start_block_y + 192))
                        wall_positions.append((start_block_x - 128, start_block_y + 192))
                        wall_positions.append((start_block_x - 192, start_block_y + 192))
                        wall_positions.append((start_block_x +192, start_block_y + 64))
                        wall_positions.append((start_block_x +192, start_block_y + 128))
                        wall_positions.append((start_block_x +192, start_block_y + 192))
                        wall_positions.append((start_block_x + 128, start_block_y + 192))
                        wall_positions.append((start_block_x + 64, start_block_y + 192))
                        wall_positions.append((start_block_x, start_block_y + 192))
                        start_block_x -=192
                        start_block_y +=192
                        most_recent_direction = "left"

                    elif most_recent_direction == "left":
                        wall_positions.append((start_block_x - 64, start_block_y))
                        wall_positions.append((start_block_x - 128, start_block_y))
                        wall_positions.append((start_block_x - 192, start_block_y))
                        wall_positions.append((start_block_x - 64, start_block_y - 192))
                        wall_positions.append((start_block_x - 128, start_block_y - 192))
                        wall_positions.append((start_block_x - 192, start_block_y - 192))
                        start_block_x -=192
                        most_recent_direction = "left"

                    elif most_recent_direction == "right":
                        most_recent_direction = "right"

                if random_direction == "right":
                    if most_recent_direction == "up" or most_recent_direction is None:
                        wall_positions.append((start_block_x , start_block_y+ 64))
                        wall_positions.append((start_block_x , start_block_y+ 128))
                        wall_positions.append((start_block_x , start_block_y+ 192))
                        wall_positions.append((start_block_x + 64, start_block_y + 192))
                        wall_positions.append((start_block_x + 128, start_block_y + 192))
                        wall_positions.append((start_block_x + 192, start_block_y + 192))
                        wall_positions.append((start_block_x + 128, start_block_y + 192))
                        wall_positions.append((start_block_x + 64, start_block_y + 192))
                        start_block_x +=192
                        start_block_y +=192
                        most_recent_direction = "right"

                    elif most_recent_direction == "right":
                        wall_positions.append((start_block_x + 64, start_block_y))
                        wall_positions.append((start_block_x + 128, start_block_y))
                        wall_positions.append((start_block_x + 192, start_block_y))
                        wall_positions.append((start_block_x + 64, start_block_y - 192))
                        wall_positions.append((start_block_x + 128, start_block_y - 192))
                        wall_positions.append((start_block_x + 192, start_block_y - 192))
                        start_block_x +=192
                        most_recent_direction = "right"

                    elif most_recent_direction == "left":
                        most_recent_direction = "left"
            if repeat == 1:
                if most_recent_direction == "up" or most_recent_direction is None:
                        wall_positions.append((start_block_x, start_block_y + 64))
                        wall_positions.append((start_block_x, start_block_y + 128))
                        wall_positions.append((start_block_x, start_block_y + 192))
                        wall_positions.append((start_block_x + 192, start_block_y + 64))
                        wall_positions.append((start_block_x + 192, start_block_y + 128))
                        wall_positions.append((start_block_x + 192, start_block_y + 192))
                        start_block_y += 192

                elif most_recent_direction == "left":
                    wall_positions.append((start_block_x, start_block_y + 64))
                    wall_positions.append((start_block_x, start_block_y + 128))
                    wall_positions.append((start_block_x, start_block_y + 192))
                    wall_positions.append((start_block_x - 192, start_block_y + 64))
                    wall_positions.append((start_block_x - 192, start_block_y + 128))
                    wall_positions.append((start_block_x - 192, start_block_y + 192))
                    wall_positions.append((start_block_x - 192, start_block_y))
                    wall_positions.append((start_block_x - 192, start_block_y-64))
                    wall_positions.append((start_block_x - 192, start_block_y-128))
                    wall_positions.append((start_block_x - 192, start_block_y-192))
                    wall_positions.append((start_block_x - 128, start_block_y-192))
                    wall_positions.append((start_block_x - 64, start_block_y-192))
                    start_block_y +=192
                    start_block_x -=192

                elif most_recent_direction == "right":
                    wall_positions.append((start_block_x, start_block_y + 64))
                    wall_positions.append((start_block_x, start_block_y + 128))
                    wall_positions.append((start_block_x, start_block_y + 192))
                    wall_positions.append((start_block_x + 192, start_block_y+64))
                    wall_positions.append((start_block_x + 192, start_block_y+128))
                    wall_positions.append((start_block_x + 192, start_block_y+192))
                    wall_positions.append((start_block_x + 192, start_block_y))
                    wall_positions.append((start_block_x + 192, start_block_y-64))
                    wall_positions.append((start_block_x + 192, start_block_y-128))
                    wall_positions.append((start_block_x + 192, start_block_y-192))
                    wall_positions.append((start_block_x + 128, start_block_y-192))
                    wall_positions.append((start_block_x + 64, start_block_y-192))
                    start_block_y +=192
        
                most_recent_direction = "up"
                wall_positions.append((start_block_x, start_block_y + 64))
                wall_positions.append((start_block_x, start_block_y + 128))
                wall_positions.append((start_block_x, start_block_y + 192))
                wall_positions.append((start_block_x + 192, start_block_y + 64))
                wall_positions.append((start_block_x + 192, start_block_y + 128))
                wall_positions.append((start_block_x + 192, start_block_y + 192))
                start_block_y += 192
                wall_positions.append((start_block_x, start_block_y + 64))
                wall_positions.append((start_block_x, start_block_y + 128))
                wall_positions.append((start_block_x, start_block_y + 192))
                wall_positions.append((start_block_x + 192, start_block_y + 64))
                wall_positions.append((start_block_x + 192, start_block_y + 128))
                wall_positions.append((start_block_x + 192, start_block_y + 192))
                start_block_y += 192
                wall_positions.append((start_block_x, start_block_y + 64))
                wall_positions.append((start_block_x, start_block_y + 128))
                wall_positions.append((start_block_x, start_block_y + 192))
                wall_positions.append((start_block_x + 192, start_block_y + 64))
                wall_positions.append((start_block_x + 192, start_block_y + 128))
                wall_positions.append((start_block_x + 192, start_block_y + 192))
                start_block_y += 192
                self.add_room_object(Ytroom(self, start_block_x, start_block_y+64))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 64, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 128, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 192, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 256, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 320, False))
                self.add_room_object(Wall(self, start_block_x - 64, start_block_y + 384, False))
                self.add_room_object(Wall(self, start_block_x + 320 - 64, start_block_y, False))
                self.add_room_object(Wall(self, start_block_x + 384 - 64, start_block_y, False))
                self.add_room_object(Wall(self, start_block_x + 448 - 64, start_block_y, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 64, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 128, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 192, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 256, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 320, False))
                self.add_room_object(Wall(self, start_block_x + 512 - 64, start_block_y + 384, False))
                self.add_room_object(Wall(self, start_block_x + 448 - 64, start_block_y + 384, False))
                self.add_room_object(Wall(self, start_block_x + 384 - 64, start_block_y + 384, False))
                self.add_room_object(Wall(self, start_block_x + 320 - 64, start_block_y + 384, False))

                repeat +=1
                start_block_y += 320
                wall_positions.append((start_block_x, start_block_y + 64))
                wall_positions.append((start_block_x, start_block_y + 128))
                wall_positions.append((start_block_x, start_block_y + 192))
                wall_positions.append((start_block_x + 192, start_block_y + 64))
                wall_positions.append((start_block_x + 192, start_block_y + 128))
                wall_positions.append((start_block_x + 192, start_block_y + 192))
                start_block_y += 192

                
            

                          
        # Add vertical walls
            
        # Add horizontal walls
        for pos in wall_positions:
            self.add_room_object(Wall(self, pos[0], pos[1], False))