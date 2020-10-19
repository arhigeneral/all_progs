import pygame

FPS = 60
W = 500  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
STOP = "0"

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

motion = STOP

while 1:
    sc.fill(WHITE)

    circle = pygame.draw.circle(sc, BLUE, (x, y), r)
    circle
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3
    elif x > W // 2:
        x -= 3
    elif x < W // 2:
        x += 3
    elif y > H // 2:
        y -= 3
    elif y < H // 2:
        y += 3





    clock.tick(FPS)
