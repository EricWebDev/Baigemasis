import pygame

pygame.init()

# Set up the display
sw, sh = 800, 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption('Bybis')

# Load the image
bg = pygame.image.load('asteroidsPics/starbg.png')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(bg, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
