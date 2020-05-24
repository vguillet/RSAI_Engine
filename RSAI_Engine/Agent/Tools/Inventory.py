
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from RSAI_Engine.Agent.Tools.States import States
from RSAI_Engine.Agent.Tools.Skills import Skills
from RSAI_Engine.Tools.Item import Item

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Inventory:
    def __init__(self, start_inventory_dict=None):
        if start_inventory_dict is None:
            self.inventory_dict = self.gen_inventory_dict()
        else:
            self.inventory_dict = start_inventory_dict

        self.max_size = 4 * 7

    def __call__(self):
        """
        Return inventory_dict when called

        :return: inventory_dict
        """
        return self.inventory_dict

    @property
    def size(self):
        """
        Size of inventory (including gold as +1)

        :return: size of inventory
        """
        return len(self.inventory_dict["Content"]) + 1

    @staticmethod
    def gen_inventory_dict():
        """
        Create new empty inventory dict

        :return: inventory_dict
        """
        inventory_dict = {"Money": 0,
                          "Content": []
                          }

        return inventory_dict

    def add_item_to_inventory(self, item):
        """
        Add item to inventory

        :param item: Item to be added
        """
        if self.size < self.max_size:
            self.inventory_dict["Content"].append(item)

    def remove_item_from_inventory(self, item):
        """
        Remove item from inventory

        :param item: Item to be removed
        """
        if item in self.inventory_dict["Content"]:
            self.inventory_dict["Content"].remove(item)
        else:
            print("!!!!! Item not in inventory !!!!!")
