
################################################################################################################
"""

"""

# Built-in/Generic Imports
import math

# Libs

# Own modules
from Settings.SETTINGS import SETTINGS

from RSAI_Engine.Agent.Tools.Skills import Skills
from RSAI_Engine.Agent.Tools.States import States
from RSAI_Engine.Agent.Tools.Equipment import Equipment

from RSAI_Engine.Agent.Tools.Inventory import Inventory
from RSAI_Engine.Agent.Tools.Pathfinder import Pathfinder

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Agent:
    def __init__(self,
                 name: "Bot name",
                 start_pos: tuple,
                 start_skills: dict = None,
                 start_states: dict = None,
                 start_equipment: dict = None,
                 start_inventory: dict = None):

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        self.name = name
        self.pos = start_pos

        # --> Setup skills/inventory/interests/characteristics dicts
        self.skills = Skills(start_skills)
        self.states = States(start_states)
        self.equipment = Equipment(start_equipment)
        self.inventory = Inventory(start_inventory)
        
        # --> Setup tools
        self.pathfinder = Pathfinder()

    def __str__(self):
        return self.name + " (Bot level " + str(self.combat_level) + ")"

    def __repr__(self):
        self.__repr__()

    @property
    def combat_level(self):
        """
        Bot combat level

        :return: combat_level
        """
        base = 0.25 * (self.skills()["Defence"]["Level"]
                       + self.skills()["Hitpoints"]["Level"]
                       + math.floor(self.skills()["Prayer"]["Level"]))

        melee = 0.325 * (self.skills()["Attack"]["Level"]
                        + self.skills()["Strength"]["Level"])

        range = 0.325 * (math.floor(self.skills()["Ranged"]["Level"]/2)
                         + self.skills()["Ranged"]["Level"])

        mage = 0.325 * (math.floor(self.skills()["Magic"]["Level"]/2)
                        + self.skills()["Magic"]["Level"])

        return math.floor(base + max([melee, range, mage]))
