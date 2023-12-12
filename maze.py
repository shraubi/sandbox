import pygame
import sys

pygame.init()

# display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define maze layout (0: path, 1: wall, 2: exit to Heaven, 3: exit to Hell)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 2, 1, 3, 1, 1, 3, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Maze cell size and position
cell_size = min(width // len(maze[0]), height // len(maze))
start_x, start_y = 0, 0

# Player position
player_x, player_y = 1, 1

# Font setup
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and maze[player_y][player_x - 1] != 1:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and maze[player_y][player_x + 1] != 1:
                player_x += 1
            elif event.key == pygame.K_UP and maze[player_y - 1][player_x] != 1:
                player_y -= 1
            elif event.key == pygame.K_DOWN and maze[player_y + 1][player_x] != 1:
                player_y += 1

    # Check for exits
    if maze[player_y][player_x] == 2:
        # Exit to Heaven
        screen.fill(white)
        text = font.render("Congratulations! You reached Heaven.", True, black)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    elif maze[player_y][player_x] == 3:
        # Exit to Hell
        screen.fill(red)
        text = font.render("Oh no! You fell into Hell.", True, white)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, white, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))
            elif maze[row][col] == 2:
                pygame.draw.rect(screen, green, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))
            elif maze[row][col] == 3:
                pygame.draw.rect(screen, blue, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, black, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

    # Draw player
    pygame.draw.rect(screen, red, (start_x + player_x * cell_size, start_y + player_y * cell_size, cell_size, cell_size))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
