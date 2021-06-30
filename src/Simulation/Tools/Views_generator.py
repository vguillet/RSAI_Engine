
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

        overview[overview == 0] = int(2)
        overview[overview == 1] = int(0)
        overview[overview == 0] = int(1)

        # --> Adding paths to overview
        overview += self.simulation.environment.grids_dict["Path"] * 2

        for agent in self.simulation.swarm.population:
            # --> Adding agent path to overview
            if agent.goal is not None:
                for step in agent.simulation_route_to_goal:
                    overview[step[0]][step[1]] = 5

            # --> Adding agent to overview
            overview[agent.simulation_pos[0]][agent.simulation_pos[1]] = 15

        # --> Adding POIs to overview
        overview += self.simulation.environment.grids_dict["POI"] * 10

        return overview

    @property
    def agent_view(self):
        agent_view = np.zeros(self.simulation.environment.shape)

        for agent in self.simulation.swarm.population:
            # --> Adding agent path
            if agent.goal is not None:
                for step in agent.simulation_route_to_goal:
                    agent_view[step[0]][step[1]] = 3

            # --> Add agent position
            agent_view[agent.simulation_pos[0]][agent.simulation_pos[1]] = 10

        return agent_view

    @property
    def POI_view(self):
        poi_grid = np.zeros(self.simulation.environment.shape)

        # --> Add POIs location
        poi_grid += self.simulation.environment.grids_dict["POI"] * 10

        # --> Add agent position
        for agent in self.simulation.swarm.population:
            poi_grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 3

        return poi_grid

    @property
    def Appeal_map_view(self):
        appeal_grid = np.zeros(self.simulation.environment.shape)

        for POI in self.simulation.swarm.grids_dict["Path pheromone"].keys():
            # --> Add paths
            appeal_grid += self.simulation.environment.grids_dict["Path"] * 1

            # --> Add compass
            appeal_grid += self.simulation.environment.grids_dict["Compass"][POI][:self.simulation.environment.shape[0], :self.simulation.environment.shape[1]] * 1

            # --> Add POIs pheromone
            appeal_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI] * 1

        # --> Add agent position
        for agent in self.simulation.swarm.population:
            appeal_grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 10

        return appeal_grid

    @property
    def Pheromone_map_view(self):
        pheromone_grid = np.zeros(self.simulation.environment.shape)

        # --> Add POIs pheromone
        for POI in self.simulation.swarm.grids_dict["Path pheromone"].keys():
            pheromone_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI]

        # --> Add agent position
        for agent in self.simulation.swarm.population:
            pheromone_grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 10

        return pheromone_grid

    @property
    def obstacle_view(self):
        obstacle_grid = np.zeros(self.simulation.environment.shape)

        # --> Add paths
        obstacle_grid += self.simulation.environment.grids_dict["Obstacle"] * 3

        # --> Add agent position
        for agent in self.simulation.swarm.population:
            obstacle_grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 10

        return obstacle_grid

    @property
    def path_view(self):
        path_grid = np.zeros(self.simulation.environment.shape)

        # --> Add paths
        path_grid += self.simulation.environment.grids_dict["Path"] * 3

        # --> Add agent position
        for agent in self.simulation.swarm.population:
            path_grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 10

        return path_grid
