import pygame

pygame.init()

sc = pygame.display.set_mode((300,300))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# GRAY = (125, 125, 125)
# LIGHT_BLUE = (64, 128, 255)
# GREEN = (0, 200, 64)
# YELLOW = (225, 225, 0)
# PINK = (230, 50, 230)
#
# r1 = pygame.Rect((150, 20, 100, 75))
#
# pygame.draw.rect(sc, WHITE, (20, 20, 100, 75))
# pygame.draw.rect(sc, LIGHT_BLUE, r1, 8)
x = 0
y = 0

while True:
    sc.fill(BLACK)
    pygame.time.delay(10)
    events = pygame.event.get()
    pygame.draw.circle(sc,WHITE,(x,y),1)
    x += 1
    y += 1
    if x == 300:
        x = 0
        y = 0
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
