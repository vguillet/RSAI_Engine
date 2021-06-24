
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
               ["Varrock E Blacksmith", "Converter", (3248, 3411)],
               ["Varrock C Blacksmith", "Converter", (3231, 3432)],
               ["Varrock W Blacksmith", "Converter", (3184, 3424)],
               ["Varrock Grand Exchange", "Converter", (3164, 3467)],
               ["Varrock General shop", "Converter", (3212, 3415)],
               ["Varrock C Clothes shop", "Converter", (3209, 3415)],
               ["Varrock E Clothes shop", "Converter", (3277, 3397)],
               ["Varrock Sword shop", "Converter", (3209, 3399)],
               ["Varrock Archery shop", "Converter", (3233, 3428)],
               ["Varrock W Bank", "Sink", (3182, 3430)],
               ["Varrock E Bank", "Sink", (3254, 3426)],
               ["Varrock SW mine", "Source", (3180, 3369)],
               ["Varrock SE mine", "Source", (3284, 3364)],

               ["Edgeville Foundry", "Converter", (3112, 3498)],
               ["Edgeville General shop", "Converter", (3080, 3506)],
               ["Edgeville Bank", "Sink", (3099, 3496)],

               ["Cooks' Guild Bank", "Sink", (3143, 3342)],

               ["Barabarian Village Helm shop", "Converter", (3085, 3412)],
               ["Barabarian Village Blacksmith", "Converter", (3085, 3412)],

               ["Lumbridge Foundry", "Converter", (3220, 3255)],
               ["Lumbridge SW mine", "Source", (3150, 3152)],
               ["Lumbridge SE mine", "Source", (3227, 3150)],

               ["Cows field", "Source", (3252, 3267)],

               ["Draynor Bank", "Sink", (3093, 3247)],

               ["Rimmington General shop", "Converter", (2944, 3218)],
               ["Rimmington NE Mine", "Source", (2975, 3240)],

               ["Falador Foundry", "Converter", (2978, 3373)],
               ["Falador Armoury", "Converter", (2972, 3315)],
               ["Falador General shop", "Converter", (2958, 3384)],
               ["Falador Jeweller’s shop", "Converter", (2945, 3338)],
               ["Falador Shield shop", "Converter", (2971, 3383)],
               ["Falador W Bank", "Sink", (2946, 3374)],
               ["Falador E Bank", "Sink", (3012, 3359)],

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
