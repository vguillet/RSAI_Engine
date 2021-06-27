
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


class Skills:
    def __init__(self, start_skills_dict=None):
        if start_skills_dict is None:
            self.skills_dict = self.gen_skills_dict()

        else:
            self.skills_dict = start_skills_dict

    def __call__(self):
        """
        Return skills_dict when called

        :return: skills_dict
        """
        return self.skills_dict

    @staticmethod
    def gen_skills_dict():
        """
        Create new skills dict

        :return: skills_dict
        """
        skills_dict = {"Attack": {"Experience": 0,
                                  "Level": 1},

                       "Strength": {"Experience": 0,
                                    "Level": 1},

                       "Defence": {"Experience": 0,
                                   "Level": 1},

                       "Ranged": {"Experience": 0,
                                  "Level": 1},

                       "Prayer": {"Experience": 0,
                                  "Level": 1},

                       "Magic": {"Experience": 0,
                                 "Level": 1},

                       "Runecrafting": {"Experience": 0,
                                        "Level": 1},

                       "Hitpoint": {"Experience": 0,
                                    "Level": 10},

                       "Crafting": {"Experience": 0,
                                    "Level": 1},

                       "Mining": {"Experience": 0,
                                  "Level": 1},

                       "Smithing": {"Experience": 0,
                                    "Level": 1},

                       "Fishing": {"Experience": 0,
                                   "Level": 1},

                       "Cooking": {"Experience": 1,
                                   "Level": 0},

                       "Firemaking": {"Experience": 0,
                                      "Level": 1},

                       "Woodcutting": {"Experience": 0,
                                       "Level": 1}
                       }

        return skills_dict
