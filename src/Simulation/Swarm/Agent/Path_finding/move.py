
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random

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

from src.Simulation.Tools.Coordinate_system_converter import *

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


def move(self,
         environments_grids, swarm_grids,
         compass_weight=1,
         path_weight=1,
         pheromone_weight=1):
    if self.goal is None:
        print("!!!!! No goal specified !!!!!")

    else:
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
            # "a": {"step": [0, 0],
            #       "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1] - 1] * (1 - top_edge) * (1 - left_edge)},
            "b": {"step": [0, 1],
                  "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1]] * (1 - top_edge)},
            # "c": {"step": [0, 2],
            #       "sim": [self.simulation_pos[0] - 1, self.simulation_pos[1] + 1] * (1 - top_edge) * (1 - right_edge)},

            "d": {"step": [1, 0],
                  "sim": [self.simulation_pos[0], self.simulation_pos[1] - 1] * (1 - left_edge)},
            "e": {"step": [1, 1],
                  "sim": [self.simulation_pos[0], self.simulation_pos[1]]},
            "f": {"step": [1, 2],
                  "sim": [self.simulation_pos[0], self.simulation_pos[1] + 1] * (1 - right_edge)},

            # "g": {"step": [2, 0],
            #       "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1] - 1] * (1 - bottom_edge) * (1 - left_edge)},
            "h": {"step": [2, 1],
                  "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1]] * (1 - bottom_edge)},
            # "i": {"step": [2, 2],
            #       "sim": [self.simulation_pos[0] + 1, self.simulation_pos[1] + 1] * (1 - bottom_edge) * (1 - right_edge)}
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

                        # > Add small amount of pheromone from other path pheromone grids
                        for POI_name in swarm_grids[array_name].keys():
                            if POI_name != self.goal.name:
                                step_arrays[array_name][tuple(kernel_dict[array_position]["step"])] = \
                                    swarm_grids[array_name][POI_name][tuple(kernel_dict[array_position]["sim"])] * 0.5

        # --> Create possible step and possible step appeal lists
        possible_steps = []
        possible_steps_appeal = []

        # > Iterate through step array positions
        for array_position in kernel_dict.keys():
            if not np.isnan(step_arrays["Obstacle"][tuple(kernel_dict[array_position]["step"])]) and \
                    step_arrays["Obstacle"][tuple(kernel_dict[array_position]["step"])] != 1:
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

        # --> Use bubblesort to sort population and fitness_evaluation according to fitness_evaluation
        for _ in range(len(possible_steps_appeal)):
            for i in range(len(possible_steps_appeal) - 1):
                if possible_steps_appeal[i] < possible_steps_appeal[i + 1]:
                    # > Reorder population
                    possible_steps[i], possible_steps[i + 1] = possible_steps[i + 1], possible_steps[i]

                    # > Reorder fitness evaluation
                    possible_steps_appeal[i], possible_steps_appeal[i + 1] = possible_steps_appeal[i + 1], \
                                                                             possible_steps_appeal[i]

        # --> Replace
        appeal_weights = [3, 2, 2, 2, 1.5, 1.5, 1, 1, 1]

        for step_appeal in range(len(possible_steps_appeal)):
            possible_steps_appeal[step_appeal] = possible_steps_appeal[step_appeal] * appeal_weights[step_appeal]

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