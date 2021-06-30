
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random

# Libs
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt

# Own modules
from src.Simulation.Swarm.Agent.RSAI_agent import Agent
from src.Simulation.Items.Item import Item
from src.Simulation.Tools.Throttle_tool import throttle
from src.Simulation.Swarm.Agent.Path_finding.update_area import update_area

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Swarm:
    def __init__(self,
                 simulation_origin,
                 simulation_shape,
                 POI_dict,
                 population_size=1,
                 verbose=1):

        # --> Settings
        self.verbose = verbose

        # --> Environment
        self.simulation_origin = simulation_origin
        self.simulation_shape = simulation_shape

        # --> Generate swarm population
        self.population = []
        self.generate_population(population_size=population_size,
                                 simulation_origin=simulation_origin,
                                 simulation_shape=simulation_shape,
                                 POI_dict=POI_dict)

        # --> Setup swarm grids
        self.grids_dict = {"Path pheromone": {}}

    def step(self, POI_dict, environments_grids):
        # TODO: Deal with unreachable goals
        for agent in self.population:
            while agent.goal is None:
                # --> Pick random goal
                goal_name = random.choice(list(POI_dict.keys()))

                if goal_name not in self.grids_dict["Path pheromone"].keys():
                    self.grids_dict["Path pheromone"][goal_name] = np.zeros(self.simulation_shape)

                # --> Set goal
                agent.set_goal_POI(POI=POI_dict[goal_name])

                if self.verbose > 1:
                    print(f"- {agent.name} - New Goal:", agent.goal)

            # --> Take a step
            agent.move(environments_grids=environments_grids,
                       swarm_grids=self.grids_dict,
                       compass_weight=1,
                       path_weight=1.5,
                       pheromone_weight=1)

            # --> If arrived at goal
            if agent.simulation_pos == agent.goal.simulation_pos:
                print(f"-> Route to {agent.goal.name} found: {len(agent.simulation_route_to_goal)} steps")

                self.evaporate_path_pheromone(evaporation_rate=0.10,
                                              POI_name=agent.goal.name)

                self.update_path_pheromone(POI_name=agent.goal.name,
                                           route=agent.simulation_route_to_goal,
                                           energy_cost=0,
                                           q=1000)

                # # --> Visualise potential grid
                # potential_grid = environments_grids["Compass"][agent.goal.name][:self.simulation_shape[0], :self.simulation_shape[1]] * 1 \
                #                  + environments_grids["Path"] * 1 \
                #                  + self.grids_dict["Path pheromone"][agent.goal.name] * 1
                #
                # plt.imshow(potential_grid, cmap='hot', interpolation='nearest')
                # plt.show()

                # --> Clear agent goal
                agent.clear_goal()

            elif agent.age > 2500:
                agent.reset()

    def reset_pheromone(self):
        for POI in self.grids_dict["Path pheromone"].keys():
            self.grids_dict["Path pheromone"][POI] = np.zeros(self.simulation_shape)

    def update_path_pheromone(self, POI_name, route, energy_cost, q):
        # --> Reduce route
        route = route.reduced

        if len(route) == 0:
            return

        # --> Calculate max pheromone
        pheromone_update = q / (len(route) + energy_cost)
        pheromone_update = 1

        # --> Update pheromone linearly increasing from start to POI
        for index, step in enumerate(route):
            # > Calc pheromone update for step
            # step_pheromone_update = pheromone_update
            step_pheromone_update = throttle(current_iteration=index,
                                             nb_of_iterations=len(route),
                                             max_value=pheromone_update,
                                             min_value=pheromone_update/2,
                                             direction="up",
                                             decay_function=1)

            # > Apply step pheromone update to grid at step location
            update_area(grid=self.grids_dict["Path pheromone"][POI_name],
                        simulation_pos=[step[0], step[1]],
                        max_value=step_pheromone_update,
                        min_value=pheromone_update/3,
                        radius=3,
                        plot=0)

            # self.grids_dict["Path pheromone"][POI_name][step[0], step[1]] += step_pheromone_update

    def evaporate_path_pheromone(self, evaporation_rate, POI_name):
        for x in range(len(self.grids_dict["Path pheromone"][POI_name])):
            for y in range(len(self.grids_dict["Path pheromone"][POI_name][x])):
                if self.grids_dict["Path pheromone"][POI_name][x, y] <= 0:
                    continue
                else:
                    self.grids_dict["Path pheromone"][POI_name][x, y] -= evaporation_rate

    def generate_population(self,
                            population_size,
                            simulation_origin,
                            simulation_shape,
                            POI_dict):
        fake = Faker()

        # --> Add agents to list
        for _ in range(population_size):
            # > Select random starting point
            POI_key = random.choice(list(POI_dict.keys()))

            self.population.append(Agent(name=fake.name(),
                                         simulation_origin=simulation_origin,
                                         simulation_shape=simulation_shape,
                                         start_simulation_pos=POI_dict[POI_key].simulation_pos))

        # --> Equip some items
        equipment = [Item("Helm", "Med_helm", "Iron"),
                     Item("Chest", "Platebody", "Iron"),
                     Item("Legs", "Platelegs", "Iron"),
                     Item("Boots", "Boots", "Iron"),
                     Item("Gloves", "Gloves", "Iron"),
                     Item("Shield", "Kiteshield", "Black"),
                     Item("Weapon", "Scimitar", "Mithril")]

        for agent in self.population:
            for item in equipment:
                agent.inventory.add_item_to_inventory(item=item)
                agent.equipment.equip_item(inventory_dict=agent.inventory(),
                                           statistics_dict=agent.statistics(),
                                           item=item)

                agent.inventory.add_item_to_inventory(item=item)
