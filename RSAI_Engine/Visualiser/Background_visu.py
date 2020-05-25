
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math

# Libs
import pygame as pg

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Background(pg.sprite.Sprite):
    def __init__(self,
                 image_file_path, alternative_image_path,
                 location, screen_size):
        super().__init__()

        # --> Load image
        self.image = pg.image.load(image_file_path)

        # --> Scale image
        self.image = pg.transform.scale(self.image, screen_size)

        # --> Load alternative image

        # --> Scale alternative image
        self.image = pg.transform.scale(self.image, screen_size)
        
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def set_map_image(self):
        self.image = pg.image.load(image_file_path)