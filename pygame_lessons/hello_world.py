import sys
import pygame
import pygame.locals


#initalize pygame
pygame.init()

#Sets up the display surface for the game
DISPLAY_SURFACE = pygame.display.set_mode((400,300))

#Sets the heading caption
pygame.display.set_caption("Hello World!")

#main game loop
while True:
    #loops through all the events captured from the
    #screen
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    #updates the screen
    pygame.display.update()
