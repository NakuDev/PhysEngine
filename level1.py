import pygame
from ball import Ball
from platform import Platform

class Level1:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.unit = self.screen.get_height()/1000
        self.running = True

        self.ball = Ball((200, 200), 50, (255, 0, 0))
        self.platform = Platform((0, 600), self.screen.get_width(), 10, (255, 255, 255))

    def update(self):
        self.ball.update()
        self.check_collides(self.ball, self.platform)

    def display(self):
        self.ball.draw()
        self.platform.draw()

    def check_collides(self, sprite1, sprite2):
        # Now calculate the offset between the rects.
        offset_x = sprite1.rect.x - sprite2.rect.x
        offset_y = sprite1.rect.y - sprite2.rect.y

        # And pass the offset to the `overlap` method of the mask.
        overlap = sprite2.mask.overlap(sprite1.mask, (offset_x, offset_y))
        if overlap:
            print('The two masks overlap!', overlap)

    '''def collide_mask(self, sprite1, sprite2):
        if pygame.sprite.collide_mask(sprite1, sprite2):
            print("test")
            sprite1.velocity = 0
            sprite2.velocity = 0'''