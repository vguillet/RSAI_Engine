
################################################################################################################
"""

"""

# Built-in/Generic Imports
import json

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Item:
    def __init__(self, type, name, material):
        """
        Item class used to generate various item types
        Available items labels:  - Weapon
                                 - Helm
                                 - Chest
                                 - Legs
                                 - Shield
                                 - Boots
                                 - Gloves

        Available items materials:    - Bronze
                                      - Iron
                                      - Steel
                                      - Black
                                      - Mithril

        """

        # --> Setup item
        self.type = type
        self.name = name
        self.material = material

        # --> Get item properties
        self.properties = self.get_item_properties(type, name, material)

    def __str__(self):
        return self.material + " " + self.name

    def __repr__(self):
        return self.__str__()

    @property
    def asset_path(self):
        return "RSAI_Engine/Data/Assets/Items_assets/" + self.type + "/" + self.material + "_" + self.name.lower() + ".png"

    @staticmethod
    def get_item_properties(type, name, material):
        """
        Retrieve items properties

        :param type: Item type
        :param name: Item name
        :param material: Item material

        :return: properties_dict
        """

        items = {"Weapon": None,
                 "Helm": None,
                 "Chest": None,
                 "Legs": None,
                 "Shield": None,
                 "Boots": None,
                 "Gloves": None
                 }

        with open("RSAI_Engine/Simulation/Items/Weapons.json") as f:
            items["Weapon"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Helms.json") as f:
            items["Helm"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Chests.json") as f:
            items["Chest"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Legs.json") as f:
            items["Legs"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Shields.json") as f:
            items["Shield"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Boots.json") as f:
            items["Boots"] = json.load(f)

        with open("RSAI_Engine/Simulation/Items/Gloves.json") as f:
            items["Gloves"] = json.load(f)

        if type in items.keys():
            if name in items[type].keys():
                properties_dict = items[type][name][material]

            else:
                properties_dict = None
        else:
            properties_dict = None

        return properties_dict
