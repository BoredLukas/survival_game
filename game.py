import os
import pygame
import sys
import random
from player import Player
from obstacles import Tree
from obstacles import Stone
from settings import Settings

class CameraGroup(pygame.sprite.Group):
    def __init__(self,width,height,settings):
        super().__init__()
        self.settings = settings
        #box setup
        self.width = width
        self.height = height

        # camera offset 
        self.offset = pygame.math.Vector2()
        self.half_w = self.width // 2
        self.half_h = self.height // 2

        # Setting up Camera Box
        self.camera_borders = {'left':100, 'right':100, 'top':50, 'bottom':100}
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        width = self.width - self.camera_borders['left'] - self.camera_borders['right']
        height = self.height - self.camera_borders['top'] - self.camera_borders['bottom']
        self.camera_rect = pygame.Rect(left, top, width, height)

        # Background
        self.ground_surf = pygame.image.load(os.path.join('data','background.png')).convert_alpha()
        self.ground_surf = pygame.transform.scale(self.ground_surf, self.settings.MAP_SIZE)
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))
    
		# zoom 
        self.zoom_scale = 1
        self.internal_surf_size = (2500,2500)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def getCAMERA_RECT(self):
        return self.camera_rect

    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def custom_draw(self,player,surface):
		
		# self.center_target_camera(player)
		# self.box_target_camera(player)
		# self.keyboard_control()
        self.box_target_camera(player)
        self.display_surface = surface
        self.internal_surf.fill('#71ddee')

		# ground 
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf,ground_offset)

		# active elements
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image,offset_pos)

        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

        self.display_surface.blit(scaled_surf,scaled_rect)

class Game:
    """
    Main GAME class
    """
    def __init__(self,settings):
        pygame.init()
        pygame.font.init()
        self.settings = settings
        self.time_delay = self.settings.TIME_DELAY
        size = (self.settings.WIN_WIDTH, self.settings.WIN_HEIGHT)
        self.screen = pygame.display.set_mode(size) # create screen which will display everything
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption(self.settings.NAME) # Game title

    def quit(self):
        pygame.quit()
        sys.exit(0)
 
    def play(self):
        # CREATE GAME OBJECTS
        # PLAYER:
        player = Player(os.path.join('data','player.png'),(self.settings.WIN_WIDTH / 2,self.settings.WIN_HEIGHT / 2),self.settings.PLAYER_SIZE, self.settings)
        
        # CAMERA GROUP
        camera_group = CameraGroup(self.settings.WIN_WIDTH,self.settings.WIN_HEIGHT, self.settings)
        camera_group.add(player)
        # OTHER OBJECTS:
        for i in range(10):
            x, y = random.randint(0,self.settings.MAP_WIDTH), random.randint(0,self.settings.MAP_HEIGHT)
            tree = Tree(os.path.join('data','tree_II.png'), self.settings.TREE_SIZE, x, y, self.settings, self.settings.TREE_MASK_SIZE)
            camera_group.add(tree)

        # for i in range(10):
        #     x, y = random.randint(0,self.settings.MAP_WIDTH), random.randint(0,self.settings.MAP_HEIGHT)
        #     stone = Stone(os.path.join('data','stone.png'), self.settings.STONE_SIZE, x, y) 
        #     camera_group.add(stone)

        # GAME PERMANENT LOOP
        while True:
            pygame.time.delay(self.settings.TIME_DELAY)
 
            # KEY EVENTS
            for event in pygame.event.get():
                # Exit app if click quit button
                if event.type == pygame.QUIT:
                    self.quit()
            # COLLISION DETECTION
            player.collide()

            for sprite in camera_group.sprites():
                if sprite != player:
                    # collision = pygame.sprite.spritecollide(player, sprite, False)
                    collision = pygame.sprite.collide_rect(player, sprite)
                    if collision:
                        print(collision)
                        if player.rect.top - sprite.rect.bottom <= 0 and player.rect.top - sprite.rect.bottom <= self.settings.SPEED:
                            player.rect.top += self.settings.SPEED
                        if player.rect.bottom - sprite.rect.top >= 0 and player.rect.bottom - sprite.rect.top <= self.settings.SPEED:
                            player.rect.bottom += self.settings.SPEED
                        if player.rect.right - sprite.rect.left <= 0 and player.rect.right - sprite.rect.left <= self.settings.SPEED:
                            player.rect.right -= self.settings.SPEED
                        if player.rect.left - sprite.rect.right >= 0 and player.rect.left - sprite.rect.right <= self.settings.SPEED:
                            player.rect.left += self.settings.SPEED

            # Naviation of player
            # restriction = player.collide(tree)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP or pygame.KSCAN_W]:
                player.rect.top -= self.settings.SPEED
            if keys[pygame.K_DOWN or pygame.K_s]:
                player.rect.top += self.settings.SPEED
            if keys[pygame.K_LEFT or pygame.K_a]:
                player.rect.left -= self.settings.SPEED
            if keys[pygame.K_RIGHT or pygame.K_d]:
                player.rect.left += self.settings.SPEED 

            

            # MOUSETRACKING
            player.point_at()
            
            # see manual for all types of collisions: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide
 
            # UPDATE ALL GAME OBJECTS
            # balls.update() # can update all members of a group with a single command
            # player.update()
 
            # DRAW

            camera_group.update()
            camera_group.custom_draw(player,self.screen)

            player.update()

            # UPDATE DISPLAY
            pygame.display.update()
        pygame.quit()