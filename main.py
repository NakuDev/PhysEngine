import pygame
from level1 import Level1

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Window:
    def __init__(self):
        self.screensize = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.screensize.current_w//2, self.screensize.current_h//2))
        self.running = True
        self.clock = pygame.time.Clock()

        self.level1 = Level1()

        self.stage = self.level1

    def handling_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.stage.update()

    def display(self):

        self.screen.fill(BLACK)

        self.stage.display()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


window = Window()
window.run()

pygame.quit()
