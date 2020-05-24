
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


class Item:
    def __init__(self, label):
        """
        Item class used to generate various item types
        Available items labels:  - Health
                                 - Weapon
                                 - Armor
                                 - Tool

        Available items size:    - S
                                 - M
                                 - L


        :param label: Object label
        """

        items = {"One-handed melee weapons": {"Dagger": {"Bronze": {"Stab_attack": 4,       # +4	+2	-4	+1	0	0	0	0	+1	0	+3	0	0%	0
                                                                    "Slash_attack": 2,
                                                                    "Crush_attack": -4,
                                                                    "Magic_attack": 1,
                                                                    "Ranged_attack": 0,

                                                                    "Stab_defence": 0,
                                                                    "Slash_defence": 0,
                                                                    "Crush_defence": 0,
                                                                    "Magic_defence": 1,
                                                                    "Ranged_defence": 0,

                                                                    "Strength": 3,
                                                                    "Ranged_strength": 0,
                                                                    "Magic_damage": 0,
                                                                    "Prayer": 0},

                                                         "Iron": [],
                                                         "Steel": [],
                                                         "Black": [],
                                                         "Mithril": []},

                                              "Axe": {"Bronze": {"Stab_attack": -2,         # -2	+4	+2	0	0	0	+1	0	0	0	+5	0	0%	0
                                                                 "Slash_attack": 4,
                                                                 "Crush_attack": 2,
                                                                 "Magic_attack": 0,
                                                                 "Ranged_attack": 0,

                                                                 "Stab_defence": 0,
                                                                 "Slash_defence": 1,
                                                                 "Crush_defence": 0,
                                                                 "Magic_defence": 0,
                                                                 "Ranged_defence": 0,

                                                                 "Strength": 5,
                                                                 "Ranged_strength": 0,
                                                                 "Magic_damage": 0,
                                                                 "Prayer": 0},
                                                      "Iron": [],
                                                      "Steel": [],
                                                      "Black": [],
                                                      "Mithril": []},

                                              "Mace": {"Bronze": {"Stab_attack": 1,         # +1	-2	+6	0	0	0	0	0	0	0	+5	0	0%	+1
                                                                  "Slash_attack": -2,
                                                                  "Crush_attack": 6,
                                                                  "Magic_attack": 0,
                                                                  "Ranged_attack": 0,

                                                                  "Stab_defence": 0,
                                                                  "Slash_defence": 0,
                                                                  "Crush_defence": 0,
                                                                  "Magic_defence": 0,
                                                                  "Ranged_defence": 0,

                                                                  "Strength": 5,
                                                                  "Ranged_strength": 0,
                                                                  "Magic_damage": 0,
                                                                  "Prayer": 1},
                                                       "Iron": [],
                                                       "Steel": [],
                                                       "Black": [],
                                                       "Mithril": []},

                                              "Sword": {"Bronze": {"Stab_attack": 4,        # +4	+3	-2	0	0	0	+2	+1	0	0	+5	0	0%	0
                                                                   "Slash_attack": 3,
                                                                   "Crush_attack": -2,
                                                                   "Magic_attack": 0,
                                                                   "Ranged_attack": 0,

                                                                   "Stab_defence": 0,
                                                                   "Slash_defence": 2,
                                                                   "Crush_defence": 1,
                                                                   "Magic_defence": 0,
                                                                   "Ranged_defence": 0,

                                                                   "Strength": 5,
                                                                   "Ranged_strength": 0,
                                                                   "Magic_damage": 0,
                                                                   "Prayer": 0},
                                                        "Iron": [],
                                                        "Steel": [],
                                                        "Black": [],
                                                        "Mithril": []},

                                              "Longsword": {"Bronze": {"Stab_attack": 4,    # +4	+5	-2	0	0	0	+3	+2	0	0	+7	0	0%	0
                                                                       "Slash_attack": 5,
                                                                       "Crush_attack": -2,
                                                                       "Magic_attack": 0,
                                                                       "Ranged_attack": 0,

                                                                       "Stab_defence": 0,
                                                                       "Slash_defence": 3,
                                                                       "Crush_defence": 2,
                                                                       "Magic_defence": 0,
                                                                       "Ranged_defence": 0,

                                                                       "Strength": 7,
                                                                       "Ranged_strength": 0,
                                                                       "Magic_damage": 0,
                                                                       "Prayer": 0},
                                                            "Iron": [],
                                                            "Steel": [],
                                                            "Black": [],
                                                            "Mithril": []},

                                              "Scimitar": {"Bronze": {"Stab_attack": 1,     # +1	+7	-2	0	0	0	+1	0	0	0	+6	0	0%	0
                                                                      "Slash_attack": 7,
                                                                      "Crush_attack": -2,
                                                                      "Magic_attack": 0,
                                                                      "Ranged_attack": 0,

                                                                      "Stab_defence": 0,
                                                                      "Slash_defence": 1,
                                                                      "Crush_defence": 0,
                                                                      "Magic_defence": 0,
                                                                      "Ranged_defence": 0,

                                                                      "Strength": 6,
                                                                      "Ranged_strength": 0,
                                                                      "Magic_damage": 0,
                                                                      "Prayer": 0},
                                                           "Iron": [],
                                                           "Steel": [],
                                                           "Black": [],
                                                           "Mithril": []},

                                              # "Hasta": {},
                                              # "Warhammer": {},
                                              "Battleaxe": {"Bronze": {"Stab_attack": -2,   # -2	+6	+3	0	0	0	0	0	0	-1	+9	0	0%	0
                                                                       "Slash_attack": 6,
                                                                       "Crush_attack": 3,
                                                                       "Magic_attack": 0,
                                                                       "Ranged_attack": 0,

                                                                       "Stab_defence": 0,
                                                                       "Slash_defence": 0,
                                                                       "Crush_defence": 0,
                                                                       "Magic_defence": 1,
                                                                       "Ranged_defence": -1,

                                                                       "Strength": 9,
                                                                       "Ranged_strength": 0,
                                                                       "Magic_damage": 0,
                                                                       "Prayer": 0},
                                                            "Iron": [],
                                                            "Steel": [],
                                                            "Black": [],
                                                            "Mithril": []},

                                              "Pickaxe": {"Bronze": {"Stab_attack": 4,      # +4	-2	+2	0	0	0	+1	0	0	0	+5	0	0%	0
                                                                     "Slash_attack": -2,
                                                                     "Crush_attack": 2,
                                                                     "Magic_attack": 0,
                                                                     "Ranged_attack": 0,

                                                                     "Stab_defence": 0,
                                                                     "Slash_defence": 1,
                                                                     "Crush_defence": 0,
                                                                     "Magic_defence": 1,
                                                                     "Ranged_defence": 0,

                                                                     "Strength": 5,
                                                                     "Ranged_strength": 0,
                                                                     "Magic_damage": 0,
                                                                     "Prayer": 0},
                                                          "Iron": [],
                                                          "Steel": [],
                                                          "Black": [],
                                                          "Mithril": []}
                                              },

                 "Two-handed melee weapons": {"2h sword": {"Bronze": {"Stab_attack": -4,     # -4	+9	+8	-4	0	0	0	0	0	-1	+10	0	0%	0
                                                                      "Slash_attack": 9,
                                                                      "Crush_attack": 8,
                                                                      "Magic_attack": -4,
                                                                      "Ranged_attack": 0,

                                                                      "Stab_defence": 0,
                                                                      "Slash_defence": 0,
                                                                      "Crush_defence": 0,
                                                                      "Magic_defence": 0,
                                                                      "Ranged_defence": -1,

                                                                      "Strength": 10,
                                                                      "Ranged_strength": 0,
                                                                      "Magic_damage": 0,
                                                                      "Prayer": 0},
                                                           "Iron": [],
                                                           "Steel": [],
                                                           "Black": [],
                                                           "Mithril": []},
                                              # "Claws": {},
                                              # "Spear": {},
                                              # "halberd": {}
                                              },

                 "Armor": {"Med helm": {"Bronze": {"Stab_attack": 4,                        # 0	0	0	-3	-1	+3	+4	+2	-1	+4	0	0	0%	0
                                                   "Slash_attack": 2,
                                                   "Crush_attack": -4,
                                                   "Magic_attack": 1,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 0,
                                                   "Crush_defence": 0,
                                                   "Magic_defence": 1,
                                                   "Ranged_defence": 0,

                                                   "Strength": 3,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},
                                        "Iron": [],
                                        "Steel": [],
                                        "Black": [],
                                        "Mithril": []},

                           "Full helm": {"Bronze": {"Stab_attack": 4,                       # 0	0	0	-6	-2	+4	+5	+3	-1	+4	0	0	0%	0
                                                    "Slash_attack": 2,
                                                    "Crush_attack": -4,
                                                    "Magic_attack": 1,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 1,
                                                    "Ranged_defence": 0,

                                                    "Strength": 3,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Chainbody": {"Bronze": {"Stab_attack": 4,                       # 0	0	0	-15	0	+7	+11	+13	-3	+6	0	0	0%	0
                                                    "Slash_attack": 2,
                                                    "Crush_attack": -4,
                                                    "Magic_attack": 1,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 1,
                                                    "Ranged_defence": 0,

                                                    "Strength": 3,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Platebody": {"Bronze": {"Stab_attack": 4,                       #
                                                    "Slash_attack": 2,
                                                    "Crush_attack": -4,
                                                    "Magic_attack": 1,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 1,
                                                    "Ranged_defence": 0,

                                                    "Strength": 3,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Platelegs": {"Bronze": {"Stab_attack": 4,                       #
                                                    "Slash_attack": 2,
                                                    "Crush_attack": -4,
                                                    "Magic_attack": 1,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 1,
                                                    "Ranged_defence": 0,

                                                    "Strength": 3,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Plateskirt": {"Bronze": {"Stab_attack": 4,                      #
                                                     "Slash_attack": 2,
                                                     "Crush_attack": -4,
                                                     "Magic_attack": 1,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 0,
                                                     "Slash_defence": 0,
                                                     "Crush_defence": 0,
                                                     "Magic_defence": 1,
                                                     "Ranged_defence": 0,

                                                     "Strength": 3,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0},
                                          "Iron": [],
                                          "Steel": [],
                                          "Black": [],
                                          "Mithril": []},

                           "Sq shield": {"Bronze": {"Stab_attack": 4,
                                                    "Slash_attack": 2,
                                                    "Crush_attack": -4,
                                                    "Magic_attack": 1,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 1,
                                                    "Ranged_defence": 0,

                                                    "Strength": 3,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Kiteshield": {"Bronze": {"Stab_attack": 4,
                                                     "Slash_attack": 2,
                                                     "Crush_attack": -4,
                                                     "Magic_attack": 1,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 0,
                                                     "Slash_defence": 0,
                                                     "Crush_defence": 0,
                                                     "Magic_defence": 1,
                                                     "Ranged_defence": 0,

                                                     "Strength": 3,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0},
                                          "Iron": [],
                                          "Steel": [],
                                          "Black": [],
                                          "Mithril": []},

                           "Boots": {"Bronze": {"Stab_attack": 4,
                                                "Slash_attack": 2,
                                                "Crush_attack": -4,
                                                "Magic_attack": 1,
                                                "Ranged_attack": 0,

                                                "Stab_defence": 0,
                                                "Slash_defence": 0,
                                                "Crush_defence": 0,
                                                "Magic_defence": 1,
                                                "Ranged_defence": 0,

                                                "Strength": 3,
                                                "Ranged_strength": 0,
                                                "Magic_damage": 0,
                                                "Prayer": 0},
                                     "Iron": [],
                                     "Steel": [],
                                     "Black": [],
                                     "Mithril": []},

                           "Gloves": {"Bronze": {"Stab_attack": 4,
                                                 "Slash_attack": 2,
                                                 "Crush_attack": -4,
                                                 "Magic_attack": 1,
                                                 "Ranged_attack": 0,

                                                 "Stab_defence": 0,
                                                 "Slash_defence": 0,
                                                 "Crush_defence": 0,
                                                 "Magic_defence": 1,
                                                 "Ranged_defence": 0,

                                                 "Strength": 3,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},
                                      "Iron": [],
                                      "Steel": [],
                                      "Black": [],
                                      "Mithril": []}
                           },
                 }
