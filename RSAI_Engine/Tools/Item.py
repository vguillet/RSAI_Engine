
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

        items = {"One-handed melee weapons": {# ========================================================================
                                              "Dagger": {"Bronze": {"Stab_attack": 4,       # +4	+2	-4	+1	0	0	0	0	+1	0	+3	0	0%	0
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

                                                         "Iron": {"Stab_attack": 5,         # +5	+3	-4	+1	0	0	0	0	+1	0	+4	0	0%	0
                                                                  "Slash_attack": 3,
                                                                  "Crush_attack": -4,
                                                                  "Magic_attack": 1,
                                                                  "Ranged_attack": 0,

                                                                  "Stab_defence": 0,
                                                                  "Slash_defence": 0,
                                                                  "Crush_defence": 0,
                                                                  "Magic_defence": 1,
                                                                  "Ranged_defence": 0,

                                                                  "Strength": 4,
                                                                  "Ranged_strength": 0,
                                                                  "Magic_damage": 0,
                                                                  "Prayer": 0},

                                                         "Steel": {"Stab_attack": 8,        # +8	+4	-4	+1	0	0	0	0	+1	0	+7	0	0%	0
                                                                   "Slash_attack": 4,
                                                                   "Crush_attack": -4,
                                                                   "Magic_attack": 1,
                                                                   "Ranged_attack": 0,

                                                                   "Stab_defence": 0,
                                                                   "Slash_defence": 0,
                                                                   "Crush_defence": 0,
                                                                   "Magic_defence": 1,
                                                                   "Ranged_defence": 0,

                                                                   "Strength": 7,
                                                                   "Ranged_strength": 0,
                                                                   "Magic_damage": 0,
                                                                   "Prayer": 0},

                                                         "Black": {"Stab_attack": 10,        # +10	+5	-4	+1	0	0	0	0	+1	0	+7	0	0%	0
                                                                   "Slash_attack": 5,
                                                                   "Crush_attack": -4,
                                                                   "Magic_attack": 1,
                                                                   "Ranged_attack": 0,

                                                                   "Stab_defence": 0,
                                                                   "Slash_defence": 0,
                                                                   "Crush_defence": 0,
                                                                   "Magic_defence": 1,
                                                                   "Ranged_defence": 0,

                                                                   "Strength": 7,
                                                                   "Ranged_strength": 0,
                                                                   "Magic_damage": 0,
                                                                   "Prayer": 0},

                                                         "Mithril": {"Stab_attack": 11,      # +11	+5	-4	+1	0	0	0	0	+1	0	+10	0	0	0
                                                                   "Slash_attack": 5,
                                                                   "Crush_attack": -4,
                                                                   "Magic_attack": 1,
                                                                   "Ranged_attack": 0,

                                                                   "Stab_defence": 0,
                                                                   "Slash_defence": 0,
                                                                   "Crush_defence": 0,
                                                                   "Magic_defence": 1,
                                                                   "Ranged_defence": 0,

                                                                   "Strength": 10,
                                                                   "Ranged_strength": 0,
                                                                   "Magic_damage": 0,
                                                                   "Prayer": 0}},

                                              # ========================================================================
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

                                                      "Iron": {"Stab_attack": -2,           # -2	+5	+3	0	0	0	+1	0	0	0	+7	0	0%	0
                                                               "Slash_attack": 5,
                                                               "Crush_attack": 3,
                                                               "Magic_attack": 0,
                                                               "Ranged_attack": 0,

                                                               "Stab_defence": 0,
                                                               "Slash_defence": 1,
                                                               "Crush_defence": 0,
                                                               "Magic_defence": 0,
                                                               "Ranged_defence": 0,

                                                               "Strength": 7,
                                                               "Ranged_strength": 0,
                                                               "Magic_damage": 0,
                                                               "Prayer": 0},

                                                      "Steel": {"Stab_attack": -2,          #  -2	+8	+6	0	0	0	+1	0	0	0	+9	0	0%	0
                                                                "Slash_attack": 8,
                                                                "Crush_attack": 6,
                                                                "Magic_attack": 0,
                                                                "Ranged_attack": 0,

                                                                "Stab_defence": 0,
                                                                "Slash_defence": 1,
                                                                "Crush_defence": 0,
                                                                "Magic_defence": 0,
                                                                "Ranged_defence": 0,

                                                                "Strength": 9,
                                                                "Ranged_strength": 0,
                                                                "Magic_damage": 0,
                                                                "Prayer": 0},

                                                      "Black": {"Stab_attack": -2,          # -2	+10	+8	0	0	0	+1	0	0	0	+12	0	0%	0
                                                                "Slash_attack": 10,
                                                                "Crush_attack": 8,
                                                                "Magic_attack": 0,
                                                                "Ranged_attack": 0,

                                                                "Stab_defence": 0,
                                                                "Slash_defence": 1,
                                                                "Crush_defence": 0,
                                                                "Magic_defence": 0,
                                                                "Ranged_defence": 0,

                                                                "Strength": 12,
                                                                "Ranged_strength": 0,
                                                                "Magic_damage": 0,
                                                                "Prayer": 0},

                                                      "Mithril": {"Stab_attack": -2,        # -2	+12	+10	0	0	0	+1	0	0	0	+13	0	0	0
                                                                  "Slash_attack": 12,
                                                                  "Crush_attack": 10,
                                                                  "Magic_attack": 0,
                                                                  "Ranged_attack": 0,

                                                                  "Stab_defence": 0,
                                                                  "Slash_defence": 1,
                                                                  "Crush_defence": 0,
                                                                  "Magic_defence": 0,
                                                                  "Ranged_defence": 0,

                                                                  "Strength": 13,
                                                                  "Ranged_strength": 0,
                                                                  "Magic_damage": 0,
                                                                  "Prayer": 0}},

                                              # ========================================================================
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

                                                       "Iron": {"Stab_attack": 4,           # +4	-2	+9	0	0	0	0	0	0	0	+7	0	0%	+1
                                                                "Slash_attack": -2,
                                                                "Crush_attack": 9,
                                                                "Magic_attack": 0,
                                                                "Ranged_attack": 0,

                                                                "Stab_defence": 0,
                                                                "Slash_defence": 0,
                                                                "Crush_defence": 0,
                                                                "Magic_defence": 0,
                                                                "Ranged_defence": 0,

                                                                "Strength": 7,
                                                                "Ranged_strength": 0,
                                                                "Magic_damage": 0,
                                                                "Prayer": 1},

                                                       "Steel": {"Stab_attack": 7,          # +7	-2	+13	0	0	0	0	0	0	0	+11	0	0%	+2
                                                                 "Slash_attack": -2,
                                                                 "Crush_attack": 13,
                                                                 "Magic_attack": 0,
                                                                 "Ranged_attack": 0,

                                                                 "Stab_defence": 0,
                                                                 "Slash_defence": 0,
                                                                 "Crush_defence": 0,
                                                                 "Magic_defence": 0,
                                                                 "Ranged_defence": 0,

                                                                 "Strength": 11,
                                                                 "Ranged_strength": 0,
                                                                 "Magic_damage": 0,
                                                                 "Prayer": 2},

                                                       "Black": {"Stab_attack": 8,          # +8	-2	+16	0	0	0	0	0	0	0	+13	0	0%	+2
                                                                 "Slash_attack": -2,
                                                                 "Crush_attack": 16,
                                                                 "Magic_attack": 0,
                                                                 "Ranged_attack": 0,

                                                                 "Stab_defence": 0,
                                                                 "Slash_defence": 0,
                                                                 "Crush_defence": 0,
                                                                 "Magic_defence": 0,
                                                                 "Ranged_defence": 0,

                                                                 "Strength": 13,
                                                                 "Ranged_strength": 0,
                                                                 "Magic_damage": 0,
                                                                 "Prayer": 2},

                                                       "Mithril": {"Stab_attack": 11,        # +11	-2	+18	0	0	0	0	0	0	0	+16	0	0	+3
                                                                   "Slash_attack": -2,
                                                                   "Crush_attack": 18,
                                                                   "Magic_attack": 0,
                                                                   "Ranged_attack": 0,

                                                                   "Stab_defence": 0,
                                                                   "Slash_defence": 0,
                                                                   "Crush_defence": 0,
                                                                   "Magic_defence": 0,
                                                                   "Ranged_defence": 0,

                                                                   "Strength": 16,
                                                                   "Ranged_strength": 0,
                                                                   "Magic_damage": 0,
                                                                   "Prayer": 3}},

                                              # ========================================================================
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

                                                        "Iron": {"Stab_attack": 6,        # +6	+4	-2	0	0	0	+2	+1	0	0	+7	0	0%	0
                                                                 "Slash_attack": 4,
                                                                 "Crush_attack": -2,
                                                                 "Magic_attack": 0,
                                                                 "Ranged_attack": 0,

                                                                 "Stab_defence": 0,
                                                                 "Slash_defence": 2,
                                                                 "Crush_defence": 1,
                                                                 "Magic_defence": 0,
                                                                 "Ranged_defence": 0,

                                                                 "Strength": 7,
                                                                 "Ranged_strength": 0,
                                                                 "Magic_damage": 0,
                                                                 "Prayer": 0},

                                                        "Steel": {"Stab_attack": 11,        # +11	+8	-2	0	0	0	+2	+1	0	0	+12	0	0%	0
                                                                  "Slash_attack": 8,
                                                                  "Crush_attack": -2,
                                                                  "Magic_attack": 0,
                                                                  "Ranged_attack": 0,

                                                                  "Stab_defence": 0,
                                                                  "Slash_defence": 2,
                                                                  "Crush_defence": 1,
                                                                  "Magic_defence": 0,
                                                                  "Ranged_defence": 0,

                                                                  "Strength": 12,
                                                                  "Ranged_strength": 0,
                                                                  "Magic_damage": 0,
                                                                  "Prayer": 0},

                                                        "Black": {"Stab_attack": 14,        # +14	+10	-2	0	0	0	+2	+1	0	0	+12	0	0%	0
                                                                  "Slash_attack": 10,
                                                                  "Crush_attack": -2,
                                                                  "Magic_attack": 0,
                                                                  "Ranged_attack": 0,

                                                                  "Stab_defence": 0,
                                                                  "Slash_defence": 2,
                                                                  "Crush_defence": 1,
                                                                  "Magic_defence": 0,
                                                                  "Ranged_defence": 0,

                                                                  "Strength": 12,
                                                                  "Ranged_strength": 0,
                                                                  "Magic_damage": 0,
                                                                  "Prayer": 0},

                                                        "Mithril": {"Stab_attack": 16,        # +16	+11	-2	0	0	0	+2	+1	0	0	+17	0	0	0
                                                                    "Slash_attack": 11,
                                                                    "Crush_attack": -2,
                                                                    "Magic_attack": 0,
                                                                    "Ranged_attack": 0,

                                                                    "Stab_defence": 0,
                                                                    "Slash_defence": 2,
                                                                    "Crush_defence": 1,
                                                                    "Magic_defence": 0,
                                                                    "Ranged_defence": 0,

                                                                    "Strength": 17,
                                                                    "Ranged_strength": 0,
                                                                    "Magic_damage": 0,
                                                                    "Prayer": 0}},

                                              # ========================================================================
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

                                                            "Iron": {"Stab_attack": 4,    # +6	+8	-2	0	0	0	+3	+2	0	0	+10	0	0%	0
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

                                                            "Steel": {"Stab_attack": 4,    # +9	+14	-2	0	0	0	+3	+2	0	0	+16	0	0%	0
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

                                                            "Black": {"Stab_attack": 4,    # +13	+18	-2	0	0	0	+3	+2	0	0	+16	0	0%	0
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

                                                            "Mithril": {"Stab_attack": 4,    # +15	+20	-2	0	0	0	+3	+2	0	0	+22	0	0	0
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
                                                                        "Prayer": 0}},

                                              # ========================================================================
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

                                              # ========================================================================
                                              # "Hasta": {},
                                              # "Warhammer": {},

                                              # ========================================================================
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

                                              # ========================================================================
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

                 "Armor": {"Med helm": {"Bronze": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+3	+4	+2	-1	+4	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -3,
                                                   "Ranged_attack": -1,

                                                   "Stab_defence": 3,
                                                   "Slash_defence": 4,
                                                   "Crush_defence": 2,
                                                   "Magic_defence": -1,
                                                   "Ranged_defence": 4,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},
                                        "Iron": [],
                                        "Steel": [],
                                        "Black": [],
                                        "Mithril": []},

                           "Full helm": {"Bronze": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+4	+5	+3	-1	+4	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -6,
                                                    "Ranged_attack": -2,

                                                    "Stab_defence": 4,
                                                    "Slash_defence": 5,
                                                    "Crush_defence": 3,
                                                    "Magic_defence": -1,
                                                    "Ranged_defence": 4,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Chainbody": {"Bronze": {"Stab_attack": 0,                       # 0	0	0	-15	0	+7	+11	+13	-3	+6	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -15,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 7,
                                                    "Slash_defence": 11,
                                                    "Crush_defence": 13,
                                                    "Magic_defence": -3,
                                                    "Ranged_defence": 6,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Platebody": {"Bronze": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+15	+14	+9	-6	+14	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -30,
                                                    "Ranged_attack": -10,

                                                    "Stab_defence": 15,
                                                    "Slash_defence": 14,
                                                    "Crush_defence": 9,
                                                    "Magic_defence": -6,
                                                    "Ranged_defence": 14,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Platelegs": {"Bronze": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+8	+7	+6	-4	+7	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -21,
                                                    "Ranged_attack": -7,

                                                    "Stab_defence": 8,
                                                    "Slash_defence": 7,
                                                    "Crush_defence": 6,
                                                    "Magic_defence": -4,
                                                    "Ranged_defence": 7,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Plateskirt": {"Bronze": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+8	+7	+6	-4	+7	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -21,
                                                     "Ranged_attack": -7,

                                                     "Stab_defence": 8,
                                                     "Slash_defence": 7,
                                                     "Crush_defence": 6,
                                                     "Magic_defence": -4,
                                                     "Ranged_defence": 7,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0},
                                          "Iron": [],
                                          "Steel": [],
                                          "Black": [],
                                          "Mithril": []},

                           "Sq shield": {"Bronze": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+5	+6	+4	0	+5	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -6,
                                                    "Ranged_attack": -2,

                                                    "Stab_defence": 5,
                                                    "Slash_defence": 6,
                                                    "Crush_defence": 4,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": 5,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},
                                         "Iron": [],
                                         "Steel": [],
                                         "Black": [],
                                         "Mithril": []},

                           "Kiteshield": {"Bronze": {"Stab_attack": 0,                      # 0	0	0	-8	-2	+5	+7	+6	-1	+6	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -8,
                                                     "Ranged_attack": -2,

                                                     "Stab_defence": 5,
                                                     "Slash_defence": 7,
                                                     "Crush_defence": 6,
                                                     "Magic_defence": -1,
                                                     "Ranged_defence": 6,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0},
                                          "Iron": [],
                                          "Steel": [],
                                          "Black": [],
                                          "Mithril": []},

                           "Boots": {"Bronze": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+1	+2	+3	0	0	0	0	0%	0
                                                "Slash_attack": 0,
                                                "Crush_attack": 0,
                                                "Magic_attack": -3,
                                                "Ranged_attack": -1,

                                                "Stab_defence": 1,
                                                "Slash_defence": 2,
                                                "Crush_defence": 3,
                                                "Magic_defence": 0,
                                                "Ranged_defence": 0,

                                                "Strength": 0,
                                                "Ranged_strength": 0,
                                                "Magic_damage": 0,
                                                "Prayer": 0},
                                     "Iron": [],
                                     "Steel": [],
                                     "Black": [],
                                     "Mithril": []},

                           "Gloves": {"Bronze": {"Stab_attack": 2,                          # +2	+2	+2	+1	+2	+2	+2	+2	+1	+2	+2	0	0%	0
                                                 "Slash_attack": 2,
                                                 "Crush_attack": 2,
                                                 "Magic_attack": 1,
                                                 "Ranged_attack": 2,

                                                 "Stab_defence": 2,
                                                 "Slash_defence": 2,
                                                 "Crush_defence": 2,
                                                 "Magic_defence": 1,
                                                 "Ranged_defence": 2,

                                                 "Strength": 2,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},
                                      "Iron": [],
                                      "Steel": [],
                                      "Black": [],
                                      "Mithril": []}
                           },
                 }
