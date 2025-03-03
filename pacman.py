!pip install pygame
import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Pac-Man settings
pacman_radius = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Ghost settings
ghost_radius = 20
ghosts = [{'x': random.randint(0, screen_width), 'y': random.randint(0, screen_height)} for _ in range(4)]
ghost_speed = 3

# Food settings
food_radius = 8
foods = [{'x': random.randint(0, screen_width), 'y': random.randint(0, screen_height)} for _ in range(5)]

# Font for score
font = pygame.font.SysFont("arial", 24)

# Game loop
clock = pygame.time.Clock()
running = True
score = 0

# Helper functions
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), pacman_radius)

def draw_ghosts(ghosts):
    for ghost in ghosts:
        pygame.draw.circle(screen, RED, (ghost['x'], ghost['y']), ghost_radius)

def draw_food(foods):
    for food in foods:
        pygame.draw.circle(screen, BLUE, (food['x'], food['y']), food_radius)

def check_collision(x, y, items, radius):
    for item in items:
        distance = ((x - item['x']) ** 2 + (y - item['y']) ** 2) ** 0.5
        if distance < radius:
            items.remove(item)
            return True
    return False

# Main game loop
while running:
    screen.fill(BLACK)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move Pac-Man
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Keep Pac-Man within the screen bounds
    pacman_x = max(pacman_radius, min(screen_width - pacman_radius, pacman_x))
    pacman_y = max(pacman_radius, min(screen_height - pacman_radius, pacman_y))

    # Check for food collision
    if check_collision(pacman_x, pacman_y, foods, food_radius):
        score += 1

    # Move ghosts randomly
    for ghost in ghosts:
        ghost['x'] += random.choice([-1, 1]) * ghost_speed
        ghost['y'] += random.choice([-1, 1]) * ghost_speed

        # Keep ghosts within screen bounds
        ghost['x'] = max(ghost_radius, min(screen_width - ghost_radius, ghost['x']))
        ghost['y'] = max(ghost_radius, min(screen_height - ghost_radius, ghost['y']))

        # Check if Pac-Man collides with a ghost
        if ((pacman_x - ghost['x']) ** 2 + (pacman_y - ghost['y']) ** 2) ** 0.5 < pacman_radius + ghost_radius:
            running = False
            print("Game Over! Final Score:", score)

    # Draw objects
    draw_pacman(pacman_x, pacman_y)
    draw_ghosts(ghosts)
    draw_food(foods)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
