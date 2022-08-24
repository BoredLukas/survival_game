import os
import pygame
import sys
from player import Player
from ball import Ball

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
        player = Player(os.path.join("data","battleship.png"),(150,550))
 
        # OTHER OBJECTS:
        """
        if you have multiple objects of the same class (e.g. enemies), use a SPRITE GROUP:
        """
        balls = pygame.sprite.Group()
        balls.add(Ball(os.path.join("data","ball_blue.png"),[100,200]))
        balls.add(Ball(os.path.join("data","ball_black.png"),[200,400]))
        balls.add(Ball(os.path.join("data","ball_green.png"),[300,600]))
 
        # GAME PERMANENT LOOP
        while True:
            pygame.time.delay(self.settings.TIME_DELAY)
 
            # KEY EVENTS
            for event in pygame.event.get():
                # Exit app if click quit button
                if event.type == pygame.QUIT:
                    self.quit()
 
            # Naviation of player
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.rect.top -= self.settings.SPEED
            if keys[pygame.K_DOWN]:
                player.rect.top += self.settings.SPEED
            # and so on ...
 
 
            # COLLISION DETECTION
            """
            see manual for all types of collisions: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide
            """
            for ball in balls: # use loop to iterate through sprite group easily
                pass
 
            # UPDATE ALL GAME OBJECTS
            balls.update() # can update all members of a group with a single command
            player.update()
 
            # DRAW
            self.screen.fill(self.settings.BG_COLOR)  # draw empty screen
            balls.draw(self.screen) # draw all group members
            self.screen.blit(player.image, player.rect) # draw single object

            # UPDATE DISPLAY
            pygame.display.update()
 
        pygame.quit()