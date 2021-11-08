import pygame, sys

from pygame.constants import KEYUP
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1200, 800))

color = (255, 100, 40)
ship = pygame.image.load('img/ship.png')
ship = pygame.transform.rotate(ship, 90)
height = 200
width = 200
#rgb

clock = pygame.time.Clock()
numFrame = 0

#print(pygame.font.get_fonts())

def drawA():
    global numFrame, ship, clock, height, width, screen
    rect = pygame.Rect(50, 50, width, height)
    screen.fill(THECOLORS['white'])
    pygame.draw.rect(screen, color, rect, 0)
    
    screen.blit(ship, (width//2, height-40))

    font = pygame.font.SysFont('arial', 40)
    text = font.render(str(numFrame), True, THECOLORS['black'])
    screen.blit(text, (50, 750))
	
    numFrame += 1
    pygame.display.flip()

    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                height = height - 10
            elif event.key == pygame.K_DOWN:
                height = height + 10
            elif event.key == pygame.K_LEFT:
                width = width + 10
            elif event.key == pygame.K_RIGHT:
                width = width + 10

        if event.type == pygame.MOUSEMOTION:
            print()

    drawA()

