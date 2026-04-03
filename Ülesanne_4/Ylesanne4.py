import pygame
import sys
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
fps = 60
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("Ülesanne 4")

# pildid
bg = pygame.image.load("img/bg_rally.jpg")
auto1 = pygame.image.load("img/f1_red.png")
auto2 = pygame.image.load("img/f1_blue.png")

# definitsioonid
laius1 = 180
korgus1 = -100
laius2 = 420
korgus2 = -200
skoor = 0

# stardipositsioon ja kiirus
posX, posY = laius1, korgus1
posX2, posY2 = laius2, korgus2
speedX = 3

running = True
while running:
    # liikumine
    posY += speedX
    posY2 += speedX

    # kui auto jõuab lõppu, liigutame algusesse
    if posY > screenY:
        posY = korgus1
        skoor += 1

    if posY2 > screenY:
        posY2 = korgus2
        skoor += 1

    # pildikesed ekraanile
    screen.blit(bg, (0, 0))
    screen.blit(auto1, (300, 390))  # y x (vp üa)
    screen.blit(auto2, (posX, posY))
    screen.blit(auto2, (posX2, posY2))

    # kuvame skoori
    font = pygame.font.Font(None, 30)
    text = font.render("Skoor: "+str(skoor), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()
