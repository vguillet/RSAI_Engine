
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Item:
    def __init__(self, label):
        """
        Item class used to generate various item types
        Available items labels:  - Health
                                 - Weapon
                                 - Armor
                                 - Tool

        Available items size:    - S
                                 - M
                                 - L


        :param label: Object label
        """
        # ----- Setup reference properties
        self.type = "Item"
        self.label = label

        item_size = label.split("_")[0]

        if item_size == "S":
            self.rating = 5

        elif item_size == "M":
            self.rating = 20

        elif item_size == "L":
            self.rating = 50
