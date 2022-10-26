import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img_path, x, y):
        super().__init__()
        
        # ASSIGN CLASS ATTRIBUTES
        if not os.path.exists(img_path):
            raise Exception("THE FOLLOWING FILE DOES NOT EXIST: {0}".format(img_path))
        self.x = x
        self.y = y
        # self.mask = pygame.mask.from_surface(self.image) # creates a mask, used for collision detection (see manual about pygame.sprite.collide_mask())

class Tree(Obstacle):
    def __init__(self, img_path, tree_size, x, y, rect=(100, 100)):
        super().__init__(img_path, x, y)
        self.image = pygame.transform.scale(pygame.image.load(str(img_path)),tree_size) # load image
        self.rect = self.image.get_rect()
        self.mask = rect

class Stone(Obstacle):
    def __init__(self, img_path, stone_size, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(str(img_path)),stone_size) # load image
        self.rect = self.image.get_rect() # create rectangle containing ball image