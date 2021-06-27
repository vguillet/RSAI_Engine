
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import time
import random

# Libs
import cv2

# Own modules
from src.Simulation.Environment.Environment import Environment
from src.Simulation.Swarm.Swarm import Swarm

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class RSAI_simulation:
    def __init__(self):
        # --> Record image paths
        self.world_image_path = "src\Data\Assets\Environment\World_image_L.png"
        self.obstacle_image_path = "src\Data\Assets\Environment\Obstacle_image.png"
        self.path_image_path = "src\Data\Assets\Environment\Path_image.png"

        self.simulation_origin = (2944, 3072)   # (2944, 3519) (3136, 3136), from bottom left

        # --> Load images
        self.world_image = cv2.imread(self.world_image_path, cv2.IMREAD_UNCHANGED)

        # --> Create environment
        self.environment = Environment(world_image=self.world_image,
                                       obstacle_image_path=self.obstacle_image_path,
                                       path_image_path=self.path_image_path,
                                       simulation_origin=self.simulation_origin)

        # --> Create swarm
        self.swarm = Swarm(simulation_origin=self.environment.origin,
                           simulation_shape=self.environment.shape,
                           start_world_pos=(3216, 3219),
                           population_size=10)

    def run_simulation(self, progress_callback):
        print("---------------------- Simulation started ----------------------")
        for agent in self.swarm.population:
            agent.goal = None

        while True:
            self.swarm.step(POI_dict=self.environment.POI_dict,
                            environments_grids=self.environment.grids_dict,
                            swarm_grids=self.swarm.grids_dict)

            time.sleep(0.005)

            progress_callback.emit()


if __name__ == "__main__":
    RSAI_simulation()
    RSAI_simulation.run_simulation()
    print("Done")
