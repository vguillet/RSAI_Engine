
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import time
import random
from multiprocessing import Pool
from multiprocessing import cpu_count

# Libs
import cv2
import matplotlib.pyplot as plt

# Own modules
from src.Simulation.Environment.Environment import Environment
from src.Simulation.Swarm.Swarm import Swarm
from src.Simulation.Tools.Pickle_tools import *

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'


##################################################################################################################


def run(ticker, *args):
    try:
        # --> Record image paths
        world_image_path = "src\Data\Assets\Environment\World_image_L.png"
        obstacle_image_path = "src\Data\Assets\Environment\Obstacle_image_L.png"
        path_image_path = "src\Data\Assets\Environment\Path_image_L.png"

        simulation_origin = (2944, 3072)  # (2944, 3519) (3136, 3136), from bottom left

        # --> Create environment
        environment = Environment(world_image_path=world_image_path,
                                  obstacle_image_path=obstacle_image_path,
                                  path_image_path=path_image_path,
                                  simulation_origin=simulation_origin)

        # --> Create swarm
        swarm = Swarm(simulation_origin=environment.origin,
                      simulation_shape=environment.shape,
                      POI_dict=environment.POI_dict,
                      population_size=100,
                      grids_dict=None,
                      verbose=0)

        print("\n-----------> Starting sim thread\n")

        for _ in range(10000):
            swarm.step(POI_dict=environment.POI_dict,
                       environments_grids=environment.grids_dict)

        print("\n===========> Process completed\n")
        return

    except:
        pass


if __name__ == "__main__":
    process_count = 5  # Number of processes to create

    pool = Pool(process_count)
    pool.map(run, [0]*100)
