
################################################################################################################
"""

"""

# Built-in/Generic Imports


# Libs
import numpy as np
import matplotlib.pyplot as plt

# Own modules
from RSAI_Engine.Simulation.Environment.Tools.POI import POI


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


def gen_POI_grid(simulation_origin, simulation_size):

    # --> Listing POIs to be added (coordinate in Exploded map coordinates)
    POI_lst = [
               ["Varrock Grand Exchange", "Converter", (3164, 3467)],
               ["Varrock GM", "Converter", (3212, 3415)],
               ["Varrock Blacksmith", "Converter", (3225, 3435)],
               ["Lumbridge Foundry", "Converter", (3220, 3255)],

               ["Cows field", "Source", (3252, 3267)],
               ["Varrock SW mine", "Source", (3180, 3369)],
               # ["Varrock SE mine", "Source", (3178, 3369)],

               ["Lumbridge SW mine", "Source", (3150, 3152)],
               ["Lumbridge SE mine", "Source", (3227, 3150)],

               ["Varrock W Bank", "Sink", (3182, 3430)],
               ["Varrock E Bank", "Sink", (3254, 3426)],
               ]

    # --> Creating POI array
    POI_array = np.zeros(simulation_size)

    # --> Creating environment POI dictionary
    POI_dict = {}

    # --> Adding POIs to environment
    for i in range(len(POI_lst)):
        POI_dict[POI_lst[i][0]] = POI(POI_lst[i][0], POI_lst[i][1], simulation_origin, simulation_size,
                                      POI_lst[i][2])

        POI_array[POI_dict[POI_lst[i][0]].simulation_pos[1]][POI_dict[POI_lst[i][0]].simulation_pos[0]] = 1

    return POI_array, POI_dict


if __name__ == "__main__":
    grid, poi_dict = gen_POI_grid((384, 128), (3136, 3136))

    plt.imshow(grid)
    plt.colorbar()
    plt.show()
