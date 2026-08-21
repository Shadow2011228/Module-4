import numpy as np
import pygame as pg
import cv2
from numba import njit
from loguru import logger as log


class ArtConverter:
    def __init__(self, path='img/wolf.jpg'):
        self.path = path
        pg.init()
        self.image = self.get_image()
        self.RES = self.width, self.height = self.image.shape[0], self.image.shape[1]
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        log.debug(self.image)


    def draw(self):
        pg.surfarray.blit_array(self.screen, self.image)
        cv2.imshow("window", self.cv2_image)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        image = cv2.cvtColor(transposed_image, cv2.COLOR_RGB2BGR)
        return image

if __name__ == '__main__':
    app = ArtConverter()
    app.run()




