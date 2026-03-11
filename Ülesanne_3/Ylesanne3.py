import pygame
import sys
pygame.init()

# värvid
Punane = [255, 0, 0]
Roheline = [0, 255, 0]
Sinine = [0, 0, 255]
Must = [0, 0, 0]
HRoheline = [144, 238, 144]

# ekraani seaded
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 3")
screen.fill(HRoheline)

# parameetrid
ruudu_suurus = 20
joone_laius = 2
read = 24
veerud = 32
v2rv = Punane

# ruudustiku joonistamise loop
def ruudustik(surface):
    # vertikaalsed jooned
    for veerg in range(veerud + 1):
        x = veerg * ruudu_suurus
        pygame.draw.line(surface, v2rv, (x, 0), (x, read * ruudu_suurus), joone_laius)
    # horisontaalsed jooned
    for rida in range(read + 1):
        y = rida * ruudu_suurus
        pygame.draw.line(surface, v2rv, (0, y), (veerud * ruudu_suurus, y), joone_laius)

# joonistame ruudustiku
ruudustik(screen)

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