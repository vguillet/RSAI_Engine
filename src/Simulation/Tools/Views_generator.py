
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

    def overview(self, POI_selection, agent_selection):
        overview = np.ones(self.simulation.environment.shape)

        # --> Add obstacles to overview
        overview -= self.simulation.environment.grids_dict["Obstacle"]

        # --> Add paths
        overview += self.simulation.environment.grids_dict["Path"]

        # --> Add POIs pheromone
        if POI_selection == "All":
            for POI in self.simulation.swarm.grids_dict["Path pheromone"].keys():
                overview += self.simulation.swarm.grids_dict["Path pheromone"][POI]

        else:
            for POI_name in self.simulation.swarm.grids_dict["Path pheromone"].keys():
                if POI_name == POI_selection:
                    overview += self.simulation.swarm.grids_dict["Path pheromone"][POI_name]
                    break

        # --> Add agents and POIs
        overview = self.add_agents_and_POIs(grid=overview,
                                            POI_selection=POI_selection,
                                            agent_selection=agent_selection)

        return overview

    def POI_view(self, POI_selection, agent_selection):
        poi_grid = np.ones(self.simulation.environment.shape)

        # --> Add obstacles to overview
        poi_grid -= self.simulation.environment.grids_dict["Obstacle"]

        # --> Add paths
        poi_grid += self.simulation.environment.grids_dict["Path"] * 0.5

        # --> Add agents and POIs
        poi_grid = self.add_agents_and_POIs(grid=poi_grid,
                                            POI_selection=POI_selection,
                                            agent_selection=agent_selection,
                                            agent_factor=0.5)

        return poi_grid

    def appeal_map_view(self, POI_selection, agent_selection):
        appeal_grid = np.ones(self.simulation.environment.shape)

        # --> Add obstacles to overview
        appeal_grid -= self.simulation.environment.grids_dict["Obstacle"]

        # --> Add paths
        appeal_grid += self.simulation.environment.grids_dict["Path"] * 1.5

        if POI_selection == "All":
            for POI_name in self.simulation.swarm.grids_dict["Path pheromone"].keys():
                # > Add compass
                appeal_grid += self.simulation.environment.grids_dict["Compass"][POI_name][:self.simulation.environment.shape[0], :self.simulation.environment.shape[1]] * 1

                # > Add pheromone
                appeal_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI_name] * 2

        else:
            for POI_name in self.simulation.environment.POI_dict.keys():
                if POI_name == POI_selection:
                    # > Add compass
                    appeal_grid += self.simulation.environment.grids_dict["Compass"][POI_name][:self.simulation.environment.shape[0], :self.simulation.environment.shape[1]] * 1

                    # > Add pheromone
                    appeal_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI_name] * 2

                    break

        # --> Add agents and POIs
        appeal_grid = self.add_agents_and_POIs(grid=appeal_grid,
                                               POI_selection=POI_selection,
                                               agent_selection=agent_selection,
                                               agent_path_factor=0.5)

        return appeal_grid

    def pheromone_map_view(self, POI_selection, agent_selection):
        pheromone_grid = np.zeros(self.simulation.environment.shape)

        # --> Add paths
        pheromone_grid += self.simulation.environment.grids_dict["Path"] * 1.5

        if POI_selection == "All":
            for POI_name in self.simulation.swarm.grids_dict["Path pheromone"].keys():
                # > Add pheromone
                pheromone_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI_name] * 2.5

        else:
            for POI_name in self.simulation.environment.POI_dict.keys():
                if POI_name == POI_selection:
                    # > Add pheromone
                    pheromone_grid += self.simulation.swarm.grids_dict["Path pheromone"][POI_name] * 2.5

                    break

        # --> Add agents and POIs
        pheromone_grid = self.add_agents_and_POIs(grid=pheromone_grid,
                                                  POI_selection=POI_selection,
                                                  agent_selection=agent_selection)

        return pheromone_grid

    def obstacle_view(self, POI_selection, agent_selection):
        obstacle_grid = np.zeros(self.simulation.environment.shape)

        # --> Add paths
        obstacle_grid += self.simulation.environment.grids_dict["Obstacle"] * 3

        # --> Add agents and POIs
        obstacle_grid = self.add_agents_and_POIs(grid=obstacle_grid,
                                                 POI_selection=POI_selection,
                                                 agent_selection=agent_selection)

        return obstacle_grid

    def path_view(self, POI_selection, agent_selection):
        path_grid = np.ones(self.simulation.environment.shape)

        # --> Add obstacles to overview
        path_grid -= self.simulation.environment.grids_dict["Obstacle"]

        # --> Add paths
        path_grid += self.simulation.environment.grids_dict["Path"] * 3

        # --> Add agents and POIs
        path_grid = self.add_agents_and_POIs(grid=path_grid,
                                             POI_selection=POI_selection,
                                             agent_selection=agent_selection)

        return path_grid

    def add_agents_and_POIs(self, grid, POI_selection, agent_selection,
                            agent_factor=1.0, agent_path_factor=1.0):
        # --> Add agent
        if agent_selection == "All":
            for agent in self.simulation.swarm.population:
                # --> Adding agent path
                if agent.goal is not None:
                    for step in agent.simulation_route_to_goal:
                        grid[step[0]][step[1]] = 3.5 * agent_path_factor

                # --> Add agent position
                grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 9 * agent_factor

        else:
            for agent in self.simulation.swarm.population:
                if agent.name == agent_selection:
                    # --> Adding agent path
                    if agent.goal is not None:
                        for step in agent.simulation_route_to_goal:
                            grid[step[0]][step[1]] = 3.5 * agent_path_factor

                    # --> Add agent position
                    grid[agent.simulation_pos[0]][agent.simulation_pos[1]] = 9

                    break

        # --> Add POIs location
        if POI_selection == "All":
            grid += self.simulation.environment.grids_dict["POI"] * 10

        else:
            for POI_name in self.simulation.environment.POI_dict.keys():
                if POI_name == POI_selection:
                    # --> Add agent position
                    grid[self.simulation.environment.POI_dict[POI_name].simulation_pos[0]][self.simulation.environment.POI_dict[POI_name].simulation_pos[1]] = 10
                    break

        return grid
