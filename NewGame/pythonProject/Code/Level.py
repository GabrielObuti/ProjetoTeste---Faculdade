#!/usr/bin/python
#-*- coding: utf-8 -*-
from Code.Entity import Entity


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.mode = menu_option  #Opção do menu
        self.entity_list: list[Entity] = []


    def run(self, ):
        pass

#PAROU EM 1:06:48
#FAZENDO A CRIAÇÃO DO BACKGROUND
#ULTIMA EXPLICAÇÃO FOI: A QUEBRA DA IMAGEM DO BACKGROUND COM TEMPOS DIFERENTES DE MOVIMENTAÇÃO
#FAZENDO ISSO, DA IMPRESSÃO DE MOVIMENTAÇÃO DO FUNDO DE UMA FORMA ANIMADA
#UMA PARTE SE MOVE MAIS RÁPIDA QUE A OUTRA