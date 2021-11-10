import pygame, sys
from pygame.color import THECOLORS
from math import sqrt

pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont('comicsansms', 40)
clock = pygame.time.Clock()
numFrame = 0
mouse_position = (0, 0)

"""Выстрелы на экране"""
fires = []


class Ship:
    """
    Класс для отображения корабля
    """

    def __init__(self, x, y, imgPath):
        """
        Конструктор корабля
        x, y - горизонтальная и вертикальная координата
        """
        self.x = x
        self.y = y
        self.img = pygame.image.load(imgPath)
        self.img = pygame.transform.rotate(self.img, 90)

    def drawOn(self, screen):
        rect = pygame.Rect((self.x - 100, self.y), (200, 70))
        pygame.draw.rect(screen, THECOLORS['green'], rect, 0)
        screen.blit(self.img, (self.x - 60, self.y - 50))


class Fire:
    """
    Класс для отображения выстрелов
    """

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

    def drawOn(self, screen):
        pygame.draw.circle(screen, THECOLORS['orange'], (self.x, self.y), 10)


ship = Ship(WIDTH // 2, HEIGHT // 2, 'img/ship.png')


def draw():
    """
    Основная функция отрисовки
    """
    screen.fill(THECOLORS['white'])
    ship.drawOn(screen)

    text = font.render(str(numFrame), True, THECOLORS['black'])
    screen.blit(text, (0, HEIGHT - text.get_height()))

    text = font.render(str(mouse_position), True, THECOLORS['black'])
    screen.blit(text, (WIDTH - text.get_width(), HEIGHT - text.get_height()))

    text = font.render(str(len(fires)), True, THECOLORS['black'])
    screen.blit(text, (WIDTH - text.get_width(), 0))

    for fire in fires:
        fire.move()
        fire.drawOn(screen)
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
                ship.y -= 10
            elif event.key == pygame.K_DOWN:
                ship.y += 10
            elif event.key == pygame.K_LEFT:
                ship.x -= 10
                if ship.x < 0:
                    ship.x = 0
            elif event.key == pygame.K_RIGHT:
                ship.x += 10

        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            dx = pos[0] - ship.x
            dy = pos[1] - ship.y
            lenXY = sqrt(dx * dx + dy * dy)
            dx = dx * 3 // lenXY
            dy = dy * 3 // lenXY
            fires.append(Fire(ship.x, ship.y, dx, dy))

    numFrame += 1
    draw()
