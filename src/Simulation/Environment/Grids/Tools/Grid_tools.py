
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


# def reduce_grid_scale(array, scale_factor):
#     vertical_chunk_count = int(array.shape[1] / scale_factor)
#     horizontal_chunk_count = int(array.shape[0] / scale_factor)
#
#     downscaled_array = np.ones((horizontal_chunk_count, vertical_chunk_count))
#
#     # -> Iterate through chunks
#     for chunk_x in range(horizontal_chunk_count):
#         for chunk_y in range(vertical_chunk_count):
#             obstacle_counter = 0
#
#             # -> Iterate inside tile
#             for row in range(scale_factor):
#                 for column in range(scale_factor):
#                     if array[(chunk_x * scale_factor) + row][(chunk_y * scale_factor) + column] == 1:
#                         obstacle_counter += 1
#                     else:
#                         pass
#
#             # -> Flag tile as obstacle if obstacle counter is too high
#             if obstacle_counter >= scale_factor / 2:
#                 downscaled_array[chunk_x][chunk_y] = 0
#
#     return downscaled_array

def reduce_grid_scale(array, scale_factor):
    vertical_chunk_count = int(array.shape[0] / scale_factor)
    horizontal_chunk_count = int(array.shape[1] / scale_factor)

    downscaled_array = np.zeros((vertical_chunk_count, horizontal_chunk_count))

    # --> Iterate through chunks
    for chunk_y in range(vertical_chunk_count):
        for chunk_x in range(horizontal_chunk_count):
            feature_counter = 0

            # --> Iterate through tiles in chunk
            for tile_y in range(scale_factor):
                for tile_x in range(scale_factor):
                    if array[(chunk_y * scale_factor) + tile_y][(chunk_x * scale_factor) + tile_x] == 1:
                        feature_counter += 1
                    else:
                        pass

            # -> Flag tile as obstacle if obstacle counter is too high
            if feature_counter >= 1:
                downscaled_array[chunk_y][chunk_x] = 1

    return downscaled_array
