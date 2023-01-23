import turtle   #used to create turtle objects
import random   #used to create random x,y co-ordinates for objects
import time     #used to delay execution of code
import os       #used to enable sound effects


### Initialising Constants
gameplay = True
wait_before_reloop = 0.15
pause_until_input = "stop"  #prevents object from initially moving without user input
default_object_size = 20
to_display_message = 1  #length of time in seconds to delay execution of code
winning_music_path = "../PR1GameDenzelandFudail/luckyblocksucess.mp3"
lose_music_path = "../PR1GameDenzelandFudail/noluckyblocksucess.mp3"
player_life_lost_path = "../PR1GameDenzelandFudail/collsioncauselifelost.mp3"



## Intial Values For Variables
players_score = 0
remaining_lives = 0
game_lost = 0
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
outside_game_screen = game_screen_size*2    # Creates values needed to remove mamba extensions from screen
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


### Lucky Block Setup
lucky_block = turtle.Turtle()   # Creates a new turtle object for the turtle object
# Below defines the characteristics of the lucky block
lucky_block.shape("circle")
lucky_block.color("yellow")
lucky_block.speed(object_speed)
lucky_block_x = random.randint(-(game_screen_size/2), (game_screen_size/2))#division by two as it calculates position..
lucky_block_y = random.randint(-(game_screen_size/2), (game_screen_size/2))#.. from the center of the screen
lucky_block.penup()     # This prevents the lucky block from drawing anything as it moves, ie. leaving no trace
lucky_block.goto(lucky_block_x, lucky_block_y)
lucky_blocks_collected = 0
timer = []  #Creates an empty list that will will grow in size recursively...
            # and be used to mimic functionality of a timer
hide_lucky_block_at  = [40] #x3
show_lucky_block_at = [80] #1.5


## Game Metrics Setup
game_metrics = turtle.Turtle()  # Creates a new turtle object to display the game metrics
# Below defines the characteristics of the game metrics
game_metrics.hideturtle()       # Hides Turtle as the turtle itself is not required, simply its 'results'
game_metrics.speed(object_speed)
game_metrics_location = (150, 260)
#game_metrics.shape("square")
game_metrics.color("white")
game_metrics.penup()    # This prevents the game metrics from drawing anything as it moves, ie. leaving no trace
game_metrics.goto(game_metrics_location)
game_lost_message = "Game Over, You Lost"
game_won_message = "Congrats! You Won!"
starting_game_metric = "⭐ Score : 0   ❤️ Lives : 0"
variable_game_metric = "⭐ Score : {}   ❤️ Lives : {}"
game_metric_fontname = "Arial"
game_metric_fonttype= "bold"
game_metric_fontalignment = "center"
game_metric_fontsize = "22"
game_metrics.write(starting_game_metric, align=game_metric_fontalignment, font=(game_metric_fontname,game_metric_fontsize, game_metric_fonttype))  # The format of game metrics
start_lives = 0
start_score = 0




## Keyboard Functions (to Move mamba)
#### the != statments are used to provide self impact due to the mabma head reversing
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


def go_and_avoid_mamba_head_impact():
    ## this function cause the mamba head to manoeuvre and prevent impact..
    ## with itself by ensuring the mamba head moves before an extension is
    ## put in its position
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


