
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


class States:
    def __init__(self, start_states_dict=None):
        if start_states_dict is None:
            self.states_dict = self.gen_states_dict()

        else:
            self.states_dict = start_states_dict

    def __call__(self):
        """
        Return states_dict when called

        :return: states_dict
        """
        return self.states_dict

    @staticmethod
    def gen_states_dict():
        """
        Create new states dict

        :return: states_dict
        """
        state_dict = {"Age": 1,
                      "Hitpoints": 10,

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
