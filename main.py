import turtle   #used to create turtle objects
import random   #used to create random x,y co-ordinates for objects
import time     #used to delay execution of code



### Initialising Constants
gameplay = True
wait_before_reloop = 0.15
pause_until_input = "stop"  #prevents object from initially moving without user input
default_object_size = 20




## Intial Values For Variables
remaining_lives = 0
object_speed = 0    # this is the animation speed of the objects
impact_zone = 20     # In Python Turtle Graphics, Objects are 20px in Size...
                        # Therefore the distance between the centre of an object from the outer is 10px..
                        # Therefore if the distance between the centres of two objects is 20 (or smaller)
                        # That means the object are overlapping and have impacted


### Screen Setup
game_screen = turtle.Screen()   # Creates a new turtle object for the game screen
# Below defines the characteristics of the game screen
game_screen_size = 626
game_screen.setup(width=game_screen_size, height=game_screen_size)  # Creates a perfectly square game screen
game_screen.bgcolor("purple")
game_screen.tracer(0) #Ignores built in turtle animations by ignoring screen updates



### Mamba Setup
mamba_head = turtle.Turtle()    # Creates a new turtle object for the mamba head
# Below defines the characteristics of the mamba head
mamba_head.shape("square")
mamba_start_postiion = (0,0)    #will center the position of the mamba head
mamba_head.direction = pause_until_input
mamba_head.speed(object_speed)
mamba_head.goto(mamba_start_postiion)
mamba_head.penup()  # This prevents the mamba head from drawing anything as it moves, ie. leaving no trace


### Regular Block Setup
regular_block = turtle.Turtle() # Creates a new turtle object for the regular blocks
# Below defines the characteristics of the regular block
regular_block.shape("circle")
regular_block.speed(object_speed)
regular_block_x = random.randint(-(game_screen_size/2), (game_screen_size/2)) #division by two as it calculates position..
regular_block_y = random.randint(-(game_screen_size/2), (game_screen_size/2))#.. from the center of the screen
regular_block.penup()   # This prevents the regular block from drawing anything as it moves, ie. leaving no trace
regular_block.goto(regular_block_x,regular_block_y)
regular_block.color("red")

## Keyboard Functions (to Move mamba)
#### the != statments are used to provide self impact due to the mabma head reversing into extentions
### to be created later.
def turn_left():
    if mamba_head.direction != "right":
        mamba_head.direction = "left"

def turn_right():
    if mamba_head.direction != "left":
        mamba_head.direction = "right"

def move_upwards():
    if mamba_head.direction != "down":
        mamba_head.direction = "up"

def move_downwards():
    if mamba_head.direction != "up":
        mamba_head.direction = "down"


def maneuver():
    ## this function cause the mamba head to manoeuvre
    if mamba_head.direction == "up":
        mamba_head.sety(mamba_head.ycor() + default_object_size)

    if mamba_head.direction == "down":
        mamba_head.sety(mamba_head.ycor() - default_object_size)

    if mamba_head.direction == "left":
        mamba_head.setx(mamba_head.xcor() - default_object_size)

    if mamba_head.direction == "right":
        mamba_head.setx(mamba_head.xcor() + default_object_size)


### Key Mappings (Bellow Maps the Key's Passed to Function)...
### which will allow the player to control the mamba head
game_screen.onkeyrelease(turn_left, "Left")
game_screen.onkeyrelease(turn_right, "Right")
game_screen.onkeyrelease(move_upwards, "Up")
game_screen.onkeyrelease(move_downwards, "Down")

# Main Game Loop

while gameplay == True:
    game_screen.listen()    # Listens for key changes
    game_screen.update()    # Updates Screen With Changes


    ### Regular Block Impact Check
    if impact_zone > mamba_head.distance(regular_block):
        # Move Regular Block to Random Position After Impact
        # Division by two as it calculates position from the center of the screen
        random_regular_block_x = random.randint(-(game_screen_size / 2), (game_screen_size / 2))
        random_regular_block_y = random.randint(-(game_screen_size / 2), (game_screen_size / 2))
        regular_block.goto(random_regular_block_x, random_regular_block_y)
        # Updating lives
        remaining_lives = remaining_lives + 1



    maneuver()   #calls function to ensure the mamba moves


    print(remaining_lives)
    time.sleep(wait_before_reloop)  #make the loop wait before re-looping so that all prior loops can be completed.
