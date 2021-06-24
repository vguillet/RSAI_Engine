
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
    def __init__(self, name, ref,
                 simulation_origin, simulation_size,
                 world_pos: tuple = None, sim_pos: tuple = None):
        # ----- Setup reference properties
        self.ref = ref
        self.type = ""
        self.name = name

        # --> Setup POI position
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin=simulation_origin,
                                                                  simulation_size=simulation_size,
                                                                  world_pos=world_pos,
                                                                  simulation_pos=sim_pos)

    def __str__(self):
        return f"{self.ref} - {self.name} ({self.type})"

    def __repr__(self):
        return self.__str__()
