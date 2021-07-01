
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import time
import random

# Libs
import cv2
import matplotlib.pyplot as plt

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
        self.obstacle_image_path = "src\Data\Assets\Environment\Obstacle_image_L.png"
        self.path_image_path = "src\Data\Assets\Environment\Path_image_L.png"

        self.simulation_origin = (2944, 3072)   # (2944, 3519) (3136, 3136), from bottom left

        # --> Create environment
        self.environment = Environment(world_image_path=self.world_image_path,
                                       obstacle_image_path=self.obstacle_image_path,
                                       path_image_path=self.path_image_path,
                                       simulation_origin=self.simulation_origin)

        # --> Create swarm
        self.swarm = Swarm(simulation_origin=self.environment.origin,
                           simulation_shape=self.environment.shape,
                           POI_dict=self.environment.POI_dict,
                           population_size=100,
                           verbose=0)

    def run_simulation(self):
        from src.Simulation.Tools.Views_generator import Views
        view_generator = Views(rsai_simulation=self)

        print("\n---------------------- Simulation started ----------------------")
        for agent in self.swarm.population:
            agent.goal = None

        counter = 0

        while True:
            self.swarm.step(POI_dict=self.environment.POI_dict,
                            environments_grids=self.environment.grids_dict)

            counter += 1

            if counter % 10000 == 0:
                print(f"- Step counts: {counter} completed")

            # if counter % 1000 == 0:
            #
            #     plt.imshow(view_generator.Pheromone_map_view, cmap='hot', interpolation='nearest')
            #     plt.show()

    def gui_run_simulation(self, progress_callback):
        print("\n---------------------- Simulation started ----------------------")
        for agent in self.swarm.population:
            agent.goal = None

        counter = 0

        while True:
            self.swarm.step(POI_dict=self.environment.POI_dict,
                            environments_grids=self.environment.grids_dict)

            counter += 1

            time.sleep(0.015)
            progress_callback.emit()

            if counter % 100 == 0:
                print(f"- Step counts: {counter} completed")
                # time.sleep(0.01)
                # progress_callback.emit()


if __name__ == "__main__":
    simulation = RSAI_simulation()
    simulation.run_simulation()
