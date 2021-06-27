
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


class Statistics:
    def __init__(self, start_statistics_dict=None):
        if start_statistics_dict is None:
            self.statistics_dict = self.gen_statistics_dict()

        else:
            self.statistics_dict = start_statistics_dict

    def __call__(self):
        """
        Return statistics_dict when called

        :return: statistics_dict
        """
        return self.statistics_dict

    @staticmethod
    def gen_statistics_dict():
        """
        Create new statistics dict

        :return: statistics_dict
        """
        state_dict = {"Hitpoint": 10,

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
                      "Prayer": 0}

        return state_dict
