import pygame
import os

class Ball(pygame.sprite.Sprite):
    """
    Class for balls, derive from pygame's sprite class
    -> makes your life easier since you can use e.g. the collision detection of the sprite class
    """
    def __init__(self, img_path, xy_center):
        super().__init__() # call __init__ of parent class (i.e. of pygame.sprite.Sprite)
 
        # ASSIGN CLASS ATTRIBUTES
        if not os.path.exists(img_path): # check if folder of image exists
            raise Exception("THE FOLLOWING FILE DOES NOT EXIST: {0}".format(img_path))
        self.image = pygame.image.load(str(img_path)) # load image
        self.rect = self.image.get_rect() # create rectangle containing ball image
        self.rect.center = xy_center # set center coords of ball
        self.mask = pygame.mask.from_surface(self.image) # creates a mask, used for collision detection (see manual about pygame.sprite.collide_mask())
 
    def update(self):
        """
        - update function gets executed in every step
        - determines motion of ball
        """
        pass
 
 
    def collide(self,ball):
        """
        ball self collides with other ball, given as argument
        this method updates velocities of BOTH balls
        """
        pass
