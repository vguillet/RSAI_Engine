
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


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class Pathfinder:
    def find_path_to_POI(self, obstacle_grid, start_coordinates, POI, show_path=False):
        # --> Set pathfinding grid
        grid = Grid(matrix=obstacle_grid)

        # --> Define starting point and goal
        start = grid.node(start_coordinates[0], start_coordinates[1])
        end = grid.node(POI.pos[0], POI.pos[1])

        # --> Find path
        path = self.find_path(start, end, grid)

        # --> Show path on grid
        if show_path:
            self.show_path(obstacle_grid, path)

        return path

    def find_path_to_coordinate(self, obstacle_grid, start_coordinates, goal_coordinates, show_path=False):
        # --> Set pathfinding grid
        grid = Grid(matrix=obstacle_grid)

        # --> Define starting point and goal
        start = grid.node(start_coordinates[0], start_coordinates[1])
        end = grid.node(goal_coordinates[0], goal_coordinates[1])

        # --> Find path
        path = self.find_path(start, end, grid)

        # --> Show path on grid
        if show_path:
            self.show_path(obstacle_grid, path)

        return path

    def find_path(self, start, end, grid):
        # --> Set pathfinding algorithm
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        # --> Find path
        path, _ = finder.find_path(start, end, grid)

        return path

    @staticmethod
    def show_path(grid, path):
        # --> Set all path steps == 2
        for step in path:
           grid[step[1]][step[0]] = 2

        plt.imshow(grid)
        plt.colorbar()
        plt.show()
        return
