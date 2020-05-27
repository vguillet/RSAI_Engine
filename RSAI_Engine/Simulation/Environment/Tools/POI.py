
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
from RSAI_Engine.Simulation.Tools.Coordinate_system_converter import convert_coordinates


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class POI:
    def __init__(self, name, label,
                 simulation_origin, simulation_size,
                 world_pos: tuple = None, sim_pos: tuple = None, ef_dict=None):
        # ----- Setup reference properties
        self.name = name
        self.type = "POI"
        self.label = label

        # --> Setup POI position
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin, simulation_size,
                                                                  world_pos, sim_pos)

        # ----- Setup POI content
        # --> Generate ef dictionary
        if ef_dict is None:
            # TODO: Add ef_dict
            pass

        # --> Use provided ef dictionary
        else:
            self.ef_dict = ef_dict

    def __str__(self):
        return self.name + self.label + " (POI) " + "\n"

    def __repr__(self):
        return self.__str__()
