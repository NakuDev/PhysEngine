import pygame


def circleSurface(color, radius):
    shape_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    return shape_surf


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color):
        super(Ball, self).__init__()
        self.screen = pygame.display.get_surface()
        self.unit = self.screen.get_height() / 1000

        self.radius = radius  # m
        self.color = color
        self.center = pos
        self.image = circleSurface(self.color, self.radius)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.center[0] - self.radius, self.center[1] - self.radius))

        self.mass = 1  # kg
        self.acceleration = 9.81  # m.s^-1
        self.velocity = 0  # m.s^-1

        self.weight = pygame.math.Vector2(-1, 0)
        self.weight.scale_to_length(self.mass * self.acceleration)
        self.forces_list = [self.weight]

        self.holded = False
        self.holded_point = ()

    def update(self):
        if not self.holded:
            self.velocity += self.acceleration / 60
            self.rect.y += self.velocity

        self.isHolded()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def isHolded(self):
        if pygame.mouse.get_pressed()[0]:
            vector = pygame.math.Vector2()
            vector.x = pygame.mouse.get_pos()[0] - self.rect.centerx
            vector.y = pygame.mouse.get_pos()[1] - self.rect.centery
            if vector.magnitude() <= self.radius and not self.holded:
                self.holded = True
                self.holded_point = (pygame.mouse.get_pos()[0] - self.rect.centerx, pygame.mouse.get_pos()[1] - self.rect.centery)
            elif self.holded:
                self.rect.center = (pygame.mouse.get_pos()[0] - self.holded_point[0], pygame.mouse.get_pos()[1] - self.holded_point[1])
        else:
            self.holded = False