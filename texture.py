from settings import *


class Texture:
    def __init__(self, app):
        self.app = app

        self.texture_0 = self.load('test.png')
        self.texture_background = self.load('background.png')

    def load(self, file_name: str):
        texture = pg.image.load(f'textures/{file_name}')

        return texture
