import pygame
import sys

class Object:
    def __init__(self, height, width, isSolid, speed, nextObjectTimer):
        self.height = height
        self.width = width
        self.isSolid = isSolid
        self.speed = speed
        self.nextObjectTimer = nextObjectTimer

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

# Box properties
BOX_SPEED = 5
box_x = (SCREEN_WIDTH // 2)  # Start in the center
box_y = (SCREEN_HEIGHT // 2)

# Load the sprites
box_sprite = pygame.image.load('png\Plane\Fly (1).png')
box_sprite2 = pygame.image.load('png\Plane\Fly (2).png')

scale_factor = 0.5
new_width = int(box_sprite.get_width() * scale_factor)
new_height = int(box_sprite.get_height() * scale_factor)
box_sprite = pygame.transform.scale(box_sprite, (new_width, new_height))
box_sprite2 = pygame.transform.scale(box_sprite2, (new_width, new_height))

# Set the current sprite
current_sprite = box_sprite

# Animation control
sprite_switch_timer = 0
sprite_switch_interval = 10  # Adjust this value to control animation speed.

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Box with Sprite")

# Frame rate control
FPS = 60
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Animation logic sprites
    sprite_switch_timer += 1
    if sprite_switch_timer > sprite_switch_interval:
        sprite_switch_timer = 0
        if current_sprite == box_sprite:
            current_sprite = box_sprite2
        else:
            current_sprite = box_sprite

    # Move the box and keep it within the screen boundaries
    sprite_width = current_sprite.get_width()
    sprite_height = current_sprite.get_height()

    if keys[pygame.K_LEFT] and box_x > 0:
        box_x -= BOX_SPEED
    if keys[pygame.K_RIGHT] and box_x + sprite_width < SCREEN_WIDTH:
        box_x += BOX_SPEED
    if keys[pygame.K_UP] and box_y > 0:
        box_y -= BOX_SPEED
    if keys[pygame.K_DOWN] and box_y + sprite_height < SCREEN_HEIGHT:
        box_y += BOX_SPEED

    # Draw
    screen.fill(SKY_BLUE)
    screen.blit(current_sprite, (box_x, box_y))
    pygame.display.flip()

    clock.tick(FPS)

# Cleanup
pygame.quit()
sys.exit()