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
