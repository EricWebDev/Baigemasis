import pygame

sw = 800
sh = 800

bg = pygame.image.load('asteriodsPics\starbg.png')
alienImg = pygame.image.load('asteriodsPics/alienShip.png')
playerRocket = pygame.image.load('asteriodsPics/spaceRocket.png')
star = pygame.image.load('asteriodsPics/star.png')
asteroid50 = pygame.image.load('asteriodsPics/asteroid50.png')
asteroid100 = pygame.image.load('asteriodsPics/asteroid100.png')
asteroid150 = pygame.image.load('asteriodsPics/asteroid150.png')

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

gameover= False



def redrawGameWindow():
    win.blit(bg, (0,0))
    
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    if not gameover:
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            
pygame.quit()