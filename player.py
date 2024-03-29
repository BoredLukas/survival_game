import pygame
import os
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, img_path, xy_center, player_size, settings):
        super().__init__() # call __init__ of parent class (i.e. of pygame.sprite.Sprite)
 
        # ASSIGN CLASS ATTRIBUTES
        if not os.path.exists(img_path):
            raise Exception("THE FOLLOWING FILE DOES NOT EXIST: {0}".format(img_path))
        self.settings = settings
        self.image = pygame.transform.scale(pygame.image.load(str(img_path)),player_size) # load image
        self.rect = self.image.get_rect() # create rectangle containing ball image
        self.rect.center = xy_center # set center coords of player
        self.mask = pygame.mask.from_surface(self.image) # creates a mask, used for collision detection (see manual about pygame.sprite.collide_mask())
        self.original_image = self.image
        # self.relative_x = # Relative coordinates on the display instead of map
        # self.relative_y = # Relative coordinates on the display instead of map
        self.previous_movement = None

    def update(self):
        self.old_pos = self.rect.copy()

    def point_at(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.image = self.original_image
        angle = ( math.atan2(self.rect.centery - mouse_y,self.rect.centerx - mouse_x) / math.pi * -180 ) + 90 
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def collide(self):

        # Collision with mapborders
        if self.rect.centerx >= self.settings.MAP_WIDTH:
            self.rect.centerx = self.rect.centerx - 10
            self.settings.SPEED = 0
        if self.rect.centerx <= 0:
            self.rect.centerx = self.rect.centerx + 10
            self.settings.SPEED = 0
        if self.rect.centery >= self.settings.MAP_HEIGHT:
            self.rect.centery = self.rect.centery - 10
            self.settings.SPEED = 0
        if self.rect.centery <= 0:
            self.rect.centery = self.rect.centery + 10
            self.settings.SPEED = 0
        else:
            self.settings.SPEED = self.settings.ORIGINAL_SPEED

    def mouseposition(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(mouse_x, mouse_y)