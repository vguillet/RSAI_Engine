
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import cv2
import numpy as np
import matplotlib.pyplot as plt

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Own modules


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


def gen_path_grid(world_image, path_image_path=None):
    # --> Load image
    img_hsv = cv2.cvtColor(world_image, cv2.COLOR_BGR2HSV)

    # --> Filter image colors
    # -> Create stone_road mask
    stone_road_low = np.asarray([0, 0, 0])
    stone_road_high = np.asarray([360, 50, 100])

    stone_road_mask = cv2.inRange(img_hsv, stone_road_low, stone_road_high)

    # -> Create dirt_road mask
    dirt_road_low = np.asarray([0, 0, 0])
    dirt_road_high = np.asarray([180, 21, 50])

    dirt_road_mask = cv2.inRange(img_hsv, dirt_road_low, dirt_road_high)

    # -> Add masks
    mask = cv2.bitwise_or(stone_road_mask, dirt_road_mask)

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
    tile_size = 4
    horizontal_tile_count = int(mask.shape[0] / tile_size)
    vertical_tile_count = int(mask.shape[1] / tile_size)

    world_obstacles_array = np.ones((horizontal_tile_count, vertical_tile_count))

    # -> Iterate through chucks
    for tile_x in range(horizontal_tile_count):
        for tile_y in range(vertical_tile_count):
            obstacle_counter = 0

            # -> Iterate inside tile
            for row in range(tile_size):
                for column in range(tile_size):
                    if mask[(tile_x * tile_size) + row][(tile_y * tile_size) + column] == 1:
                        obstacle_counter += 1
                    else:
                        pass
            
            # -> Flag tile as obstacle if obstacle counter is too high
            if obstacle_counter >= tile_size / 2:
                world_obstacles_array[tile_x][tile_y] = 0

    # np.save("world_array", world_obstacles_array)

    return world_obstacles_array

