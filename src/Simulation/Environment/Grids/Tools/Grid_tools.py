
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import numpy as np

# Own modules


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


def reduce_grid_scale(array, scale_factor):
    horizontal_tile_count = int(array.shape[0] / scale_factor)
    vertical_tile_count = int(array.shape[1] / scale_factor)

    downscaled_array = np.ones((horizontal_tile_count, vertical_tile_count))

    # -> Iterate through chucks
    for tile_x in range(horizontal_tile_count):
        for tile_y in range(vertical_tile_count):
            obstacle_counter = 0

            # -> Iterate inside tile
            for row in range(scale_factor):
                for column in range(scale_factor):
                    if array[(tile_x * scale_factor) + row][(tile_y * scale_factor) + column] == 1:
                        obstacle_counter += 1
                    else:
                        pass

            # -> Flag tile as obstacle if obstacle counter is too high
            if obstacle_counter >= scale_factor / 2:
                downscaled_array[tile_x][tile_y] = 0

    return downscaled_array