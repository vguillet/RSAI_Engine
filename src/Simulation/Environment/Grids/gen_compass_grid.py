
##################################################################################################################
"""

"""

# Built-in/Generic Imports
from math import sqrt

# Libs
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# Own modules


__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


def gen_compass_grid(simulation_shape, POI_dict, plot=1):
    # --> Create grids and multivariate normal
    compass_grids_dict = {}

    for POI_name in POI_dict.keys():
        # --> Getting max shape dimension
        max_dim = max(simulation_shape)

        # --> Creating meshgrid
        x = np.linspace(0, max_dim-1, max_dim)
        y = np.linspace(0, max_dim-1, max_dim)

        xx, yy = np.meshgrid(x, y)

        # --> Apply cone function
        grid = -np.sqrt((xx - POI_dict[POI_name].simulation_pos[1])**2 +
                        (yy - POI_dict[POI_name].simulation_pos[0])**2)

        # > Flip
        grid += np.amax(np.absolute(grid))

        # > Normalise (min=0, max=1)
        grid = grid / np.amax(grid)

        # --> Display compass grid
        if plot == 1:
            # --> Make a 3D plot
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot_surface(xx, yy, grid, cmap='viridis', linewidth=0)
            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
            plt.show()

        # --> Add to compass dictionary
        compass_grids_dict[POI_name] = grid

    return compass_grids_dict


if __name__ == "__main__":
    gen_compass_grid(simulation_shape=[100, 200],
                     POI_dict={"a": 0})
