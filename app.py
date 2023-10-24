import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

# Box properties
BOX_SPEED = 6
box_x = (SCREEN_WIDTH // 2)  # Start in the center
box_y = (SCREEN_HEIGHT // 2)

# Load the sounds
pygame.mixer.music.load('sound/propellerwav-14433.mp3')
pygame.mixer.music.play(-1)
sound_shoot = pygame.mixer.Sound('sound/machin-gun-ak47-sound-effect-6-11004.mp3')

# Load the sprites

# Plane
box_sprite = pygame.image.load('png/Plane/Fly (1).png')
box_sprite2 = pygame.image.load('png/Plane/Fly (2).png')

scale_factor = 0.5
new_width = int(box_sprite.get_width() * scale_factor)
new_height = int(box_sprite.get_height() * scale_factor)
box_sprite = pygame.transform.scale(box_sprite, (new_width, new_height))
box_sprite2 = pygame.transform.scale(box_sprite2, (new_width, new_height))

# Shoot sprites
shoot_sprites = []
for i in range(1, 6):
    sprite = pygame.image.load(f'png/Plane/Shoot ({i}).png')
    sprite = pygame.transform.scale(sprite, (new_width, new_height))  # Scale to match other sprites
    shoot_sprites.append(sprite)
    
# Bird fly sprites
bird_sprites = []
for i in range(1, 5):
    sprite = pygame.image.load(f'png/bird/bird{i}.png')
    flipped_sprite = pygame.transform.flip(sprite, True, False)
    bird_sprites.append(flipped_sprite)

# Clouds
cloud1 = pygame.image.load('png/cloud1.PNG')
cloud2 = pygame.image.load('png/cloud2.PNG')
cloud3 = pygame.image.load('png/cloud3.PNG')

# Set the current sprite
current_sprite = box_sprite

# Animation control
sprite_switch_timer = 0
sprite_switch_interval = 10
shoot_sprite_index = 0
shoot_sprite_timer = 0
shoot_sprite_interval = 5

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane")

# Frame rate control
FPS = 60
clock = pygame.time.Clock()

# Cloud setup
object_rect = pygame.Rect(1600, 250, 50, 50)
object_rect2 = pygame.Rect(1600, -200, 50, 50)
object_rect3 = pygame.Rect(2000, 200, 50, 50)
velocity = -200
velocity2 = -100
velocity3 = -50

# Birds set up
bird_rect = pygame.Rect(1600, 200, 50, 50)
velocitybird = -200
bird_sprite_index = 0
bird_sprite_timer = 0
bird_sprite_interval = 10

# Define rectangle for the plane
plane_rect = pygame.Rect(box_x, box_y, new_width, new_height)

# Game loop
running = True
shooting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Clock for cloud
    dt = clock.tick(60) / 1000.0
    
    # Move the objects
    object_rect.x += velocity * dt
    object_rect2.x += velocity2 * dt
    object_rect3.x += velocity2 * dt
    bird_rect.x += velocitybird * dt
    
    if object_rect.x < -800:
        object_rect.x = 1600
    
    if object_rect2.x < -800:
        object_rect2.x = 1600
    
    if object_rect3.x < -800:
        object_rect3.x = 2000
    
    bird_sprite_timer += 1
    if bird_sprite_timer > bird_sprite_interval:
        bird_sprite_timer = 0
        bird_sprite_index = (bird_sprite_index + 1) % len(bird_sprites)

    # Shooting logic
    if keys[pygame.K_SPACE]:
        shooting = True
        shoot_sprite_timer += 1
        if shoot_sprite_timer > shoot_sprite_interval:
            sound_shoot.play()
            shoot_sprite_timer = 0
            shoot_sprite_index = (shoot_sprite_index + 1) % len(shoot_sprites)
            current_sprite = shoot_sprites[shoot_sprite_index]
    else:
        shooting = False
        shoot_sprite_index = 0
        shoot_sprite_timer = 0
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

    # Update the plane's rectangle position
    plane_rect.topleft = (box_x, box_y)
    
    # Check for collision
    if plane_rect.colliderect(bird_rect):
        print("Collision detected!")
        # Add your collision handling code here
    
    # Draw
    screen.fill(SKY_BLUE)
    screen.blit(cloud1, object_rect.topleft)
    screen.blit(cloud2, object_rect2.topleft)
    screen.blit(bird_sprites[bird_sprite_index], bird_rect.topleft)
    screen.blit(current_sprite, (box_x, box_y))
    screen.blit(cloud3, object_rect3.topleft)
    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()