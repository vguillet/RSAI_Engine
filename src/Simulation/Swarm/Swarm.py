
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
                 start_world_pos=[3216, 3219],
                 start_simulation_pos=None,
                 population_size=1):

        # --> Environment
        self.simulation_origin = simulation_origin
        self.simulation_shape = simulation_shape

        # --> Generate swarm population
        self.population = []
        self.generate_population(population_size=population_size,
                                 simulation_origin=simulation_origin,
                                 simulation_shape=simulation_shape,
                                 start_world_pos=start_world_pos,
                                 start_simulation_pos=start_simulation_pos)

        # --> Setup swarm grids
        self.grids_dict = {"Path pheromone": {}}

    def step(self, POI_dict, environments_grids):
        # TODO: Deal with unreachable goals
        for agent in self.population:
            if agent.goal is None:
                # --> Pick random goal
                goal = random.choice(list(POI_dict.keys()))

                if goal not in self.grids_dict["Path pheromone"].keys():
                    self.grids_dict["Path pheromone"][goal] = np.zeros(self.simulation_shape)

                # --> Set goal
                agent.set_goal_POI(POI=POI_dict[goal])

                print(f"- {agent.name} - New Goal:", agent.goal)

            else:
                agent.move(environments_grids=environments_grids,
                           swarm_grids=self.grids_dict,
                           pheromone_weight=0,
                           path_weight=0.02)

                # --> If arrived at goal
                if agent.simulation_pos == agent.goal.simulation_pos:
                    print("-> Route found:", len(agent.simulation_route_to_goal))
                    self.update_path_pheromones(POI=agent.goal,
                                                route=agent.simulation_route_to_goal,
                                                energy_cost=0,
                                                q=100)
                    agent.clear_goal()

                elif agent.age > 300:
                    agent.reset()

    def reset_pheromones(self):
        for POI in self.grids_dict["Path pheromone"].keys():
            self.grids_dict["Path pheromone"][POI] = np.zeros(self.simulation_shape)

    def update_path_pheromones(self, POI, route, energy_cost, q):
        # --> Reduce route
        route = route.reduced

        if len(route) == 0:
            return

        # --> Calculate max pheromone
        pheromone_update = q / (len(route) + energy_cost)

        # --> Update pheromone linearly increasing from start to POI
        for index, step in enumerate(route):
            self.grids_dict["Path pheromone"][POI][step[0], step[1]] += throttle(current_iteration=index,
                                                                                 nb_of_iterations=len(route),
                                                                                 max_value=pheromone_update,
                                                                                 min_value=0,
                                                                                 direction="up",
                                                                                 decay_function=1)
        return

    def evaporate_path_pheromones(self, evaporation_rate):
        # print("Evaporating")
        for POI in self.grids_dict["Path pheromone"]:
            for x in range(len(self.grids_dict["Path pheromone"][POI])):
                for y in range(len(self.grids_dict["Path pheromone"][POI][x])):
                    if self.grids_dict["Path pheromone"][POI][x, y] <= 1:
                        continue
                    else:
                        self.grids_dict["Path pheromone"][POI][x, y] = \
                            max(self.grids_dict["Path pheromone"][POI][x, y] * (1 - evaporation_rate), 1)

    def generate_population(self,
                            population_size,
                            simulation_origin,
                            simulation_shape,
                            start_world_pos,
                            start_simulation_pos):
        fake = Faker()

        # --> Add agents to list
        for _ in range(population_size):
            self.population.append(Agent(name=fake.name(),
                                         simulation_origin=simulation_origin,
                                         simulation_shape=simulation_shape,
                                         start_world_pos=start_world_pos,
                                         start_simulation_pos=start_simulation_pos))

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
