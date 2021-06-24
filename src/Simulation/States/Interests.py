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


class Interests:
    def __init__(self, traded_item_types=[""], start_interests_dict=None):
        if start_interests_dict is None:
            self.interests_dict = self.gen_interests_dict(traded_item_types)

        else:
            self.interests_dict = start_interests_dict

        # self.increase_interests = self.__monkey_patch_pass
        # self.decrease_interests = self.__monkey_patch_pass

    def __call__(self):
        """
        Return interests_dict when called

        :return: interests_dict
        """
        return self.interests_dict

    @staticmethod
    def gen_interests_dict(traded_item_types):
        interests_dict = {"Weapon": None,
                          "Helm": None,
                          "Chest": None,
                          "Legs": None,
                          "Shield": None,
                          "Boots": None,
                          "Gloves": None,
                          "Resources": None
                          }

        with open("src/Simulation/Items/Catalogue/Weapons.json") as f:
            interests_dict["Weapon"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Helms.json") as f:
            interests_dict["Helm"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Chests.json") as f:
            interests_dict["Chest"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Legs.json") as f:
            interests_dict["Legs"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Shields.json") as f:
            interests_dict["Shield"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Boots.json") as f:
            interests_dict["Boots"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Gloves.json") as f:
            interests_dict["Gloves"] = json.load(f)

        with open("src/Simulation/Items/Catalogue/Resources.json") as f:
            interests_dict["Resources"] = json.load(f)

        # --> Remove non-traded items
        traded_types_interests_dict = {}

        for item_type in interests_dict:
            if item_type in traded_item_types:
                traded_types_interests_dict[item_type] = interests_dict[item_type]

        interests_dict = traded_types_interests_dict

        # --> Set interests
        material_factors = {"Bronze": 1,
                            "Iron": 1.2,
                            "Steel": 1.8,
                            "Black": 2.5,
                            "Mithril": 5,

                            "Opal": 50,
                            "Emerald": 70,
                            "Sapphire": 150,
                            "Diamond": 500,

                            "Small ration": 5,
                            "Medium ration": 10,
                            "Large ration": 20

                            }

        with open("src/Simulation/Items/Catalogue/Items_base_values.json") as f:
            items_base_value_dict = json.load(f)

            for item_type in interests_dict:
                for item in interests_dict[item_type]:
                    for material in interests_dict[item_type][item]:
                        # --> Set expectation, minimum (10% bellow), and maximum (10% above)
                        interests_dict[item_type][item][material] = {
                            "Expectation": round(items_base_value_dict[item] * material_factors[material]),
                            "Minimum": round(items_base_value_dict[item] * material_factors[material] * 0.9),
                            "Maximum": round(items_base_value_dict[item] * material_factors[material] * 1.1)
                            }

        return interests_dict

    @staticmethod
    def __monkey_patch_pass(interests_dict, *args, **kwargs):
        return interests_dict

    @staticmethod
    def increase_expectation(interests_dict, difference=None, delta_percent=10, setting=0):
        # TODO: Add expectation settings
        # --> Fixed value expectation increase
        if setting == 0:
            if interests_dict["Maximum"] > interests_dict["Expectation"] + 1:
                interests_dict["Expectation"] += 1
                return interests_dict
            else:
                interests_dict["Expectation"] = interests_dict["Maximum"]
                return interests_dict

        # --> Surplus percent based expectation increase
        if setting == 1:
            if interests_dict["Maximum"] > interests_dict["Expectation"] + delta_percent * difference:
                interests_dict["Expectation"] += delta_percent * difference
                return interests_dict
            else:
                interests_dict["Expectation"] = interests_dict["Maximum"]
                return interests_dict

    @staticmethod
    def decrease_expectation(interests_dict, difference, delta_percent=10, setting=0):
        # --> Fixed value expectation decrease
        if setting == 0:
            if interests_dict["Minimum"] > interests_dict["Expectation"] - 1:
                interests_dict["Expectation"] -= 1
                return interests_dict
            else:
                interests_dict["Expectation"] = interests_dict["Minimum"]
                return interests_dict

        # --> Expectation difference percent based expectation decrease
        if setting == 1:
            if interests_dict["Minimum"] > interests_dict["Expectation"] - delta_percent * difference:
                interests_dict["Expectation"] -= delta_percent * difference
                return interests_dict
            else:
                interests_dict["Expectation"] = interests_dict["Minimum"]
                return interests_dict


if __name__ == "__main__":
    print(Interests().interests_dict)
