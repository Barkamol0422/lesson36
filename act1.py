import pygame
import random
pygame.init()
SPRITE_COLOR = pygame.USEREVENT + 1
BACKGROUND_COLOR = pygame.USEREVENT + 2
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
GREEN = pygame.Color("Green")
BLUE = pygame.Color("Blue")
bg_color = BLUE
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]
    def update(self):
        global bg_color
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            self.image.fill(random.choice([WHITE, YELLOW, GREEN, BLUE]))
            bg_color = random.choice([MAGENTA, ORANGE, RED])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 470)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
