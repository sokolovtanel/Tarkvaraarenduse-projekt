import pygame
import sys
import time

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
pall = pygame.image.load("ect/img/ball-1.png")
alus = pygame.image.load("ect/img/pad.png")
pall = pygame.transform.scale(pall, (20, 20)) #laius, kõrgus
alus = pygame.transform.scale(alus, (120, 20))

# taustamuusika
pygame.mixer.music.load("ect/sound/bg.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# põrkeheli
boink = pygame.mixer.Sound("ect/sound/boink.mp3")
boink.set_volume(0.1)

# rect pallile
pall_rect = pall.get_rect()
pall_rect.center = (screenX / 2, screenY / 2)

# rect alusele
alus_rect = alus.get_rect()
alus_rect.center= (screenX / 2, screenY / 1.5)

# kiirused
kiirusX = 3
kiirusY = 3
alusKiirus = 0

running = True
while running:
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # aluse liigutamine nuppudega
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alusKiirus = 3
            if event.key == pygame.K_LEFT:
                alusKiirus = -3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                alusKiirus = 0

    # liigutame alust
    alus_rect.x += alusKiirus

    # aluse seinapiir
    if alus_rect.left < 0 or alus_rect.right >= screenX:
        alusKiirus *= 0

    # liigutame palli
    pall_rect.x += kiirusX
    pall_rect.y += kiirusY

    # pallipõrgatus
    if pall_rect.left < 0 or pall_rect.right >= screenX:
        kiirusX *= -1
    if pall_rect.top < 0 or pall_rect.bottom >= screenY:
        kiirusY *= -1

    # veidra liikumise parandamiseks kontrollime kiirust ka
    if pall_rect.colliderect(alus_rect) and kiirusY > 0:
        # pall tuleb ülevalt (+1 skoor ja heli)
        if pall_rect.bottom <= alus_rect.top + 10:
            kiirusY *= -1
            skoor += 1
            pygame.mixer.Sound.play(boink)
        # pall tuleb küljelt
        else:
            kiirusX *= -1

    # kuvame tausta ja pildid
    screen.fill([153, 204, 255])
    screen.blit(pall, pall_rect)
    screen.blit(alus, alus_rect)

    # kuvame skoori
    font = pygame.font.Font(None, 30)
    text = font.render("Skoor: "+str(skoor), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # kui pall puudutab põhja - mäng suletakse
    if pall_rect.bottom >= screenY:
        # kuvame lõpusõnumi ja sulgeme
        font = pygame.font.Font(None, 60)
        text = font.render("Mäng läbi!", True, (255, 0, 0))
        screen.blit(text, (220, 220))
        pygame.display.flip()
        time.sleep(2)
        running = False

    # ekraanivärskendus
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()

