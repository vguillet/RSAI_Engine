
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

from RSAI_Engine.Simulation.Tools.Coordinate_system_converter import convert_coordinates

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class RSAI_agent:
    def __init__(self,
                 name: "Bot name",
                 sim_origin, sim_size,
                 start_world_pos: tuple = None,
                 start_sim_pos: tuple = None,
                 start_skills: dict = None,
                 start_states: dict = None,
                 start_equipment: dict = None,
                 start_inventory: dict = None):
        """
        Create RSAI agent objects to be used in RSAI simulations in the RSAI engine

        :param name: Name of agent
        :param start_pos: Tuple specified in sim coordinates
        :param start_skills: Starting skill set (Optional)
        :param start_states: Starting states (Optional)
        :param start_equipment: Starting equipment (Optional)
        :param start_inventory: Starting inventory (Optional)
        """

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        self.name = name

        # --> Setup position
        self.world_pos, self.simulation_pos = convert_coordinates(sim_origin, sim_size,
                                                                  start_world_pos, start_sim_pos)

        # --> Setup skills/inventory/interests/characteristics dicts
        self.skills = Skills(start_skills)
        self.states = States(start_states)
        self.equipment = Equipment(start_equipment)
        self.inventory = Inventory(start_inventory)
        
        # --> Setup tools
        self.pathfinder = Pathfinder()
        self.goal = "None"

        # --> Setup trackers
        self.goal_history = []
        self.pos_history = []

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
