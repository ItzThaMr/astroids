import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
        size = PLAYER_RADIUS * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.draw(screen)  # Draw initial triangle

    def _get_triangle_points(self):
        # Calculate points relative to actual position
        center = self.position
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        print(f"Update called, dt: {dt}")  # Debug print

        if keys[pygame.K_w]:
            print("W pressed")  # Debug print
            self.move(dt)
        if keys[pygame.K_s]:
            print("S pressed")  # Debug print
            self.move(-dt)
        if keys[pygame.K_a]:
            print("A pressed")  # Debug print
            self.rotate(dt)
        if keys[pygame.K_d]:
            print("D pressed")  # Debug print
            self.rotate(-dt)

    def draw(self, screen):
        points = self._get_triangle_points()
        pygame.draw.polygon(screen, "white", points, 2)  # Added width=2 to match asteroid style