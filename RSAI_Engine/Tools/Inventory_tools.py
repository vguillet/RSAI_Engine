
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from RSAI_Engine.Agent.Tools.State_tools import State_tools
from RSAI_Engine.Agent.Tools.Skills_tools import Skills_tools
from RSAI_Engine.Tools.Item import Item

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Inventory_tools:
    @staticmethod
    def gen_empty_inventory_dict():
        inventory_dict = {"Money": 0,
                          "Resources": {},
                          "Items": {}
                          }

        return inventory_dict

    @staticmethod
    def equip_item(agent, item: str, item_quantity: int):
        """
        Equip item function used to add items that have an impact on agent skills
        (the agent skills are adjusted according to the item rating)
        """
        skills_tools = Skills_tools()
        state_tools = State_tools()

        item = Item(item)

        # --> Add item to agent inventory if not health potion
        if item.label.split()[-1] != "Health":
            # --> Add item to agent inventory
            if item.label in list(agent.inventory["Items"].keys()):
                agent.inventory["Items"][item.label] += item_quantity
            else:
                agent.inventory["Items"][item.label] = item_quantity

        # --> Adjust agent skills/state according to item
        # TODO: Adjust skills/state

        return

    @staticmethod
    def unequip_item(agent, item: str, item_quantity: int):
        skills_tools = Skills_tools()
        state_tools = State_tools()

        item = Item(item)

        # --> Remove item from agent inventory
        if agent.inventory["Items"][item.label] - item_quantity < 0:
            raise Exception("!!! Item quantity removed from inventory too large !!!")
        else:
            agent.inventory["Items"][item.label] -= item_quantity

        # --> Adjust agent skills/state according to item
        # TODO: Adjust skills/state

        return

    @staticmethod
    def gen_market_inventory_dict(traded_item_types: list):
        # --> Initiate empty inventory dict (with money)
        inventory_dict = {"Money": 100}

        # --> Add item type to inventory
        for item_type in traded_item_types:
            inventory_dict[item_type] = {}

        return inventory_dict

    @staticmethod
    def gen_mine_inventory_dict():
        # --> Initiate empty inventory dict (with resource item type)
        inventory_dict = {"Resources": {}}

        return inventory_dict

    @staticmethod
    def clean_inventory(inventory_dict):
        for item_type in inventory_dict:
            if isinstance(inventory_dict[item_type], dict):
                for item in inventory_dict[item_type].keys():
                    if inventory_dict[item_type][item] == 0:
                        del inventory_dict[item_type][item]

        return inventory_dict

    @staticmethod
    def get_gathered_quantity(agent, quantity):
        # --> Adjust gathered quantity to available cargo space
        if agent.skills["Cargo"] - agent.used_cargo < quantity:
            gathered_quantity = agent.skills["Cargo"] - agent.used_cargo
            if gathered_quantity < 0:
                print("No cargo space available")
                return 0
            else:
                return gathered_quantity
        else:
            return quantity
