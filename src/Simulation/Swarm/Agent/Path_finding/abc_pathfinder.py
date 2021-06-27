
##################################################################################################################
"""

"""

# Built-in/Generic Imports
from abc import ABC, abstractmethod

# Libs
import matplotlib.pyplot as plt

# Own modules
from src.Simulation.Swarm.Agent.Path_finding.Route import Route


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class Pathfinder(ABC):
    @staticmethod
    @abstractmethod
    def find_route_to_POI(self, environments_grids, swarm_grids, start_coordinates, POI, show_path=False):
        return

    @staticmethod
    @abstractmethod
    def find_route_to_coordinate(self, environments_grids, swarm_grids, start_coordinates, goal_coordinates, show_path=False):
        return

    @staticmethod
    @abstractmethod
    def find_route(environments_grids, swarm_grids, start_coordinates, goal_coordinates):
        return

    @staticmethod
    def show_route(grid, path):
        grid = grid.copy()

        # --> Set all path steps == 2
        for step in path:
            grid[step[1]][step[0]] = 2

        plt.imshow(grid)
        plt.colorbar()
        plt.show()
        return
