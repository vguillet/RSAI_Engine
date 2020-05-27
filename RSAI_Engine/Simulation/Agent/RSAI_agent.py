
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math
import random

# Libs

# Own modules
from RSAI_Engine.Settings.SETTINGS import SETTINGS

from RSAI_Engine.Simulation.Agent.Tools.Skills import Skills
from RSAI_Engine.Simulation.Agent.Tools.States import States
from RSAI_Engine.Simulation.Agent.Tools.Equipment import Equipment

from RSAI_Engine.Simulation.Agent.Tools.Inventory import Inventory
from RSAI_Engine.Simulation.Agent.Tools.Pathfinder import Pathfinder

from RSAI_Engine.Simulation.Tools.Coordinate_system_converter import *

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
                 start_states: dict = None,
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
        :param start_states: Starting states (Optional)
        :param start_equipment: Starting equipment (Optional)
        :param start_inventory: Starting inventory (Optional)
        """

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        # --> Agent
        self.name = name

        # --> Environment
        self.simulation_origin = simulation_origin
        self.simulation_shape = simulation_shape

        # --> Setup position
        self.world_pos, self.simulation_pos = convert_coordinates(simulation_origin, simulation_shape,
                                                                  start_world_pos, start_simulation_pos)

        # --> Setup skills/inventory/interests/characteristics dicts
        self.skills = Skills(start_skills)
        self.states = States(start_states)
        self.equipment = Equipment(start_equipment)
        self.inventory = Inventory(start_inventory)
        
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

    def __str__(self):
        return self.name + " (Bot level " + str(self.combat_level) + ")"

    def __repr__(self):
        self.__repr__()

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
                       + self.skills()["Hitpoints"]["Level"]
                       + math.floor(self.skills()["Prayer"]["Level"]))

        return math.floor(base + max([self.melee_level, self.range_level, self.mage_level]))

    def set_goal_POI(self, grids_dict, POI):
        if POI.simulation_pos == self.simulation_pos:
            print("!!!!! Already at goal!!!!")
            return

        if self.goal is not None:
            # --> Record previous goal
            self.goal_history.append(self.goal)

        # --> Set new goal
        self.goal = POI
        self.goal_type = "POI"

        # --> Find path for new goal
        self.simulation_path_to_goal = self.pathfinder.find_path_to_POI(grids_dict["Obstacle"],
                                                                        self.simulation_pos, POI)

        # --> Find equivalent world path
        self.world_path_to_goal, self.simulation_path_to_goal = \
            convert_path_coordinates(self.simulation_origin, self.simulation_shape,
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

    def step(self):
        if self.goal is None:
            print("!!!!! No goal specified !!!!!")

        else:
            # print(len(self.simulation_path_to_goal))
            # --> Record position
            self.simulation_pos_history.append(self.simulation_pos)

            # --> Step according to path
            self.simulation_pos = self.simulation_path_to_goal[0]
            self.world_pos, _ = convert_coordinates(self.simulation_origin, self.simulation_shape,
                                                    simulation_pos=self.simulation_pos)

            del self.simulation_path_to_goal[0]

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
