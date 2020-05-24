
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs


# Own modules
from Settings.SETTINGS import SETTINGS

from RSAI_Engine.Agent.Tools.Traits_tools import Traits_tools
from RSAI_Engine.Agent.Tools.Characteristics_tools import Characteristics_tools
from RSAI_Engine.Tools.Inventory_tools import Inventory_tools

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Agent:
    def __init__(self,
                 name: "Bot name",
                 pos: tuple,
                 traits: dict = None,
                 characteristics: dict = None,
                 inventory: dict = None):

        # ----- Setup settings
        self.settings = SETTINGS()
        self.settings.agent_settings.gen_agent_settings()

        # ----- Setup reference properties
        self.name = name
        self.pos = pos

        # --> Setup traits/inventory/interests/characteristics dicts
        self.traits, self.characteristics, self.inventory = self.gen_dicts(traits,
                                                                           characteristics,
                                                                           inventory)

    def gen_dicts(self,
                  traits: dict,
                  characteristics: dict,
                  inventory: dict):

        # --> Setting up traits
        if traits is None:
            traits = Traits_tools().gen_traits_dict()
        else:
            pass

        # --> Setting up characteristics
        if characteristics is None:
            characteristics = Characteristics_tools().gen_agent_characteristics_dict()
        else:
            pass

        # --> Setting up inventory
        if inventory is None:
            inventory = Inventory_tools().gen_agent_inventory_dict()
        else:
            pass

        return traits, characteristics, inventory

    def __str__(self):
        return self.name + " (Bot)"

    def __repr__(self):
        self.__repr__()
