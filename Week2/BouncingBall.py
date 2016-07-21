"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)






pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE







# -------- Main Program Loop -----------
x= 350
y = 250
speed1 = random.randint(-10,10)
speed2 =random.randint(-10,10)
size = random.randint(20,80)
colors_list = [BLACK, WHITE, RED, BLUE, GREY]
index = 3
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here
    #pygame.draw.line(screen, GREY, [0,0], [350,250], 1)
    

    
    
    pygame.draw.circle(screen, colors_list[index] , [x,y], size, 0)
    x += speed1
    y+= speed2

    if (x>700):
        speed1 = -speed1
        index = random.randint(0, len(colors_list)-1)
        
    if (x<0):
        speed1=-speed1
        index = random.randint(0, len(colors_list)-1)
        
    if (y<0):
        speed2 = -speed2
        index = random.randint(0, len(colors_list)-1)
    if (y>500):
        speed2 = -speed2
        index = random.randint(0, len(colors_list)-1)
    



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

