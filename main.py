import turtle   #used to create turtle objects


### Initialising Constants
gameplay = True

### Screen Setup
game_screen = turtle.Screen()   # Creates a new turtle object for the game screen
# Below defines the characteristics of the game screen
game_screen_size = 626
game_screen.setup(width=game_screen_size, height=game_screen_size)  # Creates a perfectly square game screen
game_screen.bgcolor("purple")

# Main Game Loop

while gameplay == True:
    game_screen.update()    # Updates Screen With Changes

  

import turtle   #used to create turtle objects




### Initialising Constants
gameplay = True

pause_until_input = "stop"  #prevents object from initially moving without user input
object_speed = 0    # this is the animation speed of the objects



### Screen Setup
game_screen = turtle.Screen()   # Creates a new turtle object for the game screen
# Below defines the characteristics of the game screen
game_screen_size = 626
game_screen.setup(width=game_screen_size, height=game_screen_size)  # Creates a perfectly square game screen
game_screen.bgcolor("purple")



### Mamba Setup
mamba_head = turtle.Turtle()    # Creates a new turtle object for the mamba head
# Below defines the characteristics of the mamba head
mamba_head.shape("square")
mamba_start_postiion = (0,0)    #will center the position of the mamba head
mamba_head.direction = pause_until_input
mamba_head.speed(object_speed)
mamba_head.goto(mamba_start_postiion)
mamba_head.penup()  # This prevents the mamba head from drawing anything as it moves, ie. leaving no trace


# Main Game Loop

while gameplay == True:
    game_screen.update()    # Updates Screen With Changes


