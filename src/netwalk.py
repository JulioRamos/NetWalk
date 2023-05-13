import pygame
from grid import Grid

# Initialize Pygame
pygame.init()

# Some collors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRAY = (128, 128, 128)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set the size of the screen
GRID_WIDTH = 4 # Number of horizontal tiles or houses
GRID_HEIGHT = 4 # Number of vertical tiles or houses
SQUARE_SIZE = 200 # Size of an edge of a square (in pixels)
SCREEN_SIZE = (SQUARE_SIZE * GRID_WIDTH, SQUARE_SIZE * GRID_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the caption of the window
pygame.display.set_caption("NetWalk")

# Create the game grid
grid = Grid(GRID_WIDTH, GRID_HEIGHT, SQUARE_SIZE)


# Add some test objects to the grid
# grid.add_wire(1, 1)

grid.add_computer(GRID_WIDTH - 1, GRID_HEIGHT - 1, False)
grid.add_computer(GRID_WIDTH - 2, GRID_HEIGHT - 1, True)
# grid.add_house(0, 0, True)
# grid.add_house(1, 0, True)
# grid.add_house(0, 1, True)
# grid.add_house(1, 1, True)
# grid.add_house(2, 0, False)
# grid.add_house(2, 1, False)
grid.add_house(0, 0, False, 'N')
grid.add_house(1, 0, True, 'S')
grid.add_house(2, 0, True, 'E')
grid.add_house(3, 0, True, 'W')


# Draw the grid and objects
grid.draw(screen)

# Update the screen
pygame.display.flip()

# Wait for the user to close the window
done = False
count = 0
while not done:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is inside the window
            if 0 <= event.pos[0] <= SCREEN_SIZE[0] and 0 < event.pos[1] < SCREEN_SIZE[1]:
                done = True
                print ('Mouse click on position ({}, {})'.format(event.pos[0], event.pos[1]))
    if count == 999999 * 100: done = True

# Quit Pygame
pygame.quit()