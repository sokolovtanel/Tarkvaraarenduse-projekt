import pygame
pygame.init()

Green = [153, 255, 153]

#ekraani seaded
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 3")
screen.fill(Green)

pygame.display.flip()

#hoiame mängu elus (ilma selleta viskab kohe kinni)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False