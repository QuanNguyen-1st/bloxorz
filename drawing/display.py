import pygame
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Display:
    
    def __init__(self, title='', size=(800, 600), map_size = (10,6)):
        self.width, self.height = map_size
        self.title = title
        self.size = size
        self.delta = 0
        self.currentFrame = self.get_time()
        self.lastFrame = self.get_time()
        self.surface = pygame.display.set_mode(self.size, DOUBLEBUF | OPENGL)

        pygame.display.set_caption(self.title)

        glEnable(GL_POLYGON_SMOOTH)
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)

        gluPerspective(60, (size[0] / size[1]), 0.1, 80.0)
        gluLookAt(-3, -7, 7, 0, 0, 0, 0, 0, 1) 
        glTranslatef(-self.width / 2, self.height / 2, 0)

        glLineWidth(2)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)

    def update(self):
        self.delta = self.currentFrame - self.lastFrame
        pygame.display.flip()
        self.lastFrame = self.get_time()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glViewport(0, 0, self.surface.get_width(), self.surface.get_height())

    @staticmethod
    def get_time():
        return time.time() * 1000