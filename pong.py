import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_VEL = 5

# Ball settings
BALL_RADIUS = 20  # Increase the ball radius to make it bigger
BALL_VEL_X, BALL_VEL_Y = 4, 4

# Define paddle and ball positions
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Initialize scores
left_score = 0
right_score = 0

# Set up font for displaying scores
font = pygame.font.Font(None, 74)

# Load background image
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Main game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_VEL
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_VEL
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_VEL
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_VEL

    # Move the ball
    ball.x += BALL_VEL_X
    ball.y += BALL_VEL_Y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_VEL_Y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_VEL_X *= -1

    # Ball goes out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball.y = HEIGHT // 2 - BALL_RADIUS
        BALL_VEL_X *= -1
    elif ball.right >= WIDTH:
        left_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball.y = HEIGHT // 2 - BALL_RADIUS
        BALL_VEL_X *= -1

    # Draw everything
    WINDOW.blit(background, (0, 0))
    pygame.draw.rect(WINDOW, RED, left_paddle)
    pygame.draw.rect(WINDOW, BLUE, right_paddle)
    pygame.draw.ellipse(WINDOW, GREEN, ball)

    # Render scores
    left_text = font.render(str(left_score), True, WHITE)
    WINDOW.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 20))
    right_text = font.render(str(right_score), True, WHITE)
    WINDOW.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
