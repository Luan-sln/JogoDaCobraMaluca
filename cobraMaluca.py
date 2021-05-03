import pygame
import funcoes as f

pygame.init()
wid = 800
hei = 600
nameGame = "Óia a COBRA"
dis = f.tela(wid, hei, nameGame)

red = (219, 31, 31)
blue = (56, 75, 255)

squareSz = 20
circleRds = 10

psX = 200
psY = 100

def gameLoop():
    gameOver = False
    while not gameOver:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
        pygame.draw.rect(dis, red, [psX, psY, squareSz, squareSz])
        pygame.draw.circle(dis, blue, (psX + 200, psY), circleRds)
    pygame.quit()
    
gameLoop()