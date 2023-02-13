import pygame as pg
from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Portada, Partida, MejoresJugadores


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

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
