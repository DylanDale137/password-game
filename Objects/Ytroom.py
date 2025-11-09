from GameFrame import RoomObject, Globals
import pygame

class Ytroom(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        print("Here")
        # set image
        image = self.load_image("rooms\youtube.png")
        self.set_image(image,448,320)
        
        # register for key events
        self.handle_key_events = True 
        Globals.total_walls += 1
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