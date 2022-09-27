from turtle import _Screen
import pygame
import os
from settings import Settings

class Camera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #box setup
        self.settings = Settings()
        self.camera_borders = {'left':200, 'right':200, 'top':100, 'bottom':100}
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        width = self.settings.WIN_WIDTH - self.camera_borders['left'] - self.camera_borders['right']
        height = self.settings.WIN_WIDTH - self.camera_borders['top'] - self.camera_borders['bottom']
        self.camera_rect = pygame.rect(left, top, width, height)
