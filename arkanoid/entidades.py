import os
import pygame as pg
from pygame.sprite import Sprite
from . import ALTO, ANCHO, FPS

"""
1. Crear una clase Raqueta
    a. Sea un Sprite -- hecho
    b. Se puede mover. Tendrá un método que se encargue de esto.
    c. Tiene velocidad de movimiento  -- hecho
    d. Tiene que ponder pintarse en pantalla -- hecho
"""


class Raqueta(Sprite):

    margen_inferior = 20
    velocidad = 5
    fps_animacion = 12
    limite_animacion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()
        self.imagenes = [
            pg.image.load(
                os.path.join("resources", "images", "electric00.png")
            ),
            pg.image.load(
                os.path.join("resources", "images", "electric01.png")
            ),
            pg.image.load(
                os.path.join("resources", "images", "electric02.png")
            )]
        self.siguiente_imagen = 0
        self.image = self.imagenes[self.siguiente_imagen]
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))

    def update(self):
        """Actualiza el estado de la raqueta"""

        self.iteracion += 1
        if self.iteracion == self.limite_animacion:
            self.siguiente_imagen += 1
            if self.siguiente_imagen >= len(self.imagenes):
                self.siguiente_imagen = 0
            self.image = self.imagenes[self.siguiente_imagen]
            self.iteracion = 0

        # calcular y establecer la nueva posición
        # en función de la tecla pulsada (si la hay)
        teclas = pg.key.get_pressed()
        if teclas[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if teclas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0