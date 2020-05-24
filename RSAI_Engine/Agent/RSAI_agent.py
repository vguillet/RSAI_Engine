
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs


# Own modules
from Settings.SETTINGS import SETTINGS

from RSAI_Engine.Agent.Tools.Skills_tools import Skills_tools
from RSAI_Engine.Agent.Tools.States_tools import States_tools
from RSAI_Engine.Agent.Tools.Equipment_tools import Equipment_tools

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
                 states: dict = None,
                 equipment: dict = None,
                 inventory: dict = None):

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        self.name = name
        self.pos = pos

        # --> Setup skills/inventory/interests/characteristics dicts
        self.skills, self.states, self.equipment, self.inventory = self.gen_dicts(skills,
                                                                                  states,
                                                                                  equipment,
                                                                                  inventory)
        
        # --> Setup tools
        self.pathfinder = Pathfinder()
        
    def gen_dicts(self,
                  skills: dict,
                  states: dict,
                  equipment: dict,
                  inventory: dict):

        # --> Setting up skills
        if skills is None:
            skills = Skills_tools().gen_skills_dict()
        else:
            pass

        # --> Setting up states
        if states is None:
            states = States_tools().gen_state_dict()
        else:
            pass

        # --> Setting up equipment
        if equipment is None:
            equipment = Equipment_tools()
        else:
            pass

        # --> Setting up inventory
        if inventory is None:
            inventory = Inventory_tools().gen_empty_inventory_dict()
        else:
            pass

        return skills, states, equipment, inventory

    def __str__(self):
        return self.name + " (Bot)"

    def __repr__(self):
        self.__repr__()
