import pygame
from pygame.locals import *
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time


def figure():
    print("Введите количество углов")
    i=int(input())
    verticies = []
    for vertex in range(0,i):
        verticies.append(((random.randrange(-16, 16, 1)/2) ,  (random.randrange(-12, 12, 1))/2))
    z=0
    print("Наши точки - ", verticies)
    edges = []
    verticies.sort()
    print("Наши точки после сортировки!",verticies)
    for edge in range (0,i+1):
        if (edge < i- 1):
            print("Этот edge_1 - ", edge)
            edges.append((edge,edge + 1))
        elif (edge == i):
            print("Этот edge_242425235325235 - ", edge)
            edges.append((i - 1 , 0))
        z+=1
    print("Количество линий - ", z)
    print("Вот они наши соединения - ", edges)
    points =    (
        (-100,0),
        (100,0),
        (0,-100),
        (0,100)
    )
    gates = (
        (0,1),
        (2,3)
    )
    glBegin(GL_LINES)
    for gate in gates:
        for point in gate:
            glVertex2fv(points[point])



    for edge in edges:
        for vertex in edge:
            glVertex2fv(verticies[vertex])
    glEnd()





def main():
    pygame.init()
    display = (600,400)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0, 0, 0, 1.0)
    glutInitWindowPosition(50, 50)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -50)

    # Определяем положение источника света

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 0.0, 0.0, 3)           #вращение куба
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        figure()
        pygame.display.update()
        clock.tick(60)     #таймер вращения
        time.sleep(3)
        print("Продолжать рисовать эти дурацкие n-угольники?(press y/n)")
        end=input()
        if (end == "n"):
            pygame.quit()
            quit()


main()
