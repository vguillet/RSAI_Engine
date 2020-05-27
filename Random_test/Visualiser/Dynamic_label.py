
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


class Dynamic_label():
    def __init__(self, label_lst: "str or str lst", pos_lst: list,
                 label_size: int,
                 down_shift: "+ int for down", side_shift: "+ int for right",
                 margin: int):

        # ----- Setup reference properties
        self.pos_lst = pos_lst

        # --> In case of fixed label, create list of fixed label
        if type(label_lst) is str:
            self.label_lst = [label_lst] * len(pos_lst)
        else:
            self.label_lst = label_lst

        self.label_size = label_size

        self.down_shift = down_shift
        self.side_shift = side_shift
        self.margin = margin

        self.font = pg.font.SysFont("comicsansms", self.label_size)

        self.label = self.font.render(self.label_lst[0], True, (0, 0, 0))
        self.label_pos = (self.pos_lst[0][0] + self.side_shift - self.margin,
                          self.pos_lst[0][1] + self.down_shift - self.margin)

    def update(self, step):
        # --> Update step tracker
        self.step = step

        if self.step >= len(self.label_lst):
            return

        else:
            # --> Set text
            self.label = self.font.render(self.label_lst[self.step], False, (0, 0, 0))

            # --> Set position
            self.label_pos = (self.pos_lst[self.step][0] + self.down_shift - self.margin,
                              self.pos_lst[self.step][1] + self.side_shift - self.margin)

            if self.label_pos[0] >= 800:
                self.label_pos = (self.pos_lst[self.step][0] + self.down_shift - self.margin,
                                  self.pos_lst[self.step][1] - self.side_shift - self.margin,
                                  0)

            return