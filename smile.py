import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw moduless")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
x = 200
y = 200

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)


    pygame.draw.circle(screen, YELLOW, [x, y], pi * 33,)
    pygame.draw.circle(screen, BLACK, [x, y], pi * 33, 1) #obvodka
    pygame.draw.circle(screen, RED, [x + 40, y - 30], pi * 6,)
    pygame.draw.circle(screen, BLACK, [x + 40, y - 30], pi * 6, 1) #obvodka
    pygame.draw.circle(screen, RED, [x - 40, y - 30], pi * 6)
    pygame.draw.circle(screen, BLACK, [x - 40, y - 30], pi * 6, 2) #obvodka
    pygame.draw.circle(screen, BLACK, [x + 40, y - 30], pi * 3)
    pygame.draw.circle(screen, BLACK, [x - 40, y - 30], pi * 3)
    pygame.draw.rect(screen, BLACK, [150, 250, 100, 20], 10, 1 )
    pygame.draw.line(screen, BLACK, [x - 10, y - 40], [x - 100 , y - 80], 11)
    pygame.draw.line(screen, BLACK, [x + 20, y - 40], [x + 100, y - 70], 11)

    pygame.draw.circle(screen, BLACK, [x, y], pi * 1, 10)


    pygame.display.flip()

#Proverka gita

pygame.quit()