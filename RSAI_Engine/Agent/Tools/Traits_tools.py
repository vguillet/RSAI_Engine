
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


class Traits_tools:
    @staticmethod
    def gen_traits_dict(specialisation=None):
        traits_dict = {"Combat": {"Experience": 0,
                                  "Level": 1},
                       "Mining": {"Experience": 0,
                                  "Level": 1},
                       "Trading": {"Experience": 0,
                                   "Level": 1}
                       }

        return traits_dict
