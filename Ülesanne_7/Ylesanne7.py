import pygame
import sys
import random
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
fps = 60
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("Hiir")

# muutujad
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

    # hiireliigutused / klõpsud
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # siia kogume ringide koguse
    rKogus = len(ringid)

    # kui tehakse hiireklikk ja seda ei ole veel loendis, lisatakse loendisse
    if any(click) and mousePos not in [pos for pos, varv in ringid]:
        suvav2rv = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ringid.append((mousePos, suvav2rv))

    # kui loendis on üle 10 ringi, kustutatakse esimene
    if rKogus > 10:
        del ringid[0]

    # joonistame ringid ekraanile
    for pos, suvav2rv in ringid:
        pygame.draw.circle(screen, suvav2rv, pos, rSuurus, 1)

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()

