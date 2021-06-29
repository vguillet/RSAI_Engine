
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random
import sys

# Libs
from prettyprinter import pprint

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

        self.prev_simulation_pos = self.simulation_pos

        # --> Setup states dicts
        self.skills = Skills(start_skills_dict=start_skills)
        self.statistics = Statistics(start_statistics_dict=start_statistics)
        self.interests = Interests(start_interests_dict=start_interests)
        self.equipment = Equipment(start_equipment_dict=start_equipment)
        self.inventory = Inventory(start_inventory_dict=start_inventory)
        
        # --> Setup goal tracker
        self.goal = None
        self.simulation_route_to_goal = Route()
        self.simulation_route_to_goal.append(self.simulation_pos)

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
        print(POI.simulation_pos, self.simulation_pos)

        if POI.simulation_pos == self.simulation_pos:
            return

        if self.goal is not None:
            # --> Record previous goal
            self.clear_goal()

        # --> Set new goal
        self.goal = POI

    def move(self,
             environments_grids, swarm_grids,
             compass_weight=1,
             path_weight=1,
             pheromone_weight=1):

        # def calc_step_appeal(arrays, array_step_ref, weights):
        #     return arrays["Compass"][tuple(array_step_ref)] * weights[0] \
        #            + arrays["Path"][tuple(array_step_ref)] * weights[1] \
        #            + arrays["Path pheromone"][tuple(array_step_ref)] * weights[2]

        if self.goal is None:
            print("!!!!! No goal specified !!!!!")

        else:
            # self.prev_simulation_pos = self.simulation_pos
            #
            # possible_steps = []
            # possible_steps_appeal = []
            #
            # # --> Compile weight list
            # weights_lst = [compass_weight, path_weight, pheromone_weight]
            #
            # # --> Compile arrays dictionary
            #
            # #   a b c
            # #   d e f
            # #   g h i
            #
            # step_arrays = {
            #     "Obstacle": np.array(
            #         [[environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
            #           environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1]],
            #           environments_grids["Obstacle"][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Obstacle"][self.simulation_pos[0], self.simulation_pos[1] - 1],
            #           1,
            #           environments_grids["Obstacle"][self.simulation_pos[0], self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
            #           environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1]],
            #           environments_grids["Obstacle"][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]]),
            #
            #     "Compass": np.array(
            #         [[environments_grids["Compass"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
            #           environments_grids["Compass"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1]],
            #           environments_grids["Compass"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Compass"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] - 1],
            #           1,
            #           environments_grids["Compass"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Compass"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
            #           environments_grids["Compass"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1]],
            #           environments_grids["Compass"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]]),
            #
            #     "Path": np.array(
            #         [[environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
            #           environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1]],
            #           environments_grids["Path"][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Path"][self.simulation_pos[0], self.simulation_pos[1] - 1],
            #           1,
            #           environments_grids["Path"][self.simulation_pos[0], self.simulation_pos[1] + 1]],
            #
            #          [environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
            #           environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1]],
            #           environments_grids["Path"][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]]),
            #
            #     "Path pheromone": np.array(
            #         [[swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] - 1],
            #           swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1]],
            #           swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] - 1, self.simulation_pos[1] + 1]],
            #
            #          [swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] - 1],
            #           1,
            #           swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0], self.simulation_pos[1] + 1]],
            #
            #          [swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] - 1],
            #           swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1]],
            #           swarm_grids["Path pheromone"][self.goal.name][self.simulation_pos[0] + 1, self.simulation_pos[1] + 1]]])
            # }
            #
            # # --> a
            # if step_arrays["Obstacle"][0, 0] != 1 \
            #         and self.simulation_pos[0] - 1 >= 0 \
            #         and self.simulation_pos[1] - 1 >= 0:
            #
            #     possible_steps.append([self.simulation_pos[0] - 1, self.simulation_pos[1] - 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[0, 0],
            #                                                   weights=weights_lst))
            # # --> b
            # if step_arrays["Obstacle"][0, 1] != 1 \
            #         and self.simulation_pos[0] - 1 >= 0:
            #
            #     possible_steps.append([self.simulation_pos[0] - 1, self.simulation_pos[1]])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[0, 1],
            #                                                   weights=weights_lst))
            #
            # # --> c
            # if step_arrays["Obstacle"][0, 2] != 1 \
            #         and self.simulation_pos[0] - 1 >= 0 \
            #         and self.simulation_pos[1] + 1 < self.simulation_shape[1]:
            #
            #     possible_steps.append([self.simulation_pos[0] - 1, self.simulation_pos[1] + 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[0, 2],
            #                                                   weights=weights_lst))
            #
            # # =================================
            # # --> d
            # if step_arrays["Obstacle"][1, 0] != 1 \
            #         and self.simulation_pos[1] - 1 >= 0:
            #
            #     possible_steps.append([self.simulation_pos[0], self.simulation_pos[1] - 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[1, 0],
            #                                                   weights=weights_lst))
            # # --> f
            # if step_arrays["Obstacle"][1, 2] != 1 \
            #         and self.simulation_pos[1] + 1 < self.simulation_shape[1]:
            #
            #     possible_steps.append([self.simulation_pos[0], self.simulation_pos[1] + 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[1, 2],
            #                                                   weights=weights_lst))
            #
            # # =================================
            # # --> g
            # if step_arrays["Obstacle"][2, 0] != 1 \
            #         and self.simulation_pos[0] + 1 < self.simulation_shape[0] \
            #         and self.simulation_pos[1] - 1 >= 0:
            #
            #     possible_steps.append([self.simulation_pos[0] + 1, self.simulation_pos[1] - 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[2, 0],
            #                                                   weights=weights_lst))
            #
            # # --> h
            # if step_arrays["Obstacle"][2, 1] != 1 \
            #         and self.simulation_pos[0] + 1 < self.simulation_shape[0]:
            #
            #     possible_steps.append([self.simulation_pos[0] + 1, self.simulation_pos[1]])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[2, 1],
            #                                                   weights=weights_lst))
            #
            # # --> i
            # if step_arrays["Obstacle"][2, 2] != 1 \
            #         and self.simulation_pos[0] + 1 < self.simulation_shape[0] \
            #         and self.simulation_pos[1] + 1 < self.simulation_shape[1]:
            #
            #     possible_steps.append([self.simulation_pos[0] + 1, self.simulation_pos[1] + 1])
            #     possible_steps_appeal.append(calc_step_appeal(arrays=step_arrays,
            #                                                   array_step_ref=[2, 2],
            #                                                   weights=weights_lst))

            # --> Check for boundaries:
            top_edge = False
            left_edge = False
            bottom_edge = False
            right_edge = False

            if self.simulation_pos[0] - 1 < 0:
                top_edge = True

            if self.simulation_pos[1] - 1 < 0:
                left_edge = True

            if self.simulation_pos[0] + 1 >= self.simulation_shape[0]:
                bottom_edge = True

            if self.simulation_pos[1] + 1 >= self.simulation_shape[1]:
                right_edge = True

            # --> Compile arrays dictionary

            #   a b c
            #   d e f
            #   g h i

            kernel_dict = {
                "a": {"step": [0, 0],
                      "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1] - 1] * (1 - top_edge) * (1 - left_edge)},
                "b": {"step": [0, 1],
                      "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1]] * (1 - top_edge)},
                "c": {"step": [0, 2],
                      "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1] + 1] * (1 - top_edge) * (1 - right_edge)},

                "d": {"step": [1, 0],
                      "sim": [self.simulation_pos[0], self.simulation_pos[1] - 1] * (1 - left_edge)},
                "e": {"step": [1, 1],
                      "sim": [self.simulation_pos[0], self.simulation_pos[1]]},
                "f": {"step": [1, 2],
                      "sim": [self.simulation_pos[0], self.simulation_pos[1] + 1] * (1 - right_edge)},

                "g": {"step": [2, 0],
                      "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1] - 1] * (1 - bottom_edge) * (1 - left_edge)},
                "h": {"step": [2, 1],
                      "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1]] * (1 - bottom_edge)},
                "i": {"step": [2, 2],
                      "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1] + 1] * (1 - bottom_edge) * (1 - right_edge)}
                }

            # --> Create empty array dicts
            step_arrays = {
                "Obstacle": np.zeros((3, 3)),
                "Compass": np.zeros((3, 3)),
                "Path": np.zeros((3, 3)),
                "Path pheromone": np.zeros((3, 3))
                }

            # --> Fill with nan
            for array_name in step_arrays.keys():
                step_arrays[array_name][:, :] = np.NaN

            # --> Fill with corresponding values
            # > Iterate through step array positions
            for array_position in kernel_dict.keys():
                # If the length of the step array position coordinates is equal to zero
                if len(kernel_dict[array_position]["sim"]) != 0:
                    # > Iterate through arrays in the step arrays
                    for array_name in step_arrays.keys():

                        if array_name == "Obstacle" or array_name == "Path":
                            # > Set array position in array to the value of the sim grid
                            step_arrays[array_name][tuple(kernel_dict[array_position]["step"])] = \
                                environments_grids[array_name][tuple(kernel_dict[array_position]["sim"])]

                        elif array_name == "Compass":
                            # > Set array position in array to the value of the sim grid
                            step_arrays[array_name][tuple(kernel_dict[array_position]["step"])] = \
                                environments_grids[array_name][self.goal.name][tuple(kernel_dict[array_position]["sim"])]

                        elif array_name == "Path pheromone":
                            # > Set array position in array to the value of the sim grid
                            step_arrays[array_name][tuple(kernel_dict[array_position]["step"])] = \
                                swarm_grids[array_name][self.goal.name][tuple(kernel_dict[array_position]["sim"])]

            # --> Create possible step and possible step appeal lists
            possible_steps = []
            possible_steps_appeal = []

            # > Iterate through step array positions
            for array_position in kernel_dict.keys():
                if not np.isnan(step_arrays["Obstacle"][tuple(kernel_dict[array_position]["step"])]):
                    # > Record step
                    possible_steps.append(kernel_dict[array_position]["sim"])

                    # > Record step appeal
                    possible_steps_appeal.append(
                        step_arrays["Compass"][tuple(kernel_dict[array_position]["step"])] * compass_weight +
                        step_arrays["Path"][tuple(kernel_dict[array_position]["step"])] * path_weight +
                        step_arrays["Path pheromone"][tuple(kernel_dict[array_position]["step"])] * pheromone_weight)

            # --> Remove previous direction as option
            for step in possible_steps:
                if step == self.prev_simulation_pos:
                    # > Delete step appeal
                    del possible_steps_appeal[possible_steps.index(step)]

                    # > Delete step
                    possible_steps.remove(step)
                    break

            # --> Pick a step to take
            new_pos = random.choices(possible_steps,
                                     weights=possible_steps_appeal,
                                     k=1)[0]

            # new_pos = possible_steps[possible_steps_appeal.index(max(possible_steps_appeal))]

            self.simulation_pos = new_pos

            # --> Record route
            self.simulation_route_to_goal.append(new_pos)
            self.simulation_route_to_goal = self.simulation_route_to_goal.reduced

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
        self.simulation_route_to_goal.append(self.simulation_pos)

        # --> Reset age
        self.age = 0

    def reset(self):
        # --> Reset position trackers
        self.simulation_pos = self.simulation_route_to_goal[0]
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin=self.simulation_origin,
                                                                  simulation_shape=self.simulation_shape,
                                                                  world_pos=None,
                                                                  simulation_pos=self.simulation_pos)

        self.prev_simulation_pos = self.simulation_pos

        # --> Reset goal trackers
        self.goal = None

        # --> Reset route
        self.simulation_route_to_goal = Route()
        self.simulation_route_to_goal.append(self.simulation_pos)

        # --> Reset age
        self.age = 0

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
