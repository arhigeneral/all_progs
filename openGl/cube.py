import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = [
    (1, 1, 1),#5-0
    (1, 1, -1),#1-1
    (1, -1, 1),#4-2
    (1, -1, -1),#0-3
    (-1, 1, 1),#7-4
    (-1, 1, -1),#2-5
    (-0.5, -1, 1),#6-6
    (-1, -1, -1)#3-7
    #(1, -1, -1), 0
    #(1, 1, -1), 1
    #(-1, 1, -1), 2
    #(-1, -1, -1), 3
    #(1, -1, 1), 4
    #(1, 1, 1), 5
    #(-1, -1, 1), 6
    #(-1, 1, 1) 7
    ]

edges = (
    (3,1),
    (3,7),
    (3,2),
    (5,1),
    (5,7),
    (5,4),
    (0,1),
    (0,2),
    (0,4),
    (6,7),
    (6,2),
    (6,4)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)           #вращение куба
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()                          #отрисовка куба
        pygame.display.flip()
        pygame.time.wait(10)            #таймер вращения


main()
