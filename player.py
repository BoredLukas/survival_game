import pygame
import os
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, img_path, xy_center, player_size):
        super().__init__() # call __init__ of parent class (i.e. of pygame.sprite.Sprite)
 
        # ASSIGN CLASS ATTRIBUTES
        if not os.path.exists(img_path):
            raise Exception("THE FOLLOWING FILE DOES NOT EXIST: {0}".format(img_path))
        self.image = pygame.transform.scale(pygame.image.load(str(img_path)),player_size) # load image
        self.rect = self.image.get_rect() # create rectangle containing ball image
        self.rect.center = xy_center # set center coords of player
        self.mask = pygame.mask.from_surface(self.image) # creates a mask, used for collision detection (see manual about pygame.sprite.collide_mask())
 
    def update(self):
        """
        - update function gets executed in every step
        - determines motion of player
        """
        pass

    def point_at(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(self.rect.centery - mouse_y, self.rect.centerx - mouse_x)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def collide(self,ball):
        """
        player collides with ball, given as argument
        this method updates velocities of BOTH player and ball
        """
        pass

    def mouseposition(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(mouse_x, mouse_y)