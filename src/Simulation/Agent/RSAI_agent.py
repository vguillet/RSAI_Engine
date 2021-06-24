
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random

# Libs

# Own modules
from src.Settings.SETTINGS import SETTINGS

from src.Simulation.Agent.States.Skills import Skills
from src.Simulation.Agent.States.Statistics import Statistics
from src.Simulation.States.Equipment import Equipment
from src.Simulation.States.Inventory import Inventory
from src.Simulation.States.Interests import Interests

from src.Simulation.Agent.Tools.Pathfinder import Pathfinder

from src.Simulation.Tools.Coordinate_system_converter import *

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class RSAI_agent:
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
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin, simulation_shape,
                                                                  start_world_pos, start_simulation_pos)

        # --> Setup states dicts
        self.skills = Skills(start_skills_dict=start_skills)
        self.statistics = Statistics(start_statistics_dict=start_statistics)
        self.interests = Interests(start_interests_dict=start_interests)
        self.equipment = Equipment(start_equipment_dict=start_equipment)
        self.inventory = Inventory(start_inventory_dict=start_inventory)
        
        # --> Setup goal tracker
        self.goal = None
        self.goal_type = None
        self.total_path_len = None

        self.world_path_to_goal = None
        self.simulation_path_to_goal = None

        self.pathfinder = Pathfinder()

        # --> Setup memory
        self.goal_history = []
        self.simulation_pos_history = []

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

    def set_goal_POI(self, grids_dict, POI):
        if POI.simulation_pos == self.simulation_pos:
            print("!!!!! Already at goal!!!!")
            return

        if self.goal is not None:
            # --> Record previous goal
            self.goal_history.append(self.goal)

        # --> Find path for new goal
        self.simulation_path_to_goal = self.pathfinder.find_path_to_POI(obstacle_grid=grids_dict["Obstacle"],
                                                                        start_coordinates=self.simulation_pos,
                                                                        POI=POI)

        # --> Set new goal
        if self.simulation_path_to_goal is not None:
            self.goal = POI
            self.goal_type = "POI"

            # --> Find equivalent world path
            self.world_path_to_goal, self.simulation_path_to_goal = \
                convert_path_coordinates(simulation_origin=self.simulation_origin,
                                         simulation_size=self.simulation_shape,
                                         simulation_path=self.simulation_path_to_goal)

            # --> Set path length
            self.total_path_len = len(self.simulation_path_to_goal)

    def set_goal_coordinates(self, grids_dict, coordinates):
        if coordinates == self.simulation_pos:
            print("!!!!! Already at goal!!!!")
            return

        if self.goal is not None:
            # --> Record previous goal
            self.goal_history.append(self.goal)

        # --> Set new goal
        self.goal = coordinates
        self.goal_type = "Coordinates"

        # --> Find path for new goal
        self.simulation_path_to_goal = self.pathfinder.find_path_to_coordinate(grids_dict["Obstacle"],
                                                                               self.simulation_pos,
                                                                               coordinates)
        # --> Find equivalent world path
        self.world_path_to_goal, self.simulation_path_to_goal = \
            convert_path_coordinates(self.simulation_origin, self.simulation_shape,
                                     simulation_path=self.simulation_path_to_goal)

        # --> Set path length
        self.total_path_len = len(self.simulation_path_to_goal)

    def move(self):
        if self.goal is None:
            print("!!!!! No goal specified !!!!!")

        else:
            # print(len(self.simulation_path_to_goal))
            # --> Record position
            self.simulation_pos_history.append(self.simulation_pos)

            # --> Step according to path
            self.simulation_pos = self.simulation_path_to_goal[0]
            self.world_pos, _ = convert_coordinates(simulation_origin=self.simulation_origin,
                                                    simulation_size=self.simulation_shape,
                                                    simulation_pos=self.simulation_pos)

            # --> Remove step from path
            del self.simulation_path_to_goal[0]
            # --> Find equivalent world path
            self.world_path_to_goal, self.simulation_path_to_goal = \
                convert_path_coordinates(simulation_origin=self.simulation_origin,
                                         simulation_size=self.simulation_shape,
                                         simulation_path=self.simulation_path_to_goal)

            # --> If arrived at goal
            if len(self.simulation_path_to_goal) == 0:
                # --> Record previous goal
                self.goal_history.append(self.goal)

                # --> Reset goal trackers
                self.goal = None
                self.goal_type = None
                self.total_path_len = None

                self.world_path_to_goal = None
                self.simulation_path_to_goal = None

        return

    def check_final_state(self):
        # TODO: Implement check final state
        return False

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