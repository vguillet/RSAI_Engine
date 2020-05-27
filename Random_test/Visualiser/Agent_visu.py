
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


class Agent_visu(pg.sprite.Sprite):
    def __init__(self, agent: "Agent object", margin: int):
        super().__init__()

        # ----- Setup reference properties
        self.agent = agent
        self.original_image = pg.image.load("RSAI_Engine/Data/Visualiser_Assets/agent.png").convert()
        self.original_image = pg.transform.scale(self.original_image, (20, 20))
        self.original_image.set_colorkey((0, 0, 0))  # Don't display black

        self.image = self.original_image

        self.margin = margin
        self.rect = self.image.get_rect()
        self.rect.center = (agent.pos[0] - self.margin, agent.pos[1] - self.margin)
        self.step = -1

    def update(self, step):
        # --> Update step tracker
        self.step = step

        if self.step >= len(self.agent.pos_history):
            return

        else:
            # --> Save current parameters
            x, y = self.rect.center

            # --> Solve displacement
            delta_x = self.agent.pos_history[self.step][0] - x - self.margin
            delta_y = self.agent.pos_history[self.step][1] - y - self.margin

            angle = (math.atan2(delta_y, delta_x) * 180 / math.pi)

            # --> Rotate image
            self.image = pg.transform.rotate(self.original_image, int(angle))

            # --> Move image
            self.rect = self.image.get_rect()  # Replace old rect with new rect.
            self.rect.center = (self.agent.pos_history[self.step][0] - self.margin,
                                self.agent.pos_history[self.step][1] - self.margin)  # Put the new rect's center at old center.

            return

# def update(self):
#         import random
#         x, y = self.rect.center  # Save its current center.
#
#         delta_x = random.randint(-20, 20)
#         delta_y = random.randint(-20, 20)
#
#         angle = (math.atan2(delta_y, delta_x)*180/math.pi)
#
#         # --> Rotate image
#         self.image = pg.transform.rotate(self.original_image, angle)
#
#         # --> Move image
#         self.rect = self.image.get_rect()  # Replace old rect with new rect.
#         self.rect.center = (x + delta_x, y + delta_y)  # Put the new rect's center at old center.
#
#         if self.rect.x < 0:
#             self.rect.x = 0
#
#         if self.rect.y < 0:
#             self.rect.y = 0
#
#         if self.rect.x > 800:
#             self.rect.x = 800
#
#         if self.rect.y > 800:
#             self.rect.y = 800
