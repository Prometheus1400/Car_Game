import pygame
WHITE = (255, 255, 255)

# initializing
pygame.init()
gameDisplay = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption('Car game or smth')


class Car:
    def __init__(self):
        self.x, self.xVel = 200, 0
        self.y, self.yVel = 200, 0
        self.length = 100
        self.width = 50

    def draw(self):
        pygame.draw.ellipse(gameDisplay, WHITE,
                            [self.x, self.y, self. width, self.length])

    def update(self):
        if ():
            pass


car = Car()


crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    gameDisplay.fill((57, 57, 57))
    car.draw()
