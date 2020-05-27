
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
                 environment,
                 location, screen_size):
        super().__init__()

        # --> Set properties
        self.screen_size = screen_size
        self.location = location

        # --> Load image
        self.set_map_image(environment)

        self.view = "map"

    def switch_view(self, environment):
        if self.view == "map":
            self.set_sim_image(environment)
        else:
            self.set_map_image(environment)
        return

    def set_map_image(self, environment):
        print("Setting map image")
        # --> Load image
        self.image = pg.image.load(environment.image_path)

        # --> Scale image
        self.image = pg.transform.scale(self.image, self.screen_size)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.location

        # --> Set view tracker
        self.view = "map"

    def set_sim_image(self, environment):
        print("Seting sim image")
        # --> Load image
        self.image = pg.image.load(environment.image_path)

        # --> Scale image
        self.image = pg.transform.scale(self.image, self.screen_size)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.location

        # --> Set view tracker
        self.view = "sim"
