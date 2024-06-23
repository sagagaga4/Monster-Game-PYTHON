import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Satan")

# Clock for managing updates
CLOCK = pygame.time.Clock()

# Load images (adjust paths as necessary)
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("Satan.png"), (400, 400))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("SatanJump.png"), (400, 400))
BACKGROUND = pygame.transform.scale(pygame.image.load("Background.png"), (1280, 720))

# Initial position and physics constants
player_pos = pygame.Vector2(400, 280)
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Key handling
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys_pressed[pygame.K_a]:
        player_pos.x -= 300 * dt
        
    if keys_pressed[pygame.K_SPACE] and not jumping:
        jumping = True
        Y_VELOCITY = JUMP_HEIGHT
    
    # Update position based on jumping state
    if jumping:
        player_pos.y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        
        if player_pos.y >= 280:  # On ground
            jumping = False
            player_pos.y = 280
            Y_VELOCITY = JUMP_HEIGHT
    
    # Clear screen and draw elements
    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        SCREEN.blit(JUMPING_SURFACE, (player_pos.x, player_pos.y))
    else:
        SCREEN.blit(STANDING_SURFACE, (player_pos.x, player_pos.y))
    
    # Update display and cap frame rate
    dt = CLOCK.tick(60) / 1000
    pygame.display.update()
    CLOCK.tick(60)
