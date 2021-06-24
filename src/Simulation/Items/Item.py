
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
                                     - Dagger
                                     - Axe
                                     - Mace
                                     - Sword
                                     - Longsword
                                     - Scimitar
                                     - Battleaxe
                                     - Pickaxe

                                 - Helm
                                     - Med_helm
                                     - Full_helm

                                 - Chest
                                     - Chainbody
                                     - Platebody

                                 - Legs
                                     - Platelegs
                                     - Plateskirt

                                 - Shield
                                     - Sq_shield
                                     - Kiteshield

                                 - Boots
                                     - Boots

                                 - Gloves
                                     - Gloves

                                 - Resource
                                     - Ore
                                     - Ingot
                                     - Gems
                                         - Opal
                                         - Emerald
                                         - Sapphire
                                         - Diamond
                                     - Food
                                         - Small ration
                                         - Medium ration
                                         - Large ration

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
        return "src/Data/Assets/Items_assets/" + self.type + "/" + self.material + "_" + self.name.lower() + ".png"

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
                 "Gloves": None,
                 "Resources": None
                 }

        with open("src/Simulation/Items/Catalogue/Weapons.json") as f:
            items["Weapon"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Helms.json") as f:
            items["Helm"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Chests.json") as f:
            items["Chest"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Legs.json") as f:
            items["Legs"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Shields.json") as f:
            items["Shield"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Boots.json") as f:
            items["Boots"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Gloves.json") as f:
            items["Gloves"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Resources.json") as f:
            items["Resources"] = json.load(f)

        if type in items.keys():
            if name in items[type].keys():
                return items[type][name][material]
            else:
                return None
        else:
            return None
