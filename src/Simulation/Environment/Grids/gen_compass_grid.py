
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


def gen_compass_grid(simulation_shape, POI_dict):

    compass_grids_dict = {}

    for POI_name in POI_dict.keys():
        compass_grids_dict[POI_name] = np.zeros(simulation_shape)

    return compass_grids_dict
