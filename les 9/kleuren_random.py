import pygame, sys, time, random
from pygame.locals import QUIT

pygame.init()  

breedte = int(input("Breedte: "))
hoogte = int(input("Hoogte: "))
kleur = (0,0,0)
dikte = 1

DISPLAYSURF = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Codefever Paint')
DISPLAYSURF.fill((255,255,255))

mode='red_up'
red=0
green=0
blue=0
while True:
    muispositie = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (True,False,False):
      pygame.draw.circle(DISPLAYSURF, kleur, muispositie, dikte)
      kleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
      
    if pygame.mouse.get_pressed() == (False,False,True):
        pygame.draw.circle(DISPLAYSURF, (255,255,255), muispositie, 10)
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
          if event.key == pygame.K_i:
            fileImport = input("import file: ")
            afbeelding = pygame.image.load(fileImport)
            afbeelding = pygame.transform.scale(afbeelding,(breedte,hoogte))
            DISPLAYSURF.blit(afbeelding, (0,0))
          if event.key == pygame.K_s:
            filename=input("save as: ")
            pygame.image.save(DISPLAYSURF, filename+".jpg")
          if event.key == pygame.K_r:
              kleur=(255,0,0)
          if event.key == pygame.K_g:
              kleur=(0,255,0)
          if event.key == pygame.K_b:
              kleur=(0,0,255)
          if event.key == pygame.K_UP:
              dikte += 1
          if event.key == pygame.K_DOWN:
              dikte -= 1
          if event.key == pygame.K_k:
             print("Stel zelf je kleur samen")
             rood=int(input("rood(0-255): "))
             groen=int(input("groen(0-255): "))
             blauw=int(input("blauw(0-255): "))
             kleur = (rood, groen, blauw)  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
       
    pygame.display.update()