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

# definitsioonid
skoor = 0

# pildid
pall = pygame.image.load("img/ball-1.png")
alus = pygame.image.load("img/pad.png")
pall = pygame.transform.scale(pall, (20, 20)) #laius, kõrgus
alus = pygame.transform.scale(alus, (120, 20))

# rect pallile
pall_rect = pall.get_rect()
pall_rect.center = (screenX / 2, screenY / 2)

# rect alusele
alus_rect = alus.get_rect()
alus_rect.center= (screenX / 2, screenY / 1.5)

# kiirused
kiirusX = 3
kiirusY = 3
alusKiirus = 3

running = True
while running:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # liigutame palli
    pall_rect.x += kiirusX
    pall_rect.y += kiirusY

    # liigutame alust
    alus_rect.x += alusKiirus

    # pallipõrgatus
    if pall_rect.left < 0 or pall_rect.right >= screenX:
        kiirusX *= -1

    if pall_rect.top < 0 or pall_rect.bottom >= screenY:
        kiirusY *= -1

    # aluse põrkamine
    if alus_rect.left < 0 or alus_rect.right >= screenX:
        alusKiirus *= -1

    # veidra liikumise parandamiseks kontrollime kiirust ka
    if pall_rect.colliderect(alus_rect) and kiirusY > 0:
        # pall tuleb ülevalt (+1 skoor)
        if pall_rect.bottom <= alus_rect.top + 10:
            kiirusY *= -1
            skoor += 1
        # pall tuleb küljelt
        else:
            kiirusX *= -1

    # kui pall puudutab põhja -1 skoorist
    if pall_rect.bottom >= screenY:
        skoor += -1

    # kuvame tausta ja pildid
    screen.fill([153, 204, 255])
    screen.blit(pall, pall_rect)
    screen.blit(alus, alus_rect)

    # kuvame skoori
    font = pygame.font.Font(None, 30)
    text = font.render("Skoor: "+str(skoor), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()