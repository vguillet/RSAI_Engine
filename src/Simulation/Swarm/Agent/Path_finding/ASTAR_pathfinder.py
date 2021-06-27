
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import matplotlib.pyplot as plt

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Own modules
from src.Simulation.Swarm.Agent.Path_finding.abc_pathfinder import Pathfinder

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class ASTAR_pathfinder(Pathfinder):
    def find_route_to_POI(self,
                          environments_grids,
                          swarm_grids,
                          start_coordinates,
                          POI,
                          show_path=False):
        # --> Set pathfinding grid
        grid = Grid(matrix=environments_grids["Obstacle"])

        # --> Define starting point and goal
        start = grid.node(start_coordinates[0], start_coordinates[1])
        end = grid.node(POI.simulation_pos[0], POI.simulation_pos[1])

        # --> Set pathfinding algorithm
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        # --> Find path
        route, _ = finder.find_path(start, end, grid)

        if len(route) == 0:
            print(f"!!!! No path found to {POI.name} !!!!")
            return None

        # --> Show path on grid
        if show_path:
            self.show_route(environments_grids["Obstacle"], route)

        return route

    def find_route_to_coordinate(self, environments_grids, swarm_grids, start_coordinates, goal_coordinates, show_path=False):
        # --> Set pathfinding grid
        grid = Grid(matrix=environments_grids["Obstacle"])

        # --> Define starting point and goal
        start = grid.node(start_coordinates[0], start_coordinates[1])
        end = grid.node(goal_coordinates[0], goal_coordinates[1])

        # --> Set pathfinding algorithm
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        # --> Find path
        route, _ = finder.find_path(start, end, grid)

        # --> Show path on grid
        if show_path:
            self.show_route(environments_grids["Obstacle"], route)

        return route

    @staticmethod
    def find_route(environments_grids, swarm_grids, start_coordinates, goal_coordinates):
        pass
