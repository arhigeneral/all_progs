import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
FPS = 60
y = 0
x = -20
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()

while 1:
    sc.fill(WHITE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    if y > 0:
        y -= 1
        pygame.draw.circle(sc, BLUE, (x,y), 5)
        pygame.display.update()


    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    if y == 0 :
        pygame.draw.rect(sc, RED, (x-5, 0, 10, 10))
        pygame.display.update()

    if pressed[0] and y==0:
        y = pos[1]
        x = pos[0]
        pygame.draw.circle(sc, BLUE, (pos), 5)
        pygame.display.update()



    clock.tick(FPS)
