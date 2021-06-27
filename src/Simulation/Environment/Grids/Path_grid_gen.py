
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import cv2
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from src.Simulation.Environment.Grids.Tools.Grid_tools import reduce_grid_scale

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Own modules


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


def gen_path_grid(world_image, path_image_path=None):
    if Path(path_image_path).is_file():
        mask = cv2.imread(path_image_path, cv2.IMREAD_UNCHANGED)

    else:
        # --> Load image
        img_hsv = cv2.cvtColor(world_image, cv2.COLOR_BGR2HSV)

        # --> Filter image colors
        # -> Create stone_road mask
        stone_road_low = np.asarray([0, 0, 80])
        stone_road_high = np.asarray([0, 0, 80])

        stone_road_mask = cv2.inRange(img_hsv, stone_road_low, stone_road_high)

        # -> Create desert_road mask
        desert_road_low = np.asarray([26, 122, 130])
        desert_road_high = np.asarray([26, 122, 130])

        desert_road_mask = cv2.inRange(img_hsv, desert_road_low, desert_road_high)

        # -> Create dirt_road_1 mask
        dirt_road_1_low = np.asarray([20, 51, 120])
        dirt_road_1_high = np.asarray([20, 51, 120])

        dirt_road_1_mask = cv2.inRange(img_hsv, dirt_road_1_low, dirt_road_1_high)

        # -> Create dirt_road_2 mask
        dirt_road_2_low = np.asarray([20, 102, 120])
        dirt_road_2_high = np.asarray([20, 102, 120])

        dirt_road_2_mask = cv2.inRange(img_hsv, dirt_road_2_low, dirt_road_2_high)

        # -> Create dirt_road_3 mask
        dirt_road_3_low = np.asarray([20, 153, 80])
        dirt_road_3_high = np.asarray([20, 153, 80])

        dirt_road_3_mask = cv2.inRange(img_hsv, dirt_road_3_low, dirt_road_3_high)

        # -> Create dirt_road_4 mask
        dirt_road_4_low = np.asarray([22, 95, 116])
        dirt_road_4_high = np.asarray([22, 95, 116])

        dirt_road_4_mask = cv2.inRange(img_hsv, dirt_road_4_low, dirt_road_4_high)

        # -> Create dirt_road_5 mask
        dirt_road_5_low = np.asarray([21, 185, 84])
        dirt_road_5_high = np.asarray([21, 185, 84])

        dirt_road_5_mask = cv2.inRange(img_hsv, dirt_road_5_low, dirt_road_5_high)

        # -> Create dirt_road_6 mask
        dirt_road_6_low = np.asarray([19, 209, 61])
        dirt_road_6_high = np.asarray([19, 209, 61])

        dirt_road_6_mask = cv2.inRange(img_hsv, dirt_road_6_low, dirt_road_6_high)

        # -> Add masks
        mask = cv2.bitwise_or(stone_road_mask, desert_road_mask)
        mask = cv2.bitwise_or(dirt_road_1_mask, mask)
        mask = cv2.bitwise_or(dirt_road_2_mask, mask)
        mask = cv2.bitwise_or(dirt_road_3_mask, mask)
        mask = cv2.bitwise_or(dirt_road_4_mask, mask)
        mask = cv2.bitwise_or(dirt_road_5_mask, mask)
        mask = cv2.bitwise_or(dirt_road_6_mask, mask)

        # --> Save obstacle image if path provided
        if path_image_path is not None:
            cv2.imwrite(path_image_path, mask)

        # cv2.imshow("mask", mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # -> Set obstacles to 1 and rest to 0 on mask
        mask[mask == 0] = int(0)
        mask[mask == 255] = int(1)

    # --> Reduce mask to world scale
    world_path_array = reduce_grid_scale(array=mask, scale_factor=4)
    # np.save("world_array", world_path_array)

    return world_path_array

