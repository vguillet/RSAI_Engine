
################################################################################################################
"""

"""

# Built-in/Generic Imports
import sys

# Libs
import networkx as nx
import matplotlib.pyplot as plt
from faker import Faker

# Own modules


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


def convert_coordinates(simulation_origin, simulation_size,
                        world_pos: tuple = None,
                        simulation_pos: tuple = None):
    """
    Used to convert from both from world coordinates to sim coordinates and back.
    Specify known coordinates.

    :param simulation_origin: Simulation grid origin in world coordinates
    :param simulation_size: Size of simulation grid
    :param world_pos: Position in world coordinates (Optional)
    :param simulation_pos: Position in sim coordinates (Optional)
    :return:
    """

    if simulation_pos is None:
        translated_x_coordinate = world_pos[0] - simulation_origin[0]
        translated_y_coordinate = simulation_size[0] - (world_pos[1] - simulation_origin[1])

        return world_pos, (translated_x_coordinate, translated_y_coordinate)

    elif world_pos is None:
        translated_y_coordinate = (simulation_size[0] - simulation_pos[1]) + simulation_origin[1]
        translated_x_coordinate = simulation_pos[0] + simulation_origin[0]

        return (translated_x_coordinate, translated_y_coordinate), simulation_pos

    else:
        print("!!!!! POI pos need to be specified in at least one coordinate system")
        sys.exit()
