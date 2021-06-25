
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


def gen_obstacle_grid(world_image, obstacle_image_path=None):
    # --> Load image
    img_hsv = cv2.cvtColor(world_image, cv2.COLOR_BGR2HSV)

    # --> Filter image colors
    # -> Create Walls mask
    walls_low = np.asarray([0, 0, 255])
    walls_high = np.asarray([0, 0, 255])

    walls_mask = cv2.inRange(img_hsv, walls_low, walls_high)

    # -> Create Water mask
    water_low = np.asarray([110, 99, 193])
    water_high = np.asarray([110, 99, 193])

    water_mask = cv2.inRange(img_hsv, water_low, water_high)

    # -> Create Icons mask
    icons_low = np.asarray([120, 255, 1])
    icons_high = np.asarray([120, 255, 1])

    icons_mask = cv2.inRange(img_hsv, icons_low, icons_high)

    # -> Add masks
    mask = cv2.bitwise_or(walls_mask, water_mask)
    mask = cv2.bitwise_or(icons_mask, mask)

    # --> Save obstacle image if path provided
    if obstacle_image_path is not None:
        cv2.imwrite(obstacle_image_path, mask)

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


if __name__ == "__main__":
    world_obstacles_array = gen_obstacle_grid(world_image=cv2.imread("src\Data\Assets\Environment\World_image_L.png", cv2.IMREAD_UNCHANGED),
                                              obstacle_image_path="src\Data\Environment\Obstacle_image.png")

    plt.imshow(world_obstacles_array)
    plt.colorbar()
    plt.show()

