from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


# Draw Cube
def draw():
    x_rot = 45
    y_rot = 45
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(x_rot, 1.0, 0.0, 0.0)
    glRotatef(y_rot, 0.0, 1.0, 0.0)
    glutWireCube(0.7)
    glFlush()


# Initialize
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Python Cube")
    glutDisplayFunc(draw)
    glutMainLoop()


# Run
if __name__ == '__main__':
    main()

