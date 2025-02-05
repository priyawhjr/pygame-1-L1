''' For Windows
1.Download Python from the Microsoft store
2.Install it
3.You can move to cmd and check the Python installation by typing  python --version
4.if it doesn't work try py3 --version or py --version
5.If Python works you can use pip --version
6.If python3 works use pip3 --version
7.In the future use pip/pip3 install library name to install ex: pip install pygame or pip3 install pygame

'''
# Lesson Plan 8-Bumblebee.docx


import pgzrun
import random
# from random import randint       
import time

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False   # to indicate game is not over yet. 

bee = Actor("bee")
bee.pos = (100,100)

flower = Actor("flower")
flower.pos = 200,200

msg = ' '
# to dispaly Actor & other objects in screen 
def draw():
    screen.blit("background", (0,0)) # (0,0) is the  top left corner of screen
    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over: # if game_over = True
            screen.fill("pink") #Time's Up! \nYour Final Score:
            global msg
            msg = "Time's Up! \nYour Final Score:"
            screen.draw.text( msg + str(score),midtop=(WIDTH/2,20), 
            fontsize=50, color="red")
            


def place_flower(): # to place  flower at random postion on screen
    flower.x = random.randint(70, (WIDTH-70)) # OR randint(70, (WIDTH-70)) can be use. but then do --'from random import randint' in beginning
    flower.y = random.randint(70, (HEIGHT-70))


def time_up(): # declaring this func., to end the game 
    global game_over 
    game_over = True

# this func to update score, chg bee position with the help of keyboard
def update(): 
    global score
    
    if keyboard.left:
        bee.x = bee.x - 2   # move the bee to left by 2 pixels
    if keyboard.right:
        bee.x = bee.x + 2   # move the bee to right by 2 pixels
    if keyboard.up:
        bee.y = bee.y - 2   # move the bee to up by 2 pixels
    if keyboard.down:
        bee.y = bee.y + 2   # move the bee to down by 2 pixels

    # if flower img box collides with bee img box
    flower_collected = bee.colliderect(flower) 

    if flower_collected: # if flower_collected == True
        score = score + 10
        place_flower() #call func to chg flower pos. randomly on screen.

# end the game after 60 seconds
clock.schedule(time_up, 20.0) #clock.schedule(func_name to be called, time in sec.)


pgzrun.go()

'''
For Mac users
Download from https://www.python.org/ recent version
It will download a zip file with Python packages
We need to extract it by double-clicking it 
Unzip and you will have an installation window opened
Install it, They might need an admin password to install Python sometimes, if the admin has blocked the installation of software to allow the install
You can move to terminal python --version
If it doesn't work try python3 --version
If Python works you can use pip --version
If python3 works use pip3 --version
In the future use pip/pip3 install library name to install ex: pip install pygame or pip3 install pygame
'''

