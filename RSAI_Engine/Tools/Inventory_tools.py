
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from Ingenium_Engine.Tools.Characteristics_tools import Characteristics_tools
from Ingenium_Engine.Tools.Item_gen import gen_item

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Inventory_tools:
    @staticmethod
    def gen_agent_inventory_dict(bias=None):
        inventory_dict = {"Money": 100,
                          "Resources": {"Iron": 0,
                                        "Gold": 0,
                                        "Diamond": 0,
                                        },
                          "Items": {"S_Tool": 0}
                          }

        return inventory_dict

    @staticmethod
    def equip_item(agent, item: str, item_quantity: int):
        """
        Equip item function used to add items that have an impact on agent characteristics
        (the agent characteristics are adjusted according to the item rating)
        """
        characteristics_tools = Characteristics_tools()
        item = gen_item(item)

        # --> Add item to agent inventory if not health potion
        if item.label.split()[-1] != "Health":
            # --> Add item to agent inventory
            if item.label in list(agent.inventory["Items"].keys()):
                agent.inventory["Items"][item.label] += item_quantity
            else:
                agent.inventory["Items"][item.label] = item_quantity

        # --> Adjust agent characteristics according to item
        agent.characteristics = characteristics_tools.increase_characteristic(agent.characteristics,
                                                                              item.label.split("_")[-1],
                                                                              item.rating*item_quantity)

    @staticmethod
    def unequip_item(agent, item: str, item_quantity: int):
        characteristics_tools = Characteristics_tools()
        item = gen_item(item)

        # --> Adjust agent characteristics according to item
        agent.characteristics = characteristics_tools.decrease_characteristic(agent.characteristics,
                                                                              item.label.split("_")[-1],
                                                                              item.rating*item_quantity)

        # --> Remove item from agent inventory
        if agent.inventory["Items"][item.label] - item_quantity < 0:
            raise Exception("!!! Item quantity removed from inventory too large !!!")
        else:
            agent.inventory["Items"][item.label] -= item_quantity

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
        if agent.characteristics["Cargo"] - agent.used_cargo < quantity:
            gathered_quantity = agent.characteristics["Cargo"] - agent.used_cargo
            if gathered_quantity < 0:
                print("No cargo space available")
                return 0
            else:
                return gathered_quantity
        else:
            return quantity
