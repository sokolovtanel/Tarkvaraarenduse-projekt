import pygame
import sys
pygame.init()

# määrame ekraani suuruse
screen = pygame.display.set_mode([300, 300])
# programmi pealkiri
pygame.display.set_caption("Valgusfoor - Tanel Sokolov")
# taustavärv
screen.fill([0, 0, 0])

# pygame.draw.circle(screen, värv, tsentri_pos, raadius)
pygame.draw.circle(screen, [255,0,0], [150, 65],  40)  # punane
pygame.draw.circle(screen, [255,255,0], [150, 150], 40)  # kollane
pygame.draw.circle(screen, [0,255,0], [150, 235], 40)  # roheline

# joonistame jooned
pygame.draw.rect(screen, [128, 128, 128], [100, 15, 100, 270], 2)

# värskendame ekraani
pygame.display.flip()

# hoiame mängu elus (ilma selleta viskab kohe kinni)
running = True
while running:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()