# Objects Folder

This is where you put all the individual parts (objects) of your game. 

For instance, you could make a player that has an image (from the Images folder) and moves across the screen if the arrow buttons are pressed. 

The player would be one object in the game. An enemy, wall, bouncing ball etc. could be other objects.

## `__init__.py` 

Inside folders there is a file called `__init__.py` It is this file that allows us to group files into different folders and still have the game know where to find everything. 

Whenever we add a file to a folder, we need to add an entry to the `__init__.py` file in the same folder to let the rest of the program know that the new file is there.

You will need to include code in this format

```python
from Objects.FileName import ClassName
```

## RoomObject 

Everything that placed inside a Room, must be a `GameFrame` `RoomObject` (A `TextObject` is also a type of `RoomObject`). You define room objects in the “Objects” folder, and each object is a type of `GameFrame` `RoomObject`. 

As each file in the Objects folder is a type of `RoomObject`, each has the attributes and functions of a `RoomObject`, plus any defined for that file. 

To access the `RoomObject’` code, you need to import the file as follows: 

``` python
from GameFrame import RoomObject
```

### Defining and Initialising a Room Object 

``` python
class Name_of_Object(RoomObject): 
    def __init__(self, room, x, y): 
        RoomObject.__init__(self, room, x, y)
```

### Variables

#### `Room` 

A hook to the room the object is in. 

#### `Depth` 

The layer the object is situated in. When two objects occupy the same space, the object with the higher depth value will be shown, the object with the lower depth value will be covered. 

#### `x` 

The current horizontal position of the object, taken at the top left hand corner of the image 

#### `y` 

The current vertical position of the object, taken at the top left hand corner of the image 

#### `rect` 

The bounding rectangle. That is, a rectangle that encompasses the image. Used for collision detection. 

#### `prev_x` 

The previous horizontal position of the object, taken at the top left hand corner of the image 

#### `prev_y` 

The previous vertical position of the object, taken at the top left hand corner of the image 

#### `width` 

The width in pixels, of the object image 

#### `height` 

The height in pixels, of the object image 

#### `image` 

The current image of the object 

#### `x_speed` 

The number of pixels the object is moving in the horizontal direction every frame. Positive numbers indicate a move to the right, negative numbers indicate a move to the left. 

#### `y_speed`

The number of pixels the object is moving in the vertical direction every frame. Positive numbers indicate a move down, negative numbers indicate a move up. 

#### `gravity`

The gravity is a number that is used to determine the amount of gravity exerted on an object. The higher the number, the greater effect of falling the object has. 

#### `handle_key_events`

Set to `False` by default, this variable determines whether an object is notified of keyboard presses. To listen for key events, set this variable to `True` 

#### `handle_mouse_events` 

Set to `False` by default, this variable determines whether an object is notified of mouse presses and movement. To listen for mouse events, set this variable to `True` 

### Functions 

#### `load_image(file_name)`

Retrieve and image from file. 

#### `set_image(image, width, height)`

Set the objects image by providing the image itself as well as its width and height in pixels. 

#### `delete_object(obj)`

Remove an object from the room. 

Example: 

``` python
self.delete_object(‘enemy_plane_1’)
```

#### `register_collision_object(collision_object)` 

For an object to be notified of collisions with other objects, it must register to listen for collisions with a given object type. You can register for multiple object types. 

Example: 

``` python
self.register_collision_object(‘enemy’) 
```

#### `def handle_collision(self, other)` 

When a collision is registered, the object will be notified of any such event by calling its `handle_collision` function. 

To write the code that needs to run in a collision event, the object needs to implement the function. 

Example: 

``` python
def handle_collision(self,other): 
    self.bounce(other) 
```

#### `def key_pressed(self, key)` 

If the variable `handle_key_events` is set to `True`, the object will be notified of any key presses by calling its `key_pressed` function. To write the code that needs to run in a key press event, the object needs to implement the function. The key identity will be supplied as the variable `key`. 

Example:

``` python
def key_pressed(self, key): 
    if key[pygame.K_LEFT]:
        self.x -= 4 
    elif key[pygame.K_RIGHT]: 
        self.x += 4 
    elif key[pygame.K_UP]: 
        self.y -= 4 
    elif key[pygame.K_DOWN]: 
        self.y += 4 
```

#### `def clicked(self, button_number)` 

If the variable `handle_mouse_events` is set to `True`, the object will be notified of any mouse key presses by calling its clicked function. To write the code that needs to run in a mouse key press event, the object needs to implement the function. The mouse button identity will be supplied as the variable `button_number` 

Example: 

``` python
def clicked(self, button_number): 
    # - Check for a left mouse button click - # 
    if button_number == 1: 
        self.delete_object(self) 
```

#### `def mouse_event(self,mouse_x,mouse_y,button_left,button_middle,button_right)` 

If the variable `handle_mouse_events` is set to `True`, the object will be notified of any mouse event by calling its mouse_event function. To write the code that needs to run in a mouse event, the object needs to implement the function. The mouse `x` and `y` position will be supplied as well as the buttons information 

Example: 

``` python
def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right): 
    self.x = mouse_x 
    self.y = mouse_y
```

#### `bounce(other)` 

A convenience function that makes the current object bounce off of another object. The other object is provided as the variable `other` 

#### `blocked(other)` 

A convenience function that makes the current object blocked by another object. The other object is provided as the variable `other` 

## TextObject

The `TextObject` is a type of `RoomObject`. It has all the same attributes of a `RoomObject`, but specialises in displaying text. The text can be set to various sizes and colours as well as specifying a given font type. To access the `TextObject`’ code, you need to import the file as follows: 

``` python
from GameFrame import TextObject
```

### Defining and Initialising a Text Object

``` python
class Name_of_TextObject(TextObject): 
    def __init__(self, room, x, y, 
                 text='Not Set', 
                 size=60,
                 font='Comic Sans MS', 
                 colour=(0, 0, 0), 
                 bold=False): 
        RoomObject.__init__(self, room, x, y) 
```

### Variables 

#### `text` 

The text that will be used for the `TextObject` when the function `update_text()` is called. 

#### `size` 

The font size of the text when rendered 

#### `font` 

The font type for the text when rendered. ie. ‘Sans Serif’, ‘Comic Sans MS’ 

#### `colour` 

The colour of the text when rendered 

#### `bold` 

Set to `False` by default, this will set the text to bold if `True`. 

### Functions

#### `update_text()` 

This function must be called for any changes to the object variable to take effect.