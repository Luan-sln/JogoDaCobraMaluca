import pygame

def tela(wid, hei, nomeJogo):
    display = pygame.display.set_mode((wid, hei))
    pygame.display.set_caption(nomeJogo)
    return display

def color(txt):
    cor = ()
    if txt == "red":
        cor = (219, 31, 31)
    elif txt == "blue":
        cor = (56, 75, 255)
    elif txt == "darkBlue":
        cor =(14, 0, 138)
    elif txt == "black":
        cor = (0, 0, 0)
    elif txt == "green":
        cor = (79, 214, 11)
    elif txt == "yellow":
        cor = (250, 246, 5)
    elif txt == "purple":
        cor = (122, 5, 247)
    elif txt == "orange":
        cor = (245, 113, 5)

    return cor
