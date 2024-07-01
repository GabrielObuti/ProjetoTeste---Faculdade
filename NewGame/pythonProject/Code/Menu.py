#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_GOLD, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/4.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        menu_option=0
        while True:
            ###Desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "Mountain", COLOR_GOLD, ((WIN_WIDTH / 2), (WIN_HEIGHT / 3)))
            self.menu_text(100, "Shooter", (216, 182, 31), ((WIN_WIDTH / 2), (WIN_HEIGHT / 3.5)))

            for i in range(len(MENU_OPTION)):
                if i ==menu_option:
                    self.menu_text(30,MENU_OPTION[i],COLOR_YELLOW,((WIN_WIDTH / 2),550+ 45 *i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 550 + 45 * i))
                pygame.display.flip()

            ###Verificar Evento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # Se alguma tecla for clicada
                    if event.key == pygame.K_DOWN: # Se a tecla clicada for seta para baixo
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # Se a tecla clicada for seta para baixo
                        if menu_option > 0:
                            menu_option -=1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
