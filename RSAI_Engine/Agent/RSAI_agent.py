
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs


# Own modules
from Settings.SETTINGS import SETTINGS

from RSAI_Engine.Agent.Tools.Skills_tools import Skills_tools
from RSAI_Engine.Agent.Tools.State_tools import State_tools
from RSAI_Engine.Tools.Inventory_tools import Inventory_tools

from RSAI_Engine.Agent.Tools.Pathfinder import Pathfinder

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Agent:
    def __init__(self,
                 name: "Bot name",
                 pos: tuple,
                 skills: dict = None,
                 state: dict = None,
                 inventory: dict = None):

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        self.name = name
        self.pos = pos

        # --> Setup skills/inventory/interests/characteristics dicts
        self.skills, self.state, self.inventory = self.gen_dicts(skills,
                                                                 state,
                                                                 inventory)
        
        # --> Setup tools
        self.pathfinder = Pathfinder()
        
    def gen_dicts(self,
                  skills: dict,
                  state: dict,
                  inventory: dict):

        # --> Setting up skills
        if skills is None:
            skills = Skills_tools().gen_skills_dict()
        else:
            pass

        # --> Setting up characteristics
        if state is None:
            state = State_tools().gen_agent_state_dict()
        else:
            pass

        # --> Setting up inventory
        if inventory is None:
            inventory = Inventory_tools().gen_empty_inventory_dict()
        else:
            pass

        return skills, state, inventory

    def __str__(self):
        return self.name + " (Bot)"

    def __repr__(self):
        self.__repr__()
