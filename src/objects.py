import pygame
# from netwalk import SQUARE_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRAY = (128, 128, 128)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class Square:
    directions = {'0': [0, 'North', 'N', 'Norte'], '1': [1, 'South', 'S', 'Sul'], '2': [2, 'East', 'E', 'Leste', 'L'], '3': [3, 'West', 'W', 'Oeste', 'O']}
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("Object at ({},{})".format(self.x, self.y))
    
    def draw(self, screen, square_size, color):
        rect = pygame.Rect(self.x * square_size, self.y * square_size, square_size, square_size)
        pygame.draw.rect(screen, color, rect)

    def draw_dot(self, surface, dot_color, pos, radius):
        pygame.draw.circle(surface, dot_color, pos, radius)

class Wire():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, square_size):
        rect = pygame.Rect(self.x * square_size, self.y * square_size, square_size, square_size)
        pygame.draw.rect(screen, BLACK, rect)


class Router:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, square_size):
        rect = pygame.Rect(self.x * square_size, self.y * square_size, square_size, square_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)


class Computer(Square):
    def __init__(self, x, y, connected):
        self.x = x
        self.y = y
        self.connected = connected

    def __str__(self):
        connStatus = 'Not connected'
        if self.connected: connStatus = 'Connected'
        return ("{} computer at ({},{})".format(connStatus, self.x, self.y))
        # return ('Computer')

    # Will draw the computer a computer in the grid
    # For now, it's drawing a square with a circle inside
    def draw(self, screen, square_size):
        rect = pygame.Rect((self.x + 0.2) * square_size, (self.y + 0.2) * square_size, square_size * 0.6, square_size * 0.6)
        pygame.draw.rect(screen, BLUE, rect, width = 3)
        
        pos = ((self.x * square_size) + (square_size / 2), (self.y * square_size)  + (square_size / 2))
        self.draw_dot(screen, RED, pos, square_size * 0.2)
        if self.connected:
            self.draw_dot(screen, GREEN, pos, square_size * 0.2)


class House(Square):

    def __init__(self, x, y, connected, conn_direction):
        self.x = x
        self.y = y
        self.connected = connected
        self.conn_direction = conn_direction
        
    # def rotate(self):
    #     pass
    #     self.conn_direction = self.next_direction()

    def draw(self, screen, square_size):
        self.squaresize = square_size

        # Set the colors for the house and window
        HOUSE_COLOR = RED
        LIGHT_ON_COLOR = YELLOW 
        LIGHT_OFF_COLOR = BLACK

        # Set the dimensions of the house and window
        HOUSE_WIDTH = 0.8 * self.squaresize     # 40
        HOUSE_HEIGHT = 0.8 * self.squaresize    # 40
        WINDOW_WIDTH = 0.4 * self.squaresize    # 20
        WINDOW_HEIGHT = 0.4 * self.squaresize   # 20

        # Calculate the positions of the house and window
        HOUSE_X = (self.x * self.squaresize) + ((self.squaresize -  HOUSE_WIDTH) / 2)
        HOUSE_Y = (self.y * self.squaresize) + ((self.squaresize -  HOUSE_HEIGHT) / 2)
        WINDOW_X = (self.x * self.squaresize) + ((self.squaresize -  WINDOW_WIDTH) / 2)
        WINDOW_Y = (self.y * self.squaresize) + ((self.squaresize -  WINDOW_HEIGHT) / 2)

        # Calculate the positions of the post (from center to its direction)
        POST_WIDTH = 0.2 * self.squaresize
        POST_CENTRAL_X = (self.x * self.squaresize) + (self.squaresize / 2) - 1
        POST_CENTRAL_Y = (self.y * self.squaresize) + (self.squaresize / 2) - 1
        POST_FINAL_X = POST_CENTRAL_X
        POST_FINAL_Y = POST_CENTRAL_Y
        
        
        if self.conn_direction == 'N':
            # POST_CENTRAL_X = POST_CENTRAL_X - (POST_WIDTH / 2)
            POST_FINAL_Y -= (self.squaresize / 2)
        elif self.conn_direction == 'S':
            # POST_CENTRAL_X = POST_CENTRAL_X - (POST_WIDTH / 2)
            POST_FINAL_Y += (self.squaresize / 2)
        elif self.conn_direction == 'E':
            # POST_CENTRAL_Y = POST_CENTRAL_Y - (POST_WIDTH / 2)
            POST_FINAL_X += (self.squaresize / 2)
        elif self.conn_direction == 'W':
            # POST_CENTRAL_Y = POST_CENTRAL_Y - (POST_WIDTH / 2)
            POST_FINAL_X -= (self.squaresize / 2)

        # Draw the house
        pygame.draw.rect(screen, HOUSE_COLOR, (HOUSE_X, HOUSE_Y, HOUSE_WIDTH, HOUSE_HEIGHT))

        if self.connected:
            # Draw the window with light on
            pygame.draw.rect(screen, LIGHT_ON_COLOR, (WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.draw.line(screen, LIGHT_ON_COLOR, (POST_CENTRAL_X, POST_CENTRAL_Y), (POST_FINAL_X, POST_FINAL_Y), int(POST_WIDTH))
        else:
            pygame.draw.rect(screen, LIGHT_OFF_COLOR, (WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.draw.line(screen, LIGHT_OFF_COLOR, (POST_CENTRAL_X, POST_CENTRAL_Y), (POST_FINAL_X, POST_FINAL_Y), int(POST_WIDTH))

        print ("Window at ({}, {}) to ({}, {})".format(WINDOW_X, WINDOW_Y, WINDOW_X + WINDOW_WIDTH, WINDOW_Y + WINDOW_HEIGHT))
        print ("Line at ({}, {}) to ({}, {})".format(POST_CENTRAL_X, POST_CENTRAL_Y, POST_FINAL_X, POST_FINAL_Y))