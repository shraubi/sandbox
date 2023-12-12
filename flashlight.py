import pygame
import sys

pygame.init()

# display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Flashlight")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255, 105, 180)

# Initial flashlight state and color
flashlight_on = False
flashlight_color = red

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flashlight_on = not flashlight_on
            elif event.key == pygame.K_LEFT:
                flashlight_color = red
            elif event.key == pygame.K_RIGHT:
                flashlight_color = blue
            elif event.key == pygame.K_UP:
                flashlight_color = green
            elif event.key == pygame.K_DOWN:
                flashlight_color = pink

    screen.fill(flashlight_color if flashlight_on else black)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
