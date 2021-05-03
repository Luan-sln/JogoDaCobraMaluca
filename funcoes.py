import pygame

def tela(wid, hei, nomeJogo):
    display = pygame.display.set_mode((wid, hei))
    pygame.display.set_caption(nomeJogo)
    return display