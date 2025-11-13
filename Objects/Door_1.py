from GameFrame import RoomObject, Globals
import pygame
from Objects.Hud import Password_set_1, redo_pas_1

class Door_1(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.width = 64
        self.height = 64
        self.locked = False
        self.handle_key_events = True

        Globals.total_walls += 1
        self.update_image()
        

    def update_image(self):
        if self.locked == False:
            image = self.load_image(f"Door_frames\door008.png")
            self.set_image(image, 128, 256)
        else:
            
            image = self.load_image(f"Door_frames\door000.png")
            self.set_image(image, 128, 256)
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
        if self.y <= Globals.SCREEN_HEIGHT/2 - 320:
            if Globals.start == True:
                self.room.text.set_text()
                self.room.add_room_object(Password_set_1(self.room, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/1.8, ""))       
                Globals.start = False
                Globals.password_entering = True
            self.room.text.set_text()
        if self.y >= Globals.SCREEN_HEIGHT/2 - 320:
            if Globals.got_code:
                Globals.got_code = False
                Globals.redoing_pas = True
                self.room.text.set_text()
                self.room.add_room_object(redo_pas_1(self.room, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/1.8, ""))  