import pygame
import cv2
import numpy as np
from enum import Enum

refresh_rate = 17  # => 60Hz


class Color(Enum):
    Red = (255, 0, 0)
    Green = (0, 255, 0)  # Darker Green
    Blue = (0, 0, 255)
    Yellow = (0, 255, 255)
    Black = (0, 0, 0)
    Gray1 = (175, 175, 175)


class ColorTypes(Enum):
    Wall = Color.Black.value
    Landmark = Color.Green.value


class Graphic:
    def __init__(self, width, height, screen_name):
        self.text_width = round(width/2)
        self.width = width + self.text_width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(screen_name)

    def draw_object(self, object_color, object_rect):
        pygame.draw.rect(self.screen,  object_color, object_rect.get_rect())

    def draw_area(self, color, rect, alpha):
        s = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        color = (color[0], color[1], color[2], alpha)
        s.fill(color)
        self.screen.blit(s, (rect[0], rect[1]))

    def get_background(self):
        self.screen.fill(Color.Black.value)

    def update_screen(self):
        pygame.display.update()
        pygame.time.delay(refresh_rate)  # ~60 Hz

    def blit_text(self, text, rect):
        self.screen.blit(text, rect)

    def draw_circle(self, color, position, radius, width):
        pygame.draw.circle(self.screen, color, position, radius, width)
