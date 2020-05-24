
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


class States_tools:
    @staticmethod
    def gen_states_dict():
        state_dict = {"Age": 1,
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

        return state_dict
