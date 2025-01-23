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
        self._update_image()  # Draw initial triangle

    def _get_triangle_points(self):
        # Calculate points relative to actual position
        center = self.position
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]

    def _update_image(self):
        # Clear the surface
        self.image.fill((0, 0, 0, 0))
        # Convert points to be relative to surface
        relative_points = [point - self.position + pygame.Vector2(self.radius, self.radius) for point in self._get_triangle_points()]
        # Draw to self.image
        pygame.draw.polygon(self.image, "white", relative_points, 2)

    def draw(self, screen):
        # Update rectangle position to match actual position
        self.rect.center = self.position
        screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        self._update_image()