mamba_extenstions = []    #Empty list which will store the mamba extensions & grow in size upon impact
                        #Outside Function as putting inside cause 'undefined' error

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
        # Updating Game Metrics
        remaining_lives = remaining_lives + 1
        game_metrics.clear()    #removes the previous metrics on screen
        game_metrics.write(variable_game_metric.format(players_score, remaining_lives), align=game_metric_fontalignment,
                           font=(game_metric_fontname, game_metric_fontsize, game_metric_fonttype)) #updates with new game metrics

        ### Setting Up New Mamba Extension
        new_mamba_extenstion = turtle.Turtle()    # Creates a new Turtle object for mamba extensions
        new_mamba_extenstion.penup()              #Prevents the mamba extensions from leaving lines/trails in the screen
        new_mamba_extenstion.shape("square")
        new_mamba_extenstion.speed(object_speed)
        mamba_extenstions.append(new_mamba_extenstion)      #Adds new mamba extension to list


        # Adding extensions to mamba by...
        # Going through each mamba extension in list and..
        # making the new mamba extension  assume the last position of the mamba ..
        # starting from the last mamba extension (As starting with first causes 'out of range error')
    for each_mamba_extenstion in range(len(mamba_extenstions) - 1, 0, -1):
        mamba_extenstion_x = mamba_extenstions[each_mamba_extenstion - 1].xcor()
        mamba_extenstion_y = mamba_extenstions[each_mamba_extenstion - 1].ycor()
        mamba_extenstions[each_mamba_extenstion].goto(mamba_extenstion_x, mamba_extenstion_y)

    ### Starts the process once a new mamba extension has been created
    if len(mamba_extenstions) > 0: #detetmines whether a mamba extension has been created
        initial_mamba_extenstion_x = mamba_head.xcor()
        initial_gorwth_amount_y = mamba_head.ycor()
        mamba_extenstions[0].goto(initial_mamba_extenstion_x, initial_gorwth_amount_y)

    go_and_avoid_mamba_head_impact()   #calls function to ensure the mamba moves & does not collide with new extensions


    ## Lucky Block Impact Check
    if impact_zone > mamba_head.distance(lucky_block):
        lucky_block.hideturtle()
        players_score = players_score + 25
        # Division by two as it calculates position from the center of the screen
        hidden_randomx = random.randint(-(game_screen_size / 2), (game_screen_size / 2))
        hideen_randomy = random.randint(-(game_screen_size / 2), (game_screen_size / 2))
        lucky_block.goto(hidden_randomx, hideen_randomy)    #Prevents Double Scores caused by the mamba collecting
                                                            # lucky block more than once
        lucky_blocks_collected = lucky_blocks_collected + 1
        game_metrics.clear()    #removes the previous metrics on screen
        game_metrics.write(variable_game_metric.format(players_score, remaining_lives), align=game_metric_fontalignment,
                           font=(game_metric_fontname, game_metric_fontsize, game_metric_fonttype)) #Updates with new game metrics

    if lucky_blocks_collected == 5:
        game_metrics.clear()    #removes the previous metrics on screen
        game_metrics.write(game_won_message, align=game_metric_fontalignment, font=(game_metric_fontname,game_metric_fontsize, game_metric_fonttype)) #Updates with
                                                                                                    # new game metrics
        os.system("afplay " + winning_music_path)   #plays a sound effect & pauses the game
        time.sleep(to_display_message)      #allows player to read on screen message
        break # Ends the game_play loop and in turn ends the game


    ### Lucky Block 'Makeshift' Timer
    timer.append(1) #Increases List By 1 Entry Each Loop
    tally = 0   #Creates A Taly
    for timepassing in timer:
        tally = tally + 1   #tally increments based on many entires
    time_elapsed = (int(tally)) #this convers tally into an int

    # This will hide the turtle after 40 entries have been appended (approx takes 5 secs)
    if time_elapsed in hide_lucky_block_at: #We don't use direct as the list contains the amount
        lucky_block.hideturtle()


    ## This will show the turtle after 80 entries have been appended (approx takes 5 secs)
    if time_elapsed in show_lucky_block_at:
        # Division by two as it calculates position from the center of the screen
        newx = random.randint(-(game_screen_size/2), (game_screen_size/2))
        newy = random.randint(-(game_screen_size/2), (game_screen_size/2))
        lucky_block.goto(newx, newy)    #places lucky block in new random position before being shown again
        lucky_block.showturtle()
        timer.clear() #this clears the list, so that the loop can work indefinitely without..
                        # having to define new values for 'hide_lucky_block_at' and 'show_lucky_block_at'


    ### Border Impact Check
    ## this if statment outlines the borders of the game screen & determines if mamba head is outside screen...
    # ...Division by two as it calculates position from the center of the screen
    if mamba_head.xcor() > (game_screen_size/2) or mamba_head.xcor() < -(game_screen_size/2) or mamba_head.ycor() > (game_screen_size/2) or mamba_head.ycor() < -(game_screen_size/2):

        if remaining_lives == start_lives:
            game_lost = 5  # this will iniate another loop to show a 'game lost' message

        os.system("afplay " + player_life_lost_path)    #plays sound effect to indicate a loss of life
        mamba_head.goto(mamba_start_postiion) #re-centers the mamba head to start position
        mamba_head.direction = pause_until_input


        # Hide mamba Extenstions
        for mamba_extenstion in mamba_extenstions:  #this is going through each mamba extension in mamba extensions list
            # this will move the old mamba extentions to outside the screen & python turtle
            # has no inbuilt way of clearing these mamba extensions from memory
            mamba_extenstion.goto(outside_game_screen, outside_game_screen)

        mamba_extenstions.clear() #this empties the growth amounts list

        # Removes Lives If Present
        if remaining_lives > start_lives:
            remaining_lives = remaining_lives -1



        else:
            # Reset the players score
            players_score = start_score
            remaining_lives = start_lives
            #mamba_extenstions.clear()


        game_metrics.clear()
        game_metrics.write(variable_game_metric.format(players_score, remaining_lives), align=game_metric_fontalignment,
                           font=(game_metric_fontname, game_metric_fontsize, game_metric_fonttype))     #updates with new game metric information


    ## Checks for Body Impact
    for mamba_extenstion in mamba_extenstions:
        if mamba_extenstion.distance(mamba_head) < impact_zone:
            game_lost = 5 #this will iniate another loop to show a 'game lost' message
            #break   # bresks the loop and in turn end the game


        game_metrics.clear()
        ## Updates game with more recent metrics
        game_metrics.write(variable_game_metric.format(players_score, remaining_lives), align=game_metric_fontalignment, font=(game_metric_fontname,game_metric_fontsize, game_metric_fonttype))



    if game_lost == 5: #could have used boolean, but prior test show error causing incrorrect running of loop
        game_metrics.clear()
        game_metrics.write(game_lost_message, align=game_metric_fontalignment, font=(game_metric_fontname,game_metric_fontsize, game_metric_fonttype))
        os.system("afplay " + lose_music_path) #plays lost game sound effect
        time.sleep(to_display_message)
        break  # breaks the loop and in turn end the game

    time.sleep(wait_before_reloop)  #make the loop wait before re-looping so that all prior loops can be completed.
    
    ### @Denzel Eshun
    ### @Fudailahad Khan
