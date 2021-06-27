
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random

# Libs
import numpy as np
from faker import Faker

# Own modules
from src.Simulation.Swarm.Agent.RSAI_agent import Agent
from src.Simulation.Items.Item import Item
from src.Simulation.Tools.Throttle_tool import throttle

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Swarm:
    def __init__(self,
                 simulation_origin,
                 simulation_shape,
                 start_world_pos=(3216, 3219),
                 population_size=1):

        # --> Generate swarm population
        self.population = []
        self.generate_population(population_size=population_size,
                                 simulation_origin=simulation_origin,
                                 simulation_shape=simulation_shape,
                                 start_world_pos=start_world_pos)

        # --> Setup swarm grids
        self.grids_dict = {"Path pheromones": {}}

    def step(self, POI_dict, environments_grids, swarm_grids):
        for agent in self.population:
            if agent.goal is None:
                while agent.goal is None:
                    # --> Pick random goal
                    goal = random.choice(list(POI_dict.keys()))

                    # --> Set goal
                    agent.set_goal_POI(environments_grids=environments_grids,
                                       swarm_grids=swarm_grids,
                                       POI=POI_dict[goal])

                print(f"- {agent.name} - New Goal:", agent.goal)

            else:
                agent.move()

                if len(agent.simulation_path_to_goal) == 0:

                    agent.clear_goal()

    def reset_pheromones(self):
        for POI in self.grids_dict["Path pheromones"]:
            self.grids_dict["Path pheromones"][POI] = np.zeros(self.grids_dict["Path pheromones"][POI].shape)

    def update_path_pheromones(self, POI, route, energy_cost, q):
        if len(route) == 0:
            return

        pheromone_update = q / (len(route) + energy_cost)

        # --> Update pheromone  with a linear decay from POI to start
        for index, step in enumerate(route):
            self.grids_dict["Path pheromones"][POI][step[0], step[1]] += throttle(current_iteration=index,
                                                                                  nb_of_iterations=len(route),
                                                                                  max_value=pheromone_update,
                                                                                  min_value=0,
                                                                                  direction="up",
                                                                                  decay_function=1)
        return

    def evaporate_path_pheromones(self, evaporation_rate):
        # print("Evaporating")
        for POI in self.grids_dict["Path pheromones"]:
            for x in range(len(self.grids_dict["Path pheromones"][POI])):
                for y in range(len(self.grids_dict["Path pheromones"][POI][x])):
                    if self.grids_dict["Path pheromones"][POI][x, y] <= 1:
                        continue
                    else:
                        self.grids_dict["Path pheromones"][POI][x, y] = \
                            max(self.grids_dict["Path pheromones"][POI][x, y] * (1 - evaporation_rate), 1)

    def generate_population(self,
                            population_size,
                            simulation_origin,
                            simulation_shape,
                            start_world_pos):
        fake = Faker()

        # --> Add agents to list
        for _ in range(population_size):
            self.population.append(Agent(name=fake.name(),
                                         simulation_origin=simulation_origin,
                                         simulation_shape=simulation_shape,
                                         start_world_pos=start_world_pos))

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
