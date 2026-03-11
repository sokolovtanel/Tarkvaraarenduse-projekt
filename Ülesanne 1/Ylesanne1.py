import pygame
import sys
pygame.init()

# määrame ekraani suuruse
screen = pygame.display.set_mode([300, 300])
# programmi pealkiri
pygame.display.set_caption("Lumemees - Tanel Sokolov")
# taustavärv
screen.fill([0, 0, 0])

# keha - 3 ringi
# pygame.draw.circle(screen, värv, tsentri_pos, raadius)
pygame.draw.circle(screen, [255,255,255], [150, 220], 50)  # alumine
pygame.draw.circle(screen, [255,255,255], [150, 135], 40)  # keskmine
pygame.draw.circle(screen, [255,255,255], [150, 70],  30)  # pea

# Silmad
pygame.draw.circle(screen, [0,0,0], [140,65], 5) #138 5
pygame.draw.circle(screen, [0,0,0], [160, 65], 5) #162 5

# Nina (punane kolmnurk)
#pygame.draw.polygon(screen, värv, koordinaatide_loend)
pygame.draw.polygon(screen, [255,0,0], [[150, 90], [145, 75], [155, 75]])

#värskendame ekraani
pygame.display.flip()

#hoiame mängu elus (ilma selleta viskab kohe kinni)
running = True
while running:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()