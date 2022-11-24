import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        super(Platform, self).__init__()
        self.screen = pygame.display.get_surface()

        self.color = color
        self.rect = pygame.rect.Rect(pos, (width, height))
        self.mask = pygame.mask.Mask((width, height), False)

        self.velocity = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)