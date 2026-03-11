import pygame
import sys
pygame.init()

# värvid
Green = [153, 255, 153]

#ekraani seaded
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 3")
screen.fill(Green)
# ekraani värskendamine
pygame.display.flip()







# hoiame mängu elus (ilma selleta viskab kohe kinni)
running = True
while running:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()