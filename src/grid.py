from objects import Wire, Computer, Router, House
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRAY = (128, 128, 128)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Grid:
    def __init__(self, width, height, square_size):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.board = [[None for x in range(width)] for y in range(height)]
        self.colors = {
            "background": BLACK,
            "grid_lines": GRAY,
        }
        print(self.board)

    def add_wire(self, x, y):
        self.board[y][x] = Wire(x, y)

    def add_router(self, x, y):
        self.board[y][x] = Router(x, y)

    def add_computer(self, x, y, connected = False):
        self.board[y][x] = Computer(x, y, connected)

    def add_house(self, x, y, connected = False, conn_direction = 'N'):
        self.board[y][x] = House(x, y, connected, conn_direction)

    def draw(self, screen):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size)

                pygame.draw.rect(screen, GRAY, rect, 1)
                
                if cell is not None:
                    cell.draw(screen, self.square_size)
                    # print ("cell: {}".format(cell))