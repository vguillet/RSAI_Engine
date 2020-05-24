
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


class State_tools:
    @staticmethod
    def gen_agent_state_dict():
        characteristics_dict = {"Age": 1,
                                "Health": 10,

                                "Stab_attack": 0,
                                "Slash_attack": 0,
                                "Crush_attack": 0,
                                "Magic_attack": 0,
                                "Ranged_attack": 0,

                                "Stab_defence": 0,
                                "Slash_defence": 0,
                                "Crush_defence": 0,
                                "Magic_defence": 0,
                                "Ranged_defence": 0,

                                "Strength": 0,
                                "Ranged_strength": 0,
                                "Magic_damage": 0,
                                "Prayer": 0,

                                "Inventory": 0}

        return characteristics_dict

    @staticmethod
    def gen_mine_state_dict(inventory):
        characteristics_dict = {}                      # Resource mining difficulty

        for resource in inventory["Resources"].keys():
            if resource == "Iron":
                characteristics_dict[resource] = 10

            elif resource == "Gold":
                characteristics_dict[resource] = 60

            elif resource == "Diamond":
                characteristics_dict[resource] = 100

        return characteristics_dict
