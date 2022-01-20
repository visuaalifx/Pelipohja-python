#resurssien lataus
import pygame , sys
pygame.init()

#variables

virtanappula = 1
leveys= 300
korkeus= 300

#kuvaruutu

screen = pygame.display.set_mode([leveys,korkeus])
pygame.display.set_caption("darkrinth")
taustakuva = pygame.image.load("tausta.png").convert()


#objects

class hahmo(pygame.sprite.Sprite):
    def __init__(pelaajaobjekti):  #init luo funktiosta toimivan objektin?`?????
        pygame.sprite.Sprite.__init__(pelaajaobjekti)
        pelaaja = pygame.image.load("pingviini.png").convert()
        pelaajaobjekti.images = []
        pelaajaobjekti.images.append(pelaaja)
        pelaajaobjekti.image = pelaajaobjekti.images [0]
        pelaajaobjekti.rect = pelaajaobjekti.image.get_rect()  #luo objektille neliön muotoiset rajat?


#pelaaja
hahmo = hahmo()     #luo pelaajan
hahmo.rect.x = 0
hahmo.rect.y = 0
pelaajalista = pygame.sprite.Group()   #pelaajalista = sprite ryhmä
pelaajalista.add(hahmo)
pelaajalista.draw(taustakuva)          #piirtää pelaajan
screen.blit (taustakuva,(0,0))








#peliloop

while virtanappula == 1:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            virtanappula = 0
            pygame.quit()
            sys.exit()
        pygame.display.update()




