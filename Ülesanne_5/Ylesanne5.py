import pygame
import sys
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
fps = 60
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("PingPong")

# pildid
pall = pygame.image.load("img/ball-1.png")
alus = pygame.image.load("img/pad.png")

# rect pallile
pall_rect = pall.get_rect()
pall_rect.center = (screenX / 2, screenY / 2)

# kiirused
kiirusX = 3
kiirusY = 3

running = True
while running:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # liigutame palli
    pall_rect.x += kiirusX
    pall_rect.y += kiirusY

    # pallipõrgatus
    if pall_rect.left < 0 or pall_rect.right >= screenX:
        kiirusX *= -1

    if pall_rect.top < 0 or pall_rect.bottom >= screenY:
        kiirusY *= -1

    screen.fill([153, 204, 255])
    screen.blit(pall, pall_rect)

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()





'''
*Lisa ja animeeri pall
palli suurus 20×20
*pall liigub sinu valitud kiirusega
*pall põrkub seintest tagasi
Lisa ja animeeri alus
aluse suurus 120×20
aluse y-koordinaat on keskkohast allpool. Näiteks screenY/1.5
alus liigub vasakule/paremale (vahetab suunda, kui puudub seinu)
Kokkupõrke tuvastamine
kui pall puutub alust siis muudab suunda.
kui pall käitub kokkupuutel alusega imelikult, siis lisa tingimusse kontroll, et palli y-suund oleks suurem kui null (ballSpeedY > 0)
Boonus
kui pall puudub alumist äärt, siis saab mängija negatiivse punkti
kui pall puutub alust, siis saab positiivse punkti
kuva tulemus mängu ülemises nurgas
'''