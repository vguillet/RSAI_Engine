
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import time

# Libs
import cv2
import numpy as np

# Own modules
from RSAI_Engine.Simulation.Environment.RSAI_environment import RSAI_environment
from RSAI_Engine.Simulation.Agent.RSAI_agent import RSAI_agent

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class RSAI_simulation:
    def __init__(self,
                 sim_origin: "World coordinates tuple" = (3136, 3136),
                 world_image_path="RSAI_Engine\Data\Environment\World_image.png",
                 obstacle_image_path="RSAI_Engine\Data\Environment\Obstacle_image.png"):

        # --> Record image paths
        self.world_image_path = world_image_path
        self.obstacle_image_path = obstacle_image_path

        # --> Load images
        self.world_image = cv2.imread(world_image_path, cv2.IMREAD_UNCHANGED)

        # --> Create environment
        self.environment = RSAI_environment(world_image=self.world_image,
                                            obstacle_image_path=self.obstacle_image_path,
                                            sim_origin=sim_origin)
        # --> Create agent
        self.agent = RSAI_agent("Bob",
                                self.environment.origin,
                                self.environment.shape,
                                start_world_pos=(3216, 3219))

        # --> Test goal
        self.agent.set_goal_POI(self.environment.grids_dict,
                                self.environment.POI_dict["Varrock GM"])

    def run_simulation(self, progress_callback):
        # --> Test goal
        self.agent.set_goal_POI(self.environment.grids_dict,
                                self.environment.POI_dict["Varrock GM"])

        step = 0
        while self.agent.goal is not None:
            step += 1
            self.agent.step()
            progress_callback.emit(step)
            time.sleep(0.02)

        self.agent.set_goal_POI(self.environment.grids_dict,
                                self.environment.POI_dict["Varrock GM"])

        print("Done")
        return
