import pygame
import sys
import time
import random

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
fps = 60
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("Hiir")

# def
ringid = []
rSuurus = 10

running = True
while running:
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ekraani taustavärv
    screen.fill([153, 204, 255])

    rKogus = len(ringid)


    # hiireliigutused / klõpsud
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # kui tehakse hiireklikk ja seda ei ole veel loendis, lisatakse loendisse
    if any(click) and mousePos not in ringid:
        ringid.append(mousePos)

    # kui loendis on üle 10 ringi, kustutatakse esimene
    if rKogus >= 10:
        del ringid[0]

    # loop-iga joonistatakse ekraanile
    for i in ringid:
        pygame.draw.circle(screen, (0, 0, 255), i, rSuurus, 1)

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()

