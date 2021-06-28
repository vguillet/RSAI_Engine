
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random
import sys

# Libs

# Own modules
import numpy as np

from src.Settings.SETTINGS import SETTINGS

from src.Simulation.Swarm.Agent.States.Skills import Skills
from src.Simulation.Swarm.Agent.States.Statistics import Statistics
from src.Simulation.States.Equipment import Equipment
from src.Simulation.States.Inventory import Inventory
from src.Simulation.States.Interests import Interests

from src.Simulation.Swarm.Agent.Path_finding.Route import Route

from src.Simulation.Swarm.Agent.Path_finding.ASTAR_pathfinder import ASTAR_pathfinder
from src.Simulation.Swarm.Agent.Path_finding.ACO_pathfinder import AOC_pathfinder

from src.Simulation.Tools.Coordinate_system_converter import *

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Agent:
    def __init__(self,
                 name: "Bot name",
                 simulation_origin, simulation_shape,
                 start_world_pos: tuple = None,
                 start_simulation_pos: tuple = None,
                 start_skills: dict = None,
                 start_statistics: dict = None,
                 start_interests: dict = None,
                 start_equipment: dict = None,
                 start_inventory: dict = None):
        """
        Create RSAI agent objects to be used in RSAI simulations in the RSAI engine

        :param name: Name of agent
        :param simulation_origin: Simulation origin
        :param simulation_shape: Simulation shape
        :param start_world_pos: Tuple specified in world coordinates
        :param start_simulation_pos: Tuple specified in simulation coordinates
        :param start_skills: Starting skill set (Optional)
        :param start_statistics: Starting states (Optional)
        :param start_equipment: Starting equipment (Optional)
        :param start_inventory: Starting inventory (Optional)
        """

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        # --> Agent
        self.name = name
        self.age = 1

        # --> Environment
        self.simulation_origin = simulation_origin
        self.simulation_shape = simulation_shape

        # --> Setup position
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin=simulation_origin,
                                                                  simulation_shape=simulation_shape,
                                                                  world_pos=start_world_pos,
                                                                  simulation_pos=start_simulation_pos)

        # --> Setup states dicts
        self.skills = Skills(start_skills_dict=start_skills)
        self.statistics = Statistics(start_statistics_dict=start_statistics)
        self.interests = Interests(start_interests_dict=start_interests)
        self.equipment = Equipment(start_equipment_dict=start_equipment)
        self.inventory = Inventory(start_inventory_dict=start_inventory)
        
        # --> Setup goal tracker
        self.goal = None

        self.simulation_route_to_goal = Route()

        # --> Setup memory
        self.goal_history = []
        self.simulation_route_history = []

        print("- Agent initiated:", self)

    def __str__(self):
        return self.name + " (RSAI bot level " + str(self.combat_level) + ")"

    def __repr__(self):
        return self.__str__()

    @property
    def melee_level(self):
        return 0.325 * (self.skills()["Attack"]["Level"] + self.skills()["Strength"]["Level"])

    @property
    def range_level(self):
        return 0.325 * (math.floor(self.skills()["Ranged"]["Level"]/2) + self.skills()["Ranged"]["Level"])

    @property
    def mage_level(self):
        return 0.325 * (math.floor(self.skills()["Magic"]["Level"]/2) + self.skills()["Magic"]["Level"])

    @property
    def combat_level(self):
        """
        Bot combat level

        :return: combat_level
        """
        base = 0.25 * (self.skills()["Defence"]["Level"]
                       + self.skills()["Hitpoint"]["Level"]
                       + math.floor(self.skills()["Prayer"]["Level"]))

        return math.floor(base + max([self.melee_level, self.range_level, self.mage_level]))

    def set_goal_POI(self, POI):
        if POI.simulation_pos == self.simulation_pos:
            print("!!!!! Already at goal!!!!")
            return

        if self.goal is not None:
            # --> Record previous goal
            self.clear_goal()

        # --> Set new goal
        self.goal = POI

    def move(self, environments_grids, swarm_grids, pheromone_weight=1, path_weight=1):
        if self.goal is None:
            print("!!!!! No goal specified !!!!!")

        else:
            possible_steps = []

            #   a b c
            #   d e f
            #   g h i

            # =================================
            step_obstacle_array = \
                np.array([[environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
                           environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1]],
                           environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],

                          [environments_grids["Obstacle"][self.simulation_pos[0], self.simulation_pos[1] - 1],
                           1,
                           environments_grids["Obstacle"][self.simulation_pos[0], self.simulation_pos[1] + 1]],

                          [environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
                           environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1]],
                           environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]])

            step_path_array = \
                np.array([[environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
                           environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1]],
                           environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],

                          [environments_grids["Path"][self.simulation_pos[0], self.simulation_pos[1] - 1],
                           1,
                           environments_grids["Path"][self.simulation_pos[0], self.simulation_pos[1] + 1]],

                          [environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
                           environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1]],
                           environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]])

            step_pheromone_array = np.array(
                [[swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
                  swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1]],
                  swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],

                 [swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] - 1],
                  1,
                  swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] + 1]],

                 [swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
                  swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1]],
                  swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]])

            # --> a
            if step_obstacle_array[0, 0] != 1 and self.simulation_pos[0] - 1 >= 0 \
                    and self.simulation_pos[1] - 1 >= 0:
                possible_steps.append([[self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
                                      step_path_array[0, 0] * path_weight + step_pheromone_array[0, 0] * pheromone_weight])

            # --> b
            if step_obstacle_array[0, 1] != 1 \
                    and self.simulation_pos[0] - 1 >= 0:
                possible_steps.append([[self.simulation_pos[0] - 1, self.simulation_pos[1]],
                                      step_path_array[0, 1] * path_weight + step_pheromone_array[0, 1] * pheromone_weight])

            # --> c
            if step_obstacle_array[0, 2] != 1 \
                    and self.simulation_pos[0] - 1 >= 0 \
                    and self.simulation_pos[1] + 1 <= self.simulation_shape[1]:
                possible_steps.append([[self.simulation_pos[0] - 1, self.simulation_pos[1] + 1],
                                      step_path_array[0, 2] * path_weight + step_pheromone_array[0, 2] * pheromone_weight])

            # =================================
            # --> d
            if step_obstacle_array[1, 0] != 1 \
                    and self.simulation_pos[1] - 1 >= 0:
                possible_steps.append([[self.simulation_pos[0], self.simulation_pos[1] - 1],
                                      step_path_array[1, 0] * path_weight + step_pheromone_array[1, 0] * pheromone_weight])

            # --> f
            if step_obstacle_array[1, 2] != 1 \
                    and self.simulation_pos[1] + 1 <= self.simulation_shape[1]:
                possible_steps.append([[self.simulation_pos[0], self.simulation_pos[1] + 1],
                                      step_path_array[1, 2] * path_weight + step_pheromone_array[1, 2] * pheromone_weight])

            # =================================
            # --> g
            if step_obstacle_array[2, 0] != 1 \
                    and self.simulation_pos[0] + 1 <= self.simulation_shape[0] \
                    and self.simulation_pos[1] - 1 >= 0:
                possible_steps.append([[self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
                                      step_path_array[2, 0] * path_weight + step_pheromone_array[2, 0] * pheromone_weight])

            # --> h
            if step_obstacle_array[2, 1] != 1 \
                    and self.simulation_pos[0] + 1 <= self.simulation_shape[0]:
                possible_steps.append([[self.simulation_pos[0] + 1, self.simulation_pos[1]],
                                      step_path_array[2, 1] * path_weight + step_pheromone_array[2, 1] * pheromone_weight])

            # --> i
            if step_obstacle_array[2, 2] != 1 \
                    and self.simulation_pos[0] + 1 <= self.simulation_shape[0] \
                    and self.simulation_pos[1] + 1 <= self.simulation_shape[1]:
                possible_steps.append([[self.simulation_pos[0] + 1, self.simulation_pos[1] + 1],
                                      step_path_array[2, 2] * path_weight + step_pheromone_array[2, 2] * pheromone_weight])

            # --> Remove previous direction as option
            if len(self.simulation_route_to_goal) > 1:
                possible_steps.remove(self.simulation_route_to_goal[-1])

            total_surrounding_appeal = 0

            for step in possible_steps:
                total_surrounding_appeal += step[-1]

            # new_pos = possible_steps[0]
            # print(step_obstacle_array)
            # print(step_path_array)
            # print(step_pheromone_array)
            # print("\n")

            # --> Randomize the order in which possible steps will be evaluated
            random.shuffle(possible_steps)

            # --> Pick a step to take
            random_number = random.random()

            new_pos = None

            for step in possible_steps:
                # --> Compute probability this step should be taken

                if total_surrounding_appeal != 0:
                    relative_appeal = step[-1] / total_surrounding_appeal
                else:
                    relative_appeal = step[-1]

                # --> Take this step if the probability roll picked this step
                if relative_appeal >= random_number:
                    new_pos = step
                    break

                else:
                    random_number -= relative_appeal

            max_step = possible_steps[0]
            for step in possible_steps:
                if step[-1] > max_step[-1]:
                    max_step = step

            new_pos = max_step

            if new_pos is None:
                new_pos = random.choice(possible_steps)

            # self.simulation_route_to_goal.append(new_pos[0])
            self.simulation_pos = new_pos[0]

            # --> Increase age
            self.age += 1

    def clear_goal(self):
        # --> Record previous goal
        self.goal_history.append(self.goal)
        self.simulation_route_history.append(self.simulation_route_to_goal)

        # --> Reset goal trackers
        self.goal = None

        # --> Rest route
        self.simulation_route_to_goal = Route()

    def reset(self):
        # TODO: Implement reset agent/sim
        return

    def hit(self, target):
        """
        Calculate damage done when attempting to hit

        :param target: target to hit
        """

        # --> Roll D2 to check if hit
        if bool(random.getrandbits(1)):
            # --> Roll a D6 to check damage:
            damage = random.randint(0, 6) * self.melee_level
        else:
            damage = 0

        # TODO: Do damage to target, account for target defence
