import pygame
from GameFrame import TextObject, Globals, RoomObject
# thx edward pookie
class Text_1(TextObject):
    def __init__(self, room, x, y, text=None):
        TextObject.__init__(self, room, x, y, text)
        
        self.size = 30
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
 
    
        



    def set_text(self):
        if Globals.start:
            change = "Traverse through your computer. Avoid the hacker"
            self.text = str(change)
        elif Globals.password_entering:
            change = "Enter a password hold enter when you are finished"
            self.text = str(change)
        self.update_text()
class Password_set_1(TextObject):
    def __init__(self, room, x, y, text=None):
        TextObject.__init__(self, room, x, y, text)
        
        self.size = 30
        self.font = 'Arial Black'
        self.colour = (0,120,120)
        self.bold = False
        self.update_text()
        self.handle_key_events = True
        Globals.FRAMES_PER_SECOND = 5
        self.depth = 10

    def set_text(self):
        self.text = str(Globals.password_1)
        self.update_text()
    def reset_key(self, can_reset):
        if not can_reset:
            self.key_imput = False
            self.set_timer(100, self.reset_key(True))
    def key_pressed(self, key):
        '''
        # Letters
        if key[pygame.K_a]:
            Globals.password_1 = Globals.password_1 + "a"
            self.set_text()
            print("a")
        # Special keys
        if key[pygame.K_SPACE]:
            Globals.password_1 = Globals.password_1 + " "
            self.set_text()
        if key[pygame.K_BACKSPACE]:
            Globals.password_1 = Globals.password_1[:-1]
            self.set_text()'''
        # Backspace
        if Globals.password_1_start:
            self.key_imput = False
            Globals.password_1_start = True

        # Space
        if key[pygame.K_RETURN]:
            Globals.FRAMES_PER_SECOND = 30
            self.room.door_1_spot.locked = True
            self.room.door_1_spot.update_image()
            print(Globals.password_1)
            Globals.pas_1_strength = len(Globals.password_1 * 15)
            print(Globals.pas_1_strength)
            self.room.delete_object(self)
            


        # Alphabetic keys A-Z
        # Check each letter; append with correct case depending on shift
        for i in range(ord('a'), ord('z') + 1):
            k = getattr(pygame, f'K_{chr(i)}')
            if key[k]:
                ch = chr(i)
                if self.key_imput == False:
                    Globals.password_1 = Globals.password_1 + ch
    
                    self.set_text()
                else:
                    
                    self.set_timer(100, self.reset_key(False))


        # Numeric keys 0-9 (top row)
        for i in range(0, 10):
            k = getattr(pygame, f'K_{i}')
            if key[k]:
                if self.key_imput == False:
                    Globals.password_1 = Globals.password_1 + str(i)
                    self.set_text()
                else:
                    
                    self.set_timer(100, self.reset_key(False))
        if key[pygame.K_BACKSPACE]:
            if self.key_imput == False:
                Globals.password_1 = Globals.password_1[:-1]
                self.set_text()
            else:
                
                self.set_timer(100, self.reset_key(False))
        