
################################################################################################################
"""
# TODO: Add reputation?
"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Simulation.Environment.POIs.Core.POI import POI

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Converter(POI):
    def __init__(self,
                 name,
                 ref,
                 simulation_origin,
                 simulation_size,
                 world_pos):
        # --> Initialising base class
        super().__init__(name=name,
                         ref=ref,
                         simulation_origin=simulation_origin,
                         simulation_size=simulation_size,
                         world_pos=world_pos)

        # ----- Setup reference properties
        self.type = "Converter"
