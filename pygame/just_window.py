import pygame

pygame.init()

pygame.display.set_mode((600, 400))
FPS = 60
clock = pygame.time.Clock()
caption = ('mamba','ksavie','pygame','kotika','mac','book','niga')
i = 0
while True:
    events = pygame.event.get()
    for event in events:
        pygame.display.set_caption(caption[i])
        i+=1
        if i == 6:
            i = 0
        if event.type == pygame.QUIT:
            exit()
        clock.tick(FPS)
