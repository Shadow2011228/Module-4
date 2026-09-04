import numpy as np
import pygame as pg
import cv2
from numba import njit
from loguru import logger as log


class ArtConverter:
    def __init__(self, path='video/madagaskar.mp4', font_size=4, color='white', color_lvl=32):
        self.path = path
        pg.init()
        self.ASCII_CHARS = ' ixzao*MW&8%B@$#'
        self.capture = cv2.VideoCapture(path)
        self.color_lvl = color_lvl
        self.font_size = font_size
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)
        self.font = pg.font.SysFont('Consolas', font_size, bold=True)
        self.CHAR_STEP = int(font_size * 0.6)
        # self.RENDERED_ASCII_CHARS = [self.font.render(char, False, color) for char in self.ASCII_CHARS]
        self.PALETTE, self.COLOR_COEFF = self.create_palette()


        self.rgb_image, self.gray_image = self.get_image()
        self.RES = self.width, self.height = self.gray_image.shape[0], self.gray_image.shape[1]
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        log.debug(self.gray_image)
        self.rec_fps = 60
        self.record = False
        self.recorder = cv2.VideoWriter('output/video.mp4', cv2.VideoWriter_fourcc(*'avc1'), self.rec_fps, self.RES)

    def get_frame(self):
        frame = pg.surfarray.array3d(self.screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.transpose(frame)
        return frame

    def record_frame(self):
        if self.record:
            frame = self.get_frame()
            self.recorder.write(frame)
            cv2.imshow('frame', frame)


    def draw(self):
        # pg.surfarray.blit_array(self.screen, self.image)
        # cv2.imshow("window", self.cv2_image)
        self.screen.fill("black")
        self.draw_converted_image()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        print(1)
                        self.record = not self.record
                    if event.key == pg.K_ESCAPE and self.record:
                        print(2)
                        self.record = not self.record
                        cv2.destroyAllWindows()

            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()

    def get_image(self):
        # self.cv2_image = cv2.imread(self.path)
        ok, self.cv2_image = self.capture.read()
        if not ok:
            exit()
        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        return rgb_image, gray_image

    def draw_converted_image(self):
        self.rgb_image, self.gray_image = self.get_image()
        char_indices = self.gray_image // self.ASCII_COEFF
        color_indices = self.rgb_image // self.COLOR_COEFF

        values = conversion(self.rgb_image, self.gray_image, self.width,
                            self.height, self.COLOR_COEFF, self.ASCII_COEFF, self.CHAR_STEP)
        for char_index, color, pos in values:
            char = self.ASCII_CHARS[char_index]
            self.screen.blit(self.PALETTE[char][color], pos)

    def create_palette(self):
        colors, color_coeff = np.linspace(0, 255, num=self.color_lvl, dtype=int, retstep=True)
        color_palette = [np.array([r, g, b]) for r in colors for g in colors for b in colors]
        palette = dict.fromkeys(self.ASCII_CHARS, None)
        color_coeff = int(color_coeff)
        for char in palette:
            char_palette = {}
            for color in color_palette:
                color_key = tuple(color // color_coeff)
                char_palette[color_key] = self.font.render(char, False, tuple(color))
            palette[char] = char_palette
        return palette, color_coeff

@njit(fastmath=True)
def conversion(image, gray_image, width, height, color_coeff, ascii_coeff, step):
    values = []
    for x in range(0, width, step):
        for y in range(0, height, step):
            char_index = gray_image[x, y] // ascii_coeff
            if char_index:
                r, g, b = image[x, y] // color_coeff
                values.append((char_index, (r, g, b), (x, y)))
    return values


if __name__ == '__main__':
    app = ArtConverter()
    app.run()




