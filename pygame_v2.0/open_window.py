import pygame

pygame.init()

pygame.display.set_mode((600,400))
caption = ('a','b','c','d','e','f','g')
i = 0
clock = pygame.time.Clock()
FPS = 60

while True:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.set_caption(caption[i])
    i += 1
    if i == 7:
        i = 0
    pygame.display.update()
