# Rooms Folder

Rooms are stages or levels in the game. 

In the Rooms folder you put each level-stage-room of your game. 

For instance, the first room might be a maze, and when the player reaches the end of the maze they move into the next room which is a platform game. 

## `__init__.py` 

Inside folders there is a file called `__init__.py` It is this file that allows us to group files into different folders and still have the game know where to find everything. 

Whenever we add a file to a folder, we need to add an entry to the `__init__.py` file in the same folder to let the rest of the program know that the new file is there.

You will need to include code in this format

```python
from Rooms.FileName import ClassName
```

## Levels

In a game made with GameFrame, a room is the area in which a game is played. To have a game, there must be at least one room, but there can be many rooms, with the game progressing through different rooms. 

A room is defined and kept in the `Rooms` folder, and it is a type of GameFrame `Level`. As a room is a type of Level, every room has the attributes and functions of a Level, plus any defined for that room. 

To access the `Level` code, you need to import the file as follows: 

``` python
from GameFrame import Level
```

### Defining and Initialising a Room/Level:

``` python
class LevelName(Level): 
    def __init__(self, screen): 
        Level.__init__(self, screen)
```

### Variables 

#### `screen`

Passed to the Room/Level when started, the screen variable is a hook to the display area of the room.

#### `running` 

Level is active when true, level stops running due to being successfully complete when set to False 

#### `quitting` 

Level stops running and has not been successfully completed.

### Functions 

#### `set_background_image(image_file)` 

This function is called to set the background image of the level, where image_file is replaced by the name of an image in the Images folder. 

Example: 

``` python
self.set_background_image('background.jpg')
```

#### `set_background_scroll(speed)`

GameFrame provides this simple function call to set a scrolling background, such as those used for scrolling shooter games like 1942. The variable speed is the number of pixels moved every frame (Frames are set by default to 30 per second) 

Example: 

``` python
self.set_background_scroll(5)
```

#### `load_sound(sound_file)`

Read a sound file from the Sounds folder. Once read into a variable it can be played anytime by calling play() on the variable 

Example: 

``` python
self.explosion_sound = self.load_sound(‘explosion.wav’) 

self.explosion_sound.play()
```

#### `delete_object(obj)` 

Remove an object from the room. 

Example: 

``` python
self.room.delete_object(‘enemy_plane_1’)
```

#### `set_timer(ticks, function_call)`

When you want to set a timed event, you call the set_timer function providing the number of ticks (frames ticked over) and a function to call when the number of ticks is reached. 

For example, if I wanted to generate a new enemy character every 10 seconds, and the Frames per second is at the default setting of 30, I could write the call 

``` python
set_timer(300, create_new_enemy)
```

Within the function `create_new_enemy`, I could have that same line to repeatedly call itself every 10 seconds