# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



def draw():
    a=1

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(300, 300)

glutInitWindowPosition(50, 50)

glutInit(sys.argv)

glutCreateWindow(b"Pervaya laba!")

glutDisplayFunc(draw);

glutMainLoop()
