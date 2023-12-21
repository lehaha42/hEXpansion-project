from settings import *


class Texture:
    def __init__(self, app):
        self.app = app

        self.textures = {}

        self.load('test.png')
        self.load('background.png')

    def get_texture(self, name):
        return self.textures.get(name) or None

    def load(self, file_name: str):
        texture = pg.image.load(f'textures/{file_name}')
        self.textures[file_name] = texture
