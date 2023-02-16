import os
import pygame as pg
from . import ALTO, ANCHO, FPS
from .entidades import Raqueta


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        """
        Este método debe ser implementado por cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        ruta = os.path.join("resources", "images", "arkanoid_name.png")
        self.logo = pg.image.load(ruta)

        ruta_tipo = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(ruta_tipo, 28)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_texto()
            pg.display.flip()
        return False

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO/3
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa <espacio> para comenzar la partida"
        # texto = pg.font.Font.render(self.tipografia, mensaje, True, (255, 255, 255))
        texto = self.tipografia.render(mensaje, True, (255, 255, 255))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        # crear la ruta donde está la imagen
        ruta = os.path.join("resources", "images", "background.jpg")
        # cargar la imagen en un atributo
        self.fondo = pg.image.load(ruta)
        self.jugador = Raqueta()

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            self.reloj.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True

            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            pg.display.flip()
        return False

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        # pintar la imagen de fondo en la pantalla
        self.pantalla.blit(self.fondo, (0, 0))


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
        return False
