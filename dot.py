import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Dots")


class Dot:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(5, 20)
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        if self.x < 0 or self.x > WIDTH:
            self.angle = math.pi - self.angle
        if self.y < 0 or self.y > HEIGHT:
            self.angle = -self.angle

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


dots = [Dot() for _ in range(100)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for dot in dots:
        dot.move()
        dot.draw()

    pygame.display.flip()
pygame.quit()
