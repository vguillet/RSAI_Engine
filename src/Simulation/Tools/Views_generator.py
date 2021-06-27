
##################################################################################################################
"""
This script contains the class used for generating the different views used by the RSAI GUI
"""

# Built-in/Generic Imports

# Libs
import numpy as np

# Own modules

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

        for agent in self.simulation.swarm.population:
            # --> Adding agent path to overview
            if agent.goal is not None:
                for step in agent.simulation_path_to_goal:
                    overview[step[1]][step[0]] = 5

            # --> Adding agent to overview
            overview[agent.simulation_pos[1]][agent.simulation_pos[0]] = 15

        # --> Adding POIs to overview
        overview += self.simulation.environment.grids_dict["POI"] * 10

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

        for agent in self.simulation.swarm.population:
            # --> Adding agent path
            if agent.goal is not None:
                for step in agent.simulation_path_to_goal:
                    agent_view[step[1]][step[0]] = 1

            # --> Add agent position
            agent_view[agent.simulation_pos[1]][agent.simulation_pos[0]] = 10

        return agent_view
