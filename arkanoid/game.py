import os
import pygame as pg
from . import ALTO, ANCHO
from .escenas import Portada, Partida, MejoresJugadores


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ Version")

        # Mac: resources/images/icon.png
        ruta = os.path.join("resources", "images", "icon.png")
        icono = pg.image.load(ruta)
        pg.display.set_icon(icono)

        objeto_portada = Portada(self.pantalla)
        objeto_partida = Partida(self.pantalla)
        objeto_mejores = MejoresJugadores(self.pantalla)

        self.escenas = [
            objeto_portada,
            objeto_partida,
            objeto_mejores
        ]

        # Escrito de forma simplificada:
        #
        # self.escenas = [
        #     Portada(self.pantalla)
        #     Partida(self.pantalla)
        #     MejoresJugadores(self.pantalla)
        # ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()
