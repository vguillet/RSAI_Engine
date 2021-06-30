
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random
import sys

# Libs
import matplotlib.pyplot as plt

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################
import numpy as np


def update_area(grid, simulation_pos, max_value=10, min_value=0, radius=3, plot=1):
    # --> Creating meshgrid
    x = np.linspace(0, radius * 2, radius * 2)
    y = np.linspace(0, radius * 2, radius * 2)

    xx, yy = np.meshgrid(x, y)

    # --> Apply cone function
    update_grid = -np.sqrt((xx - radius) ** 2 +
                           (yy - radius) ** 2)

    update_grid += np.amax(np.absolute(update_grid))

    # --> Apply max/min limits
    update_grid = update_grid/np.amax(update_grid) * (max_value-min_value) + min_value

    # --> Display update grid
    if plot == 1:
        # --> Make a 3D plot
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(xx, yy, grid, cmap='viridis', linewidth=0)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.show()

    # --> Apply to grid
    for i in range(radius * 2):
        for j in range(radius * 2):
            try:
                grid[simulation_pos[0] - radius + i, simulation_pos[1] - radius + j] = update_grid[i, j]
            except:
                pass


if __name__ == "__main__":
    update_area(grid=np.array([5, 5]),
                simulation_pos=[0, 0],
                max_value=10,
                min_value=5,
                radius=10)
