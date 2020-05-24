
################################################################################################################
"""

"""

# Built-in/Generic Imports


# Libs
import numpy as np
import matplotlib.pyplot as plt

# Own modules
from RSAI_Engine.Environment.Tools.POI import POI


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


def gen_POI_grid(grid_size, origin):

    # --> Listing POIs to be added (coordinate in Exploded map coordinates)
    POI_lst = [["Cows field", "Source", (3252, 3267)],
               ["Varrock GM", "Converter", (3213, 3415)],
               ["Varrock SW mine", "Source", (3178, 3369)],
               # ["Varrock SE mine", "Source", (3178, 3369)],
               ]

    # --> Creating POI array
    POI_array = np.zeros(grid_size)

    # --> Creating environment POI dictionary
    POI_dict = {}

    # --> Adding POIs to environment
    for i in range(len(POI_lst)):
        print(POI_lst[i][0])
        translated_y_coordinate = grid_size[0] - (POI_lst[i][2][1] - origin[1])
        translated_x_coordinate = POI_lst[i][2][0] - origin[0]

        POI_dict[POI_lst[i][0]] = POI(POI_lst[i][0], POI_lst[i][1], (translated_x_coordinate, translated_y_coordinate))
        POI_array[translated_y_coordinate][translated_x_coordinate] = 1

    print("-- RSAI environment layout generated successfully --")
    return POI_array, POI_dict


if __name__ == "__main__":
    grid, poi_dict = gen_POI_grid((384, 128), (3136, 3136))

    plt.imshow(grid)
    plt.colorbar()
    plt.show()
