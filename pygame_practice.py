import pygame
import random

class Box():
    def __init__(self, display, x, y, width, height):
        # makes class boat that will create a boat object of desired color at desired coords
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.d = d
        #self.color = color
        self.display = display
        self.speed_x = 5
        self.speed_y = 1

    def draw_box(self):
        # draws box at x and y coords
        pygame.draw.rect(self.display, (255, 0, 0), (self.x, self.y, 50, 50), 0)

    def move_box(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_box(self):

        if self.x < 0 or self.x > self.width-50:
            self.speed_x *= -1
            #self.x += self.speed_x

        if self.y <= 0 or self.y >= self.height-50:
            self.speed_y *= -1
            #self.y += self.speed_y

    def box_x(self):
        return self.x

    def box_y(self):
        return self.y



pygame.init()

# setting constant variables
SEABLUE  = (25, 94, 172)
SKYBLUE = (136, 192, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SADDLE_BROWN = (139, 69, 19)
SPRING_GREEN = (0, 255, 127)
GREEN = (85, 107, 47)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 1000
HEIGHT = 800
FPS = 100

# creating screen and clock objects
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

box_list = []
for i in range(20):
    random_x = random.randint(0,WIDTH-50)
    random_y = random.randint(0, HEIGHT-50)
    box_list.append(Box(screen, random_x, random_y, WIDTH, HEIGHT))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    '''
    box1.draw_box()
    box1.move_box()
    box1.bounce_box()

    box2.draw_box()
    box2.move_box()
    box2.bounce_box()
    '''
    for box in box_list:
        box.draw_box()
        box.move_box()
        box.bounce_box()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
