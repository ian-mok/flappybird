import asyncio
import pygame
from snake import Snake
from apple import Apple

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")

clock = pygame.time.Clock()

# Global score so show_score() can read it
score = 0


def game_over():
    font = pygame.font.SysFont('arial', 100)
    surface = font.render("YOU LOST :(", True, pygame.Color(255, 0, 0))
    rect = surface.get_rect()
    rect.midtop = (WIDTH // 2, HEIGHT // 3)
    screen.blit(surface, rect)
    pygame.display.flip()


async def show_score():
    # Use the global score variable
    font = pygame.font.SysFont('arial', 50)
    surface = font.render("score: " + str(score), True, pygame.Color(0, 0, 0))
    rect = surface.get_rect()
    rect.midtop = (100, 0)
    screen.blit(surface, rect)


 

    apple = Apple()
    snake = Snake()

    score = 0
    running = True

    while running:
        screen.fill((0, 255, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw snake
        for body in snake.body:
            pygame.draw.rect(screen, (255, 0, 0), (body[0], body[1], 10, 10))

        # Draw apple
        pygame.draw.rect(screen, apple.colour, (apple.body[0], apple.body[1], 10, 10))

        # Collision with apple
        if snake.head[0] == apple.body[0] and snake.head[1] == apple.body[1]:
            score += 1
            snake.add_length(True)
            apple.reset_apple()
        else:
            snake.add_length(False)

        # Collisions with wall or body
        if snake.hit_wall():
            game_over()

            pygame.time.delay(1000)
            running = False

        if snake.hit_body():
            game_over()
            pygame.time.delay(1000)
            running = False

        # Input handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake.direction != 'right':
            snake.direction = "left"
        if keys[pygame.K_RIGHT] and snake.direction != 'left':
            snake.direction = 'right'
        if keys[pygame.K_UP] and snake.direction != 'down':
            snake.direction = 'up'
        if keys[pygame.K_DOWN] and snake.direction != 'up':
            snake.direction = 'down'

        # Move snake
        snake.move()

        # Draw score
        show_score()

        # Update display
        pygame.display.update()

        # Limit FPS
        clock.tick(10)

        # Required by Pygbag: yield to browser event loop
        await asyncio.sleep(0)  # keep argument 0 for Pygbag

    pygame.quit()


# Entry point – this pattern is what Pygbag expects
# Do not put any more code after asyncio.run(main()) for web builds
asyncio.run
