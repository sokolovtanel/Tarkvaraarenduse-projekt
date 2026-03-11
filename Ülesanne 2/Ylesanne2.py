import pygame
pygame.init()
#ekraani seaded
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

#Lisame pildid
bg = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg, (0, 0))

seller = pygame.image.load("img/seller.png")
seller = pygame.transform.scale(seller, (255, 310)) #laius pikkus
screen.blit(seller, (105, 155)) # y x (vp üa)

chat = pygame.image.load("img/chat.png")
chat = pygame.transform.scale(chat, (260, 195))
screen.blit(chat, (245, 70))

# lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Tere, olen Tanel", True, (255, 255, 255))
screen.blit(text, (300, 140))

pygame.display.flip()

#hoiame mängu elus (ilma selleta viskab kohe kinni)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False