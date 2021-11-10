import pygame, sys
from pygame.color import THECOLORS
from math import sqrt

pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ship = pygame.image.load('img/ship.png')
ship = pygame.transform.rotate(ship, 90)

"""Координаты корабля"""
shipX = 600
shipY = 400

font = pygame.font.SysFont('comicsansms', 40)
clock = pygame.time.Clock()
numFrame = 0
mouse_position = (0, 0)

"""Выстрелы на экране"""
fires = []


class Fire:
    """координаты выстрела"""
    x: int
    y: int
    """направление выстрела"""
    dx: int
    dy: int

    def __init__(self, x, y, dx, dy):
        """
        Конструктор выстрела
        """
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        """
        Сдвиг выстрела по направлению
        """
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def out(self):
        """
        Проверка, вышел ли выстрел за пределы поля
        """
        return self.x < 0 or self.y < 0 or self.x > WIDTH or self.y > HEIGHT


def draw():
    """
    Основная функция отрисовки
    """
    global numFrame
    screen.fill(THECOLORS['white'])
    rect = pygame.Rect((shipX - 100, shipY), (200, 70))
    pygame.draw.rect(screen, THECOLORS['green'], rect, 0)
    screen.blit(ship, (shipX - 60, shipY - 50))

    text = font.render(str(numFrame), True, THECOLORS['black'])
    numFrame += 1
    screen.blit(text, (0, 750))

    text = font.render(str(mouse_position), True, THECOLORS['black'])
    screen.blit(text, (1000, 750))

    text = font.render(str(len(fires)), True, THECOLORS['black'])
    screen.blit(text, (1000, 50))

    for fire in fires:
        fire.move()
        pygame.draw.circle(screen, THECOLORS['orange'], (fire.x, fire.y), 10)
        if fire.out():
            fires.remove(fire)

    pygame.display.flip()
    clock.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                shipY -= 10
            elif event.key == pygame.K_DOWN:
                shipY += 10
            elif event.key == pygame.K_LEFT:
                shipX -= 10
            elif event.key == pygame.K_RIGHT:
                shipX += 10

        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            dx = pos[0] - shipX
            dy = pos[1] - shipY
            lenXY = sqrt(dx * dx + dy * dy)
            dx = dx * 3 // lenXY
            dy = dy * 3 // lenXY
            fires.append(Fire(shipX, shipY, dx, dy))

    draw()
