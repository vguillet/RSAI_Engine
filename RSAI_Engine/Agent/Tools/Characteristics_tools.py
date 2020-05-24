
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


class Characteristics_tools:
    @staticmethod
    def increase_characteristic(characteristics_dict, characteristic: str, amount: int):
        if characteristics_dict[characteristic] + amount > 100:
            characteristics_dict[characteristic] = 100
        else:
            characteristics_dict[characteristic] += amount

        return characteristics_dict

    @staticmethod
    def decrease_characteristic(characteristics_dict, characteristic: str, amount: int):
        if characteristics_dict[characteristic] - amount < 1:
            characteristics_dict[characteristic] = 1
        else:
            characteristics_dict[characteristic] -= amount

        return characteristics_dict

    @staticmethod
    def gen_agent_characteristics_dict():
        characteristics_dict = {"Age": 1,
                                "Health": 100,
                                "Weapon": 0,
                                "Armor": 0,
                                "Tool": 20,
                                "Cargo": 5}

        return characteristics_dict

    @staticmethod
    def gen_mine_characteristics_dict(inventory):
        characteristics_dict = {"Reputation": 100,
                                "Infrastructure": 100,
                                "RMD": {}}                      # Resource mining difficulty

        for resource in inventory["Resources"].keys():
            if resource == "Iron":
                characteristics_dict["RMD"][resource] = 10

            elif resource == "Gold":
                characteristics_dict["RMD"][resource] = 60

            elif resource == "Diamond":
                characteristics_dict["RMD"][resource] = 100

        return characteristics_dict

    @staticmethod
    def gen_market_characteristics_dict():
        characteristics_dict = {"Reputation": 100,
                                "Honesty": 100
                                }

        return characteristics_dict

