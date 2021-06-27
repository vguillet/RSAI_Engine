
################################################################################################################
"""

"""

# Built-in/Generic Imports


# Libs
import numpy as np
import matplotlib.pyplot as plt

# Own modules
from src.Simulation.Environment.POIs.Core.POI import POI
from src.Simulation.Environment.POIs.Shop import Shop


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


def gen_POI_grid(simulation_origin, simulation_shape):

    # --> Listing POIs to be added (coordinate in Exploded map coordinates)
    POI_lst = [
               ["Converter", "Varrock E Blacksmith", ["Ingot"], (3248, 3411)],
               ["Converter", "Varrock C Blacksmith", ["Ingot"], (3231, 3432)],
               ["Converter", "Varrock W Blacksmith", ["Ingot"], (3184, 3424)],
               ["Shop", "Varrock Grand Exchange", ["Weapon", "Helm", "Chest", "Legs", "Shield", "Boots", "Gloves", "Resource", "Ingot", "Food"], (3164, 3467)],
               ["Shop", "Varrock General shop", ["Weapon", "Helm", "Chest", "Legs", "Shield", "Boots", "Gloves", "Resource", "Ingot", "Food"], (3212, 3415)],
               ["Shop", "Varrock C Clothes shop", ["Boots", "Gloves"], (3209, 3415)],
               ["Shop", "Varrock E Clothes shop", ["Boots", "Gloves"], (3277, 3397)],
               ["Shop", "Varrock Sword shop", ["Weapon"], (3210, 3399)],
               ["Shop", "Varrock Archery shop", ["Weapon"], (3233, 3428)],
               ["Bank", "Varrock W Bank", [""], (3182, 3430)],
               ["Bank", "Varrock E Bank", [""], (3254, 3426)],
               ["Mine", "Varrock SW mine", [""], (3180, 3369)],
               ["Mine", "Varrock SE mine", [""], (3284, 3364)],

               ["Converter", "Edgeville Foundry", ["Ore"], (3112, 3498)],
               ["Shop", "Edgeville General shop", ["Weapon", "Helm", "Chest", "Legs", "Shield", "Boots", "Gloves", "Resource", "Ingot", "Food"], (3080, 3506)],
               ["Bank", "Edgeville Bank", [""], (3099, 3496)],

               ["Bank", "Cooks' Guild Bank", [""], (3143, 3342)],

               ["Shop", "Barbarian Village Helm shop", ["Helm"], (3085, 3412)],
               ["Converter", "Barbarian Village Blacksmith", ["Ingot"], (3085, 3412)],

               ["Converter", "Lumbridge Foundry", ["Ore"], (3220, 3255)],
               ["Mine", "Lumbridge SW mine", [""], (3150, 3152)],
               ["Mine", "Lumbridge SE mine", [""], (3227, 3150)],

               ["Source", "Cows field", [""], (3252, 3267)],

               ["Bank", "Draynor Bank", [""], (3093, 3247)],

               ["Shop", "Rimmington General shop", ["Weapon", "Helm", "Chest", "Legs", "Shield", "Boots", "Gloves", "Resource", "Ingot", "Food"], (2944, 3218)],
               ["Mine", "Rimmington NE Mine", [""], (2975, 3240)],

               ["Converter", "Falador Foundry", ["Ore"], (2978, 3373)],
               ["Shop", "Falador General shop", ["Weapon", "Helm", "Chest", "Legs", "Shield", "Boots", "Gloves", "Resource", "Ingot", "Food"], (2958, 3384)],
               ["Shop", "Falador Armoury", ["Chest", "Legs"], (2972, 3315)],
               ["Shop", "Falador Jeweller’s shop", ["Gems"], (2945, 3338)],
               ["Shop", "Falador Shield shop", ["Shield"], (2971, 3383)],
               ["Bank", "Falador W Bank", [""], (2946, 3374)],
               ["Bank", "Falador E Bank", [""], (3012, 3359)],

               ]

    # --> Creating POI array
    POI_array = np.zeros(simulation_shape)

    # --> Creating environment POI dictionary
    POI_dict = {}

    # --> Adding POIs to environment
    for i in range(len(POI_lst)):
        if POI_lst[i][0] == "Shop":
            POI_dict[POI_lst[i][1]] = Shop(name=POI_lst[i][1],
                                           ref=0,
                                           simulation_origin=simulation_origin,
                                           simulation_size=simulation_shape,
                                           world_pos=POI_lst[i][-1],
                                           traded_item_types=POI_lst[i][2])

        else:
            POI_dict[POI_lst[i][1]] = POI(name=POI_lst[i][1],
                                          ref=0,
                                          simulation_origin=simulation_origin,
                                          simulation_size=simulation_shape,
                                          world_pos=POI_lst[i][-1])

        POI_array[POI_dict[POI_lst[i][1]].simulation_pos[1]][POI_dict[POI_lst[i][1]].simulation_pos[0]] = 1

    return POI_array, POI_dict


if __name__ == "__main__":
    grid, poi_dict = gen_POI_grid((384, 128), (3136, 3136))

    plt.imshow(grid)
    plt.colorbar()
    plt.show()
