import pygame

FPS = 60
WIN_WIDTH = 255
WIN_HEIGHT = 255

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
j = 0
color = []
for colors in range (0,254):
    j += 1
    color.append((colors+j,colors+j,colors+j))

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH*2, WIN_HEIGHT*2))

# радиус и координаты круга
r = 10
x = 0 - r  # скрываем за левой границей
y = 0 - r # выравнивание по центру по вертикали
j = 0

while 1:
    sc.fill(WHITE)

    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

    pygame.draw.circle(sc, (j,j,j), (x, y), r)
    if j == 255:
        j = 0
    j += 1

    pygame.display.update()

    # если полностью скрылся за правой границей
    if x >= WIN_WIDTH*2 + r:
        x = 0 - r
        y = 0 - r
    else:  # во всех остальных случаях
        x += 2  # в следующем кадре круг сместится,
        y += 2
        # от значения зависит "скорость движения"

    clock.tick(FPS)
