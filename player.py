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
        self._draw_triangle()  # Draw initial triangle

    def _get_triangle_points(self):
        # Calculate points relative to center of surface
        center = pygame.Vector2(self.radius, self.radius)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    def _draw_triangle(self):
        self.image.fill((0,0,0,0))  # Clear with transparency
        points = self._get_triangle_points()
        pygame.draw.polygon(self.image, "white", points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self._draw_triangle()  # Redraw triangle after rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position

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