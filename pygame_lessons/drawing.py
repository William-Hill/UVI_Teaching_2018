import sys
import pygame
import pygame.locals


#initalize pygame
pygame.init()

#Sets up the display surface for the game
DISPLAY_SURFACE = pygame.display.set_mode((500,400), 0 ,32)

#Sets the heading caption
pygame.display.set_caption("Drawing")

#setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
BLUE = (0,0,255)

DISPLAY_SURFACE.fill(WHITE)
#draws a maroon pentagon
pygame.draw.polygon(DISPLAY_SURFACE, MAROON, ((146, 0), (291, 106), (236,277), (56,277), (0,106)))
pygame.draw.line(DISPLAY_SURFACE, BLUE, (60,60), (120,60), 4)
pygame.draw.circle(DISPLAY_SURFACE, BLUE, (300, 50), 20, 0)

pix_obj = pygame.PixelArray(DISPLAY_SURFACE)
pix_obj[480][380] = BLACK
del pix_obj

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
