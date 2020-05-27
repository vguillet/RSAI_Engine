
##################################################################################################################
"""
This script contains the class used for generating the different views used by the RSAI GUI
"""

# Built-in/Generic Imports

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


class Views:
    def __init__(self, rsai_simulation):
        self.simulation = rsai_simulation

    @property
    def overview(self):
        # --> Adding obstacles to overview
        overview = self.simulation.environment.grids_dict["Obstacle"].copy()

        # --> Adding paths to overview

        # --> Adding agent path to overview
        for step in self.simulation.agent.path_to_goal:
            overview[step[1]][step[0]] = 10

        # --> Adding POIs to overview
        overview += self.simulation.environment.grids_dict["POI"] * 15

        # --> Adding agent to overview
        overview[self.simulation.agent.simulation_pos[1]][self.simulation.agent.simulation_pos[0]] = 25

        return overview

    @property
    def obstacle_view(self):
        return self.simulation.environment.grids_dict["Obstacle"]

    @property
    def POI_view(self):
        return self.simulation.environment.grids_dict["POI"]

    @property
    def agent_view(self):
        agent_view = np.zeros(self.simulation.environment.shape)

        # --> Add agent position
        agent_view[self.simulation.agent.simulation_pos[1]][self.simulation.agent.simulation_pos[0]] = 10

        # --> Add agent path

        return agent_view