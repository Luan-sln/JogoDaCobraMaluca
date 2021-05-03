import pygame
import funcoes as f

pygame.init()
wid = 800
hei = 600
nameGame = "Óia a COBRA"
dis = f.tela(wid, hei, nameGame)
##################################
squareSz = 20

clock = pygame.time.Clock()

speed = 18



def gameLoop():
    gameOver = False
    psX = wid/2
    psY = 0
    while not gameOver:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

        
        
        
        dis.fill(f.color("black"))
        pygame.draw.rect(dis, f.color("red"), [psX, psY, squareSz, squareSz])
        psY += speed


        if psY > (hei - squareSz):
            psY = hei - squareSz
        if psY < 0:
            psY = 0
        if psX > (wid - squareSz):
            psX = wid - squareSz
        if psX < 0:
            psX = 0

        pygame.display.update()
        clock.tick(speed)
    pygame.quit()
gameLoop()