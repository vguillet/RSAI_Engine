
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import time

# Libs
import pygame as pg

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Button:
    def __init__(self, screen, x, y, w, h, label, action=None):
        self.label = label

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        self.button_width = w
        self.button_height = h

        self.button_x = x
        self.button_y = y - self.button_height

        # --> If mouse is on button
        if self.button_x + self.button_width > mouse[0] > self.button_x \
                and self.button_y + self.button_height > mouse[1] > self.button_y:
            pg.draw.rect(screen, (255, 255, 200), (self.button_x, self.button_y, self.button_width, self.button_height))

            if click[0] == 1 and action is not None:
                print("Click")
                action()

        else:
            pg.draw.rect(screen, (255, 255, 255), (self.button_x, self.button_y, self.button_width, self.button_height))
        pg.display.update()

        smallText = pg.font.Font("freesansbold.ttf", 10)

        text_surface = smallText.render(self.label, True, (0, 0, 0))
        text_rect = text_surface.get_rect()

        text_rect.center = ((self.button_x + (self.button_width / 2)), (self.button_y + (self.button_height / 2)))
        screen.blit(text_surface, text_rect)

        # pg.display.update()
        # time.sleep(0.2)
