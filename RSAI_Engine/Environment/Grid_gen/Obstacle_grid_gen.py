
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


def gen_obstacle_grid(map_image, obstacle_image_path=None):
    # TODO: Add loading grid directly if already exists
    # --> Load image
    img_hsv = cv2.cvtColor(map_image, cv2.COLOR_BGR2HSV)

    # --> Filter image colors
    # -> Create Walls/icon mask
    water_low = np.asarray([0, 0, 150])
    walls_high = np.asarray([150, 150, 255])

    walls_mask = cv2.inRange(img_hsv, water_low, walls_high)

    # -> Create Water mask
    water_low = np.asarray([50, 50, 50])
    water_high = np.asarray([118, 143, 193])

    water_mask = cv2.inRange(img_hsv, water_low, water_high)

    # -> Add masks
    mask = cv2.bitwise_or(walls_mask, water_mask)

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
            if obstacle_counter >= tile_size/2:
                world_obstacles_array[tile_x][tile_y] = 0

    np.save("world_array", world_obstacles_array)

    return world_obstacles_array


if __name__ == "__main__":
    world_obstacles_array = gen_obstacle_grid("RSAI_Engine\Data\Environment\Obstacle_image.png")
    print(world_obstacles_array.shape)

    # --> Test pathfinding
    grid = Grid(matrix=world_obstacles_array)

    start = grid.node(2, 300)
    end = grid.node(127, 0)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    print('Path length:', len(path))

    for step in path:
        world_obstacles_array[step[1]][step[0]] = 2

    plt.imshow(world_obstacles_array)
    plt.colorbar()
    plt.show()

