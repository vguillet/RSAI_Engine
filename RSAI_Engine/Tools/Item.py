
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
    def __init__(self, type, name, material):
        """
        Item class used to generate various item types
        Available items labels:  - Weapon
                                 - Helm
                                 - Chest
                                 - Legs
                                 - Shield
                                 - Boots
                                 - Gloves

        Available items materials:    - Bronze
                                      - Iron
                                      - Steel
                                      - Black
                                      - Mithril

        """

        # --> Setup item
        self.type = type
        self.name = name
        self.material = material

        # --> Get item properties
        self.properties = self.get_item_properties(type, name, material)

    def __str__(self):
        return self.material + self.name + "(item)"

    def __repr__(self):
        self.__repr__()

    @staticmethod
    def get_item_properties(type, name, material):
        """
        Retrieve items properties

        :param type: Item type
        :param name: Item name
        :param material: Item material

        :return: properties_dict
        """
        items = {
                 "Weapon": {# ========================================================================
                            "Dagger": {
                                       "Bronze": {"Stab_attack": 4,       # +4	+2	-4	+1	0	0	0	0	+1	0	+3	0	0%	0
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
                            "Axe": {
                                    "Bronze": {"Stab_attack": -2,         # -2	+4	+2	0	0	0	+1	0	0	0	+5	0	0%	0
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
                            "Mace": {
                                     "Bronze": {"Stab_attack": 1,         # +1	-2	+6	0	0	0	0	0	0	0	+5	0	0%	+1
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
                            "Sword": {
                                      "Bronze": {"Stab_attack": 4,        # +4	+3	-2	0	0	0	+2	+1	0	0	+5	0	0%	0
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
                            "Longsword": {
                                          "Bronze": {"Stab_attack": 4,    # +4	+5	-2	0	0	0	+3	+2	0	0	+7	0	0%	0
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

                                          "Iron": {"Stab_attack": 6,    # +6	+8	-2	0	0	0	+3	+2	0	0	+10	0	0%	0
                                                   "Slash_attack": 8,
                                                   "Crush_attack": -2,
                                                   "Magic_attack": 0,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 3,
                                                   "Crush_defence": 2,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": 0,

                                                   "Strength": 10,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                          "Steel": {"Stab_attack": 9,    # +9	+14	-2	0	0	0	+3	+2	0	0	+16	0	0%	0
                                                    "Slash_attack": 14,
                                                    "Crush_attack": -2,
                                                    "Magic_attack": 0,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 3,
                                                    "Crush_defence": 2,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": 0,

                                                    "Strength": 16,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Black": {"Stab_attack": 13,    # +13	+18	-2	0	0	0	+3	+2	0	0	+16	0	0%	0
                                                    "Slash_attack": 18,
                                                    "Crush_attack": -2,
                                                    "Magic_attack": 0,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 3,
                                                    "Crush_defence": 2,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": 0,

                                                    "Strength": 16,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Mithril": {"Stab_attack": 15,    # +15	+20	-2	0	0	0	+3	+2	0	0	+22	0	0	0
                                                      "Slash_attack": 20,
                                                      "Crush_attack": -2,
                                                      "Magic_attack": 0,
                                                      "Ranged_attack": 0,

                                                      "Stab_defence": 0,
                                                      "Slash_defence": 3,
                                                      "Crush_defence": 2,
                                                      "Magic_defence": 0,
                                                      "Ranged_defence": 0,

                                                      "Strength": 22,
                                                      "Ranged_strength": 0,
                                                      "Magic_damage": 0,
                                                      "Prayer": 0}},

                            # ========================================================================
                            "Scimitar": {
                                         "Bronze": {"Stab_attack": 1,     # +1	+7	-2	0	0	0	+1	0	0	0	+6	0	0%	0
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

                                         "Iron": {"Stab_attack": 2,     # +2	+10	-2	0	0	0	+1	0	0	0	+9	0	0%	0
                                                  "Slash_attack": 10,
                                                  "Crush_attack": -2,
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

                                         "Steel": {"Stab_attack": 3,     # +3	+15	-2	0	0	0	+1	0	0	0	+14	0	0%	0
                                                   "Slash_attack": 15,
                                                   "Crush_attack": -2,
                                                   "Magic_attack": 0,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 1,
                                                   "Crush_defence": 0,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": 0,

                                                   "Strength": 14,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Black": {"Stab_attack": 4,     # +4	+19	-2	0	0	0	+1	0	0	0	+14	0	0%	0
                                                   "Slash_attack": 19,
                                                   "Crush_attack": -2,
                                                   "Magic_attack": 0,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 1,
                                                   "Crush_defence": 0,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": 0,

                                                   "Strength": 14,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": 5,     # +5	+21	-2	0	0	0	+1	0	0	0	+20	0	0	0
                                                     "Slash_attack": 21,
                                                     "Crush_attack": -2,
                                                     "Magic_attack": 0,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 0,
                                                     "Slash_defence": 1,
                                                     "Crush_defence": 0,
                                                     "Magic_defence": 0,
                                                     "Ranged_defence": 0,

                                                     "Strength": 20,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},

                            # ========================================================================
                            # "Hasta": {},
                            # "Warhammer": {},

                            # ========================================================================
                            "Battleaxe": {
                                          "Bronze": {"Stab_attack": -2,   # -2	+6	+3	0	0	0	0	0	0	-1	+9	0	0%	0
                                                     "Slash_attack": 6,
                                                     "Crush_attack": 3,
                                                     "Magic_attack": 0,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 0,
                                                     "Slash_defence": 0,
                                                     "Crush_defence": 0,
                                                     "Magic_defence": 0,
                                                     "Ranged_defence": -1,

                                                     "Strength": 9,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0},

                                          "Iron": {"Stab_attack": -2,   # -2	+8	+5	0	0	0	0	0	0	-1	+13	0	0%	0
                                                   "Slash_attack": 8,
                                                   "Crush_attack": 5,
                                                    "Magic_attack": 0,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": -1,

                                                    "Strength": 13,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Steel": {"Stab_attack": -2,   # -2	+16	+11	0	0	0	0	0	0	-1	+20	0	0%	0
                                                    "Slash_attack": 16,
                                                    "Crush_attack": 11,
                                                    "Magic_attack": 0,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": -1,

                                                    "Strength": 20,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Black": {"Stab_attack": -2,   # -2	+20	+15	0	0	0	0	0	0	-1	+24	0	0%	0
                                                    "Slash_attack": 20,
                                                    "Crush_attack": 15,
                                                    "Magic_attack": 0,
                                                    "Ranged_attack": 0,

                                                    "Stab_defence": 0,
                                                    "Slash_defence": 0,
                                                    "Crush_defence": 0,
                                                    "Magic_defence": 0,
                                                    "Ranged_defence": -1,

                                                    "Strength": 24,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Mithril": {"Stab_attack": -2,   # -2	+22	+17	0	0	0	0	0	0	-1	+29	0	0	0
                                                      "Slash_attack": 22,
                                                      "Crush_attack": 17,
                                                      "Magic_attack": 0,
                                                      "Ranged_attack": 0,

                                                      "Stab_defence": 0,
                                                      "Slash_defence": 0,
                                                      "Crush_defence": 0,
                                                      "Magic_defence": 0,
                                                      "Ranged_defence": -1,

                                                      "Strength": 29,
                                                      "Ranged_strength": 0,
                                                      "Magic_damage": 0,
                                                      "Prayer": 0}},

                            # ========================================================================
                            "Pickaxe": {
                                        "Bronze": {"Stab_attack": 4,      # +4	-2	+2	0	0	0	+1	0	0	0	+5	0	0%	0
                                                   "Slash_attack": -2,
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

                                        "Iron": {"Stab_attack": 5,      # +5	-2	+3	0	0	0	+1	0	0	0	+7	0	0%	0
                                                 "Slash_attack": -2,
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

                                        "Steel": {"Stab_attack": 8,      # +8	-2	+6	0	0	0	+1	0	0	0	+9	0	0%	0
                                                  "Slash_attack": -2,
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

                                        "Black": {"Stab_attack": 10,      # +10	-2	+8	0	0	0	+1	0	0	0	+11	0	0%	0
                                                  "Slash_attack": -2,
                                                  "Crush_attack": 8,
                                                  "Magic_attack": 0,
                                                  "Ranged_attack": 0,

                                                  "Stab_defence": 0,
                                                  "Slash_defence": 1,
                                                  "Crush_defence": 0,
                                                  "Magic_defence": 0,
                                                  "Ranged_defence": 0,

                                                  "Strength": 11,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                        "Mithril": {"Stab_attack": 12,      # +12	-2	+10	0	0	0	+1	0	0	0	+13	0	0	0
                                                    "Slash_attack": -2,
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
                            "2h sword": {
                                         "Bronze": {"Stab_attack": -4,     # -4	+9	+8	-4	0	0	0	0	0	-1	+10	0	0%	0
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

                                         "Iron": {"Stab_attack": -4,     # -4	+13	+10	-4	0	0	0	0	0	-1	+14	0	0%	0
                                                  "Slash_attack": 13,
                                                  "Crush_attack": 10,
                                                  "Magic_attack": -4,
                                                  "Ranged_attack": 0,

                                                  "Stab_defence": 0,
                                                  "Slash_defence": 0,
                                                  "Crush_defence": 0,
                                                  "Magic_defence": 0,
                                                  "Ranged_defence": -1,

                                                  "Strength": 14,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                         "Steel": {"Stab_attack": -4,     # -4	+21	+16	-4	0	0	0	0	0	-1	+22	0	0%	0
                                                   "Slash_attack": 21,
                                                   "Crush_attack": 16,
                                                   "Magic_attack": -4,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 0,
                                                   "Crush_defence": 0,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": -1,

                                                    "Strength": 22,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                         "Black": {"Stab_attack": -4,     # -4	+27	+21	-4	0	0	0	0	0	-1	+26	0	0%	0
                                                   "Slash_attack": 27,
                                                   "Crush_attack": 21,
                                                   "Magic_attack": -4,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 0,
                                                   "Slash_defence": 0,
                                                   "Crush_defence": 0,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": -1,

                                                   "Strength": 26,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": -4,     # -4	+30	+24	-4	0	0	0	0	0	-1	+31	0	0	0
                                                     "Slash_attack": 30,
                                                     "Crush_attack": 24,
                                                     "Magic_attack": -4,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 0,
                                                     "Slash_defence": 0,
                                                     "Crush_defence": 0,
                                                     "Magic_defence": 0,
                                                     "Ranged_defence": -1,

                                                     "Strength": 31,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},

                             # ========================================================================
                             # "Claws": {},
                             # "Spear": {},
                             # "halberd": {}
                             },

                 "Helm": {# ============================================================================================
                          "Med helm": {
                                       "Bronze": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+3	+4	+2	-1	+4	0	0	0%	0
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

                                       "Iron": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+4	+5	+3	-1	+4	0	0	0%	0
                                                "Slash_attack": 0,
                                                "Crush_attack": 0,
                                                "Magic_attack": -3,
                                                "Ranged_attack": -1,

                                                "Stab_defence": 4,
                                                "Slash_defence": 5,
                                                "Crush_defence": 3,
                                                "Magic_defence": -1,
                                                "Ranged_defence": 4,

                                                "Strength": 0,
                                                "Ranged_strength": 0,
                                                "Magic_damage": 0,
                                                "Prayer": 0},

                                       "Steel": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+7	+8	+6	-1	+7	0	0	0%	0
                                                 "Slash_attack": 0,
                                                 "Crush_attack": 0,
                                                 "Magic_attack": -3,
                                                 "Ranged_attack": -1,

                                                 "Stab_defence": 7,
                                                 "Slash_defence": 8,
                                                 "Crush_defence": 6,
                                                 "Magic_defence": -1,
                                                 "Ranged_defence": 7,

                                                 "Strength": 0,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},

                                       "Black": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+9	+10	+8	-1	+9	0	0	0%	0
                                                 "Slash_attack": 0,
                                                 "Crush_attack": 0,
                                                 "Magic_attack": -3,
                                                 "Ranged_attack": -1,

                                                 "Stab_defence": 9,
                                                 "Slash_defence": 10,
                                                 "Crush_defence": 8,
                                                 "Magic_defence": -1,
                                                 "Ranged_defence": 9,

                                                 "Strength": 0,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},

                                       "Mithril": {"Stab_attack": 0,                        # 0	0	0	-3	-1	+10	+11	+9	-1	+10	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -3,
                                                   "Ranged_attack": -1,

                                                   "Stab_defence": 10,
                                                   "Slash_defence": 11,
                                                   "Crush_defence": 9,
                                                   "Magic_defence": -1,
                                                   "Ranged_defence": 10,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0}},

                           # ===========================================================================================
                          "Full helm": {
                                        "Bronze": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+4	+5	+3	-1	+4	0	0	0%	0
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

                                        "Iron": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+6	+7	+5	-1	+6	0	0	0%	0
                                                 "Slash_attack": 0,
                                                 "Crush_attack": 0,
                                                 "Magic_attack": -6,
                                                 "Ranged_attack": -2,

                                                 "Stab_defence": 6,
                                                 "Slash_defence": 7,
                                                 "Crush_defence": 5,
                                                 "Magic_defence": -1,
                                                 "Ranged_defence": 6,

                                                 "Strength": 0,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},

                                        "Steel": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+9	+10	+7	-1	+9	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -6,
                                                  "Ranged_attack": -2,

                                                  "Stab_defence": 9,
                                                  "Slash_defence": 10,
                                                  "Crush_defence": 7,
                                                  "Magic_defence": -1,
                                                  "Ranged_defence": 9,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                        "Black": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+12	+13	+10	-1	+12	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -6,
                                                  "Ranged_attack": -2,

                                                  "Stab_defence": 12,
                                                  "Slash_defence": 13,
                                                  "Crush_defence": 10,
                                                  "Magic_defence": -1,
                                                  "Ranged_defence": 12,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                        "Mithril": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+13	+14	+11	-1	+13	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -6,
                                                    "Ranged_attack": -2,

                                                    "Stab_defence": 13,
                                                    "Slash_defence": 14,
                                                    "Crush_defence": 11,
                                                    "Magic_defence": -1,
                                                    "Ranged_defence": 13,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0}}
                           },

                 "Chest": {# ===========================================================================================
                           "Chainbody": {
                                         "Bronze": {"Stab_attack": 0,                       # 0	0	0	-15	0	+7	+11	+13	-3	+6	0	0	0%	0
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

                                         "Iron": {"Stab_attack": 0,                       # 0	0	0	-15	0	+10	+15	+19	-3	+12	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -15,
                                                  "Ranged_attack": 0,

                                                  "Stab_defence": 10,
                                                  "Slash_defence": 15,
                                                  "Crush_defence": 19,
                                                  "Magic_defence": -3,
                                                  "Ranged_defence": 12,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                         "Steel": {"Stab_attack": 0,                       # 0	0	0	-15	0	+17	+25	+30	-3	+19	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -15,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 17,
                                                   "Slash_defence": 25,
                                                   "Crush_defence": 30,
                                                   "Magic_defence": -3,
                                                   "Ranged_defence": 19,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Black": {"Stab_attack": 0,                       # 0	0	0	-15	0	+22	+32	+39	-3	+24	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -15,
                                                   "Ranged_attack": 0,

                                                   "Stab_defence": 22,
                                                   "Slash_defence": 32,
                                                   "Crush_defence": 39,
                                                   "Magic_defence": -3,
                                                   "Ranged_defence": 24,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": 0,                       # 0	0	0	-15	0	+25	+35	+42	-3	+19	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -15,
                                                     "Ranged_attack": 0,

                                                     "Stab_defence": 25,
                                                     "Slash_defence": 35,
                                                     "Crush_defence": 42,
                                                     "Magic_defence": -3,
                                                     "Ranged_defence": 19,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},

                           # ===========================================================================================
                           "Platebody": {
                                         "Bronze": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+15	+14	+9	-6	+14	0	0	0%	0
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

                                         "Iron": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+21	+20	+12	-6	+20	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -30,
                                                  "Ranged_attack": -10,

                                                  "Stab_defence": 21,
                                                  "Slash_defence": 20,
                                                  "Crush_defence": 12,
                                                  "Magic_defence": -6,
                                                  "Ranged_defence": 20,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                         "Steel": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+32	+31	+24	-6	+31	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -30,
                                                   "Ranged_attack": -10,

                                                   "Stab_defence": 32,
                                                   "Slash_defence": 31,
                                                   "Crush_defence": 24,
                                                   "Magic_defence": -6,
                                                   "Ranged_defence": 31,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Black": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+41	+40	+30	-6	+40	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -30,
                                                   "Ranged_attack": -10,

                                                   "Stab_defence": 41,
                                                   "Slash_defence": 40,
                                                   "Crush_defence": 30,
                                                   "Magic_defence": -6,
                                                   "Ranged_defence": 40,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": 0,                       # 0	0	0	-30	-10	+46	+44	+38	-6	+44	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -30,
                                                     "Ranged_attack": -10,

                                                     "Stab_defence": 46,
                                                     "Slash_defence": 44,
                                                     "Crush_defence": 38,
                                                     "Magic_defence": -6,
                                                     "Ranged_defence": 44,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},
                           },

                 "Legs": {# ===========================================================================================
                          "Platelegs": {
                                        "Bronze": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+8	+7	+6	-4	+7	0	0	0%	0
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

                                        "Iron": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+11	+10	+10	-4	+10	0	0	0%	0
                                                 "Slash_attack": 0,
                                                 "Crush_attack": 0,
                                                 "Magic_attack": -21,
                                                 "Ranged_attack": -7,

                                                 "Stab_defence": 11,
                                                 "Slash_defence": 10,
                                                 "Crush_defence": 10,
                                                 "Magic_defence": -4,
                                                 "Ranged_defence": 10,

                                                 "Strength": 0,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0},

                                        "Steel": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+17	+16	+15	-4	+16	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -21,
                                                  "Ranged_attack": -7,

                                                  "Stab_defence": 17,
                                                  "Slash_defence": 16,
                                                  "Crush_defence": 15,
                                                  "Magic_defence": -4,
                                                  "Ranged_defence": 16,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                        "Black": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+21	+20	+19	-4	+20	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -21,
                                                  "Ranged_attack": -7,

                                                  "Stab_defence": 21,
                                                  "Slash_defence": 20,
                                                  "Crush_defence": 19,
                                                  "Magic_defence": -4,
                                                  "Ranged_defence": 20,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                        "Mithril": {"Stab_attack": 0,                       # 0	0	0	-21	-7	+24	+22	+20	-4	+22	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -21,
                                                    "Ranged_attack": -7,

                                                    "Stab_defence": 24,
                                                    "Slash_defence": 22,
                                                    "Crush_defence": 20,
                                                    "Magic_defence": -4,
                                                    "Ranged_defence": 22,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0}},

                          # ===========================================================================================
                          "Plateskirt": {
                                         "Bronze": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+8	+7	+6	-4	+7	0	0	0%	0
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

                                         "Iron": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+11	+10	+10	-4	+10	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -21,
                                                   "Ranged_attack": -7,

                                                   "Stab_defence": 11,
                                                   "Slash_defence": 10,
                                                   "Crush_defence": 10,
                                                   "Magic_defence": -4,
                                                   "Ranged_defence": 10,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Steel": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+17	+16	+15	-4	+16	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -21,
                                                   "Ranged_attack": -7,

                                                   "Stab_defence": 17,
                                                   "Slash_defence": 16,
                                                   "Crush_defence": 15,
                                                   "Magic_defence": -4,
                                                   "Ranged_defence": 16,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Black": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+21	+20	+19	-4	+20	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -21,
                                                   "Ranged_attack": -7,

                                                   "Stab_defence": 21,
                                                   "Slash_defence": 20,
                                                   "Crush_defence": 19,
                                                   "Magic_defence": -4,
                                                   "Ranged_defence": 20,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": 0,                      # 0	0	0	-21	-7	+24	+22	+20	-4	+22	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -21,
                                                     "Ranged_attack": -7,

                                                     "Stab_defence": 24,
                                                     "Slash_defence": 22,
                                                     "Crush_defence": 20,
                                                     "Magic_defence": -4,
                                                     "Ranged_defence": 22,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},
                           },

                 "Shield": {# ==========================================================================================
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

                                         "Iron": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+8	+9	+7	0	+8	0	0	0%	0
                                                  "Slash_attack": 0,
                                                  "Crush_attack": 0,
                                                  "Magic_attack": -6,
                                                  "Ranged_attack": -2,

                                                  "Stab_defence": 8,
                                                  "Slash_defence": 9,
                                                  "Crush_defence": 7,
                                                  "Magic_defence": 0,
                                                  "Ranged_defence": 8,

                                                  "Strength": 0,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0},

                                         "Steel": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+12	+13	+11	-0	+12	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -6,
                                                   "Ranged_attack": -2,

                                                   "Stab_defence": 12,
                                                   "Slash_defence": 13,
                                                   "Crush_defence": 11,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": 12,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Black": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+15	+16	+14	0	+15	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -6,
                                                   "Ranged_attack": -2,

                                                   "Stab_defence": 15,
                                                   "Slash_defence": 16,
                                                   "Crush_defence": 14,
                                                   "Magic_defence": 0,
                                                   "Ranged_defence": 15,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                         "Mithril": {"Stab_attack": 0,                       # 0	0	0	-6	-2	+17	+19	+15	0	+17	0	0	0%	0
                                                     "Slash_attack": 0,
                                                     "Crush_attack": 0,
                                                     "Magic_attack": -6,
                                                     "Ranged_attack": -2,

                                                     "Stab_defence": 17,
                                                     "Slash_defence": 19,
                                                     "Crush_defence": 15,
                                                     "Magic_defence": 0,
                                                     "Ranged_defence": 17,

                                                     "Strength": 0,
                                                     "Ranged_strength": 0,
                                                     "Magic_damage": 0,
                                                     "Prayer": 0}},

                           # ===========================================================================================
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

                                          "Iron": {"Stab_attack": 0,                      # 0	0	0	-8	-2	+8	+10	+9	-1	+9	0	0	0%	0
                                                   "Slash_attack": 0,
                                                   "Crush_attack": 0,
                                                   "Magic_attack": -8,
                                                   "Ranged_attack": -2,

                                                   "Stab_defence": 8,
                                                   "Slash_defence": 10,
                                                   "Crush_defence": 9,
                                                   "Magic_defence": -1,
                                                   "Ranged_defence": 9,

                                                   "Strength": 0,
                                                   "Ranged_strength": 0,
                                                   "Magic_damage": 0,
                                                   "Prayer": 0},

                                          "Steel": {"Stab_attack": 0,                      # 0	0	0	-8	-2	+13	+15	+14	-1	+14	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -8,
                                                    "Ranged_attack": -2,

                                                    "Stab_defence": 13,
                                                    "Slash_defence": 15,
                                                    "Crush_defence": 14,
                                                    "Magic_defence": -1,
                                                    "Ranged_defence": 14,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Black": {"Stab_attack": 0,                      # 0	0	0	-8	-2	+17	+19	+18	-1	+18	0	0	0%	0
                                                    "Slash_attack": 0,
                                                    "Crush_attack": 0,
                                                    "Magic_attack": -8,
                                                    "Ranged_attack": -2,

                                                    "Stab_defence": 17,
                                                    "Slash_defence": 19,
                                                    "Crush_defence": 18,
                                                    "Magic_defence": -1,
                                                    "Ranged_defence": 18,

                                                    "Strength": 0,
                                                    "Ranged_strength": 0,
                                                    "Magic_damage": 0,
                                                    "Prayer": 0},

                                          "Mithril": {"Stab_attack": 0,                      # 0	0	0	-8	-2	+18	+22	+20	-1	+20	0	0	0%	0
                                                      "Slash_attack": 0,
                                                      "Crush_attack": 0,
                                                      "Magic_attack": -8,
                                                      "Ranged_attack": -2,

                                                      "Stab_defence": 18,
                                                      "Slash_defence": 22,
                                                      "Crush_defence": 20,
                                                      "Magic_defence": -1,
                                                      "Ranged_defence": 20,

                                                      "Strength": 0,
                                                      "Ranged_strength": 0,
                                                      "Magic_damage": 0,
                                                      "Prayer": 0}},
                           },

                 "Boots": {# ==========================================================================================
                           "Boots": {
                                     "Bronze": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+1	+2	+3	0	0	0	0	0%	0
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

                                     "Iron": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+2	+3	+4	0	0	0	0	0%	0
                                              "Slash_attack": 0,
                                              "Crush_attack": 0,
                                              "Magic_attack": -3,
                                              "Ranged_attack": -1,

                                              "Stab_defence": 2,
                                              "Slash_defence": 3,
                                              "Crush_defence": 4,
                                              "Magic_defence": 0,
                                              "Ranged_defence": 0,

                                              "Strength": 0,
                                              "Ranged_strength": 0,
                                              "Magic_damage": 0,
                                              "Prayer": 0},

                                     "Steel": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+5	+6	+7	0	0	0	0	0%	0
                                               "Slash_attack": 0,
                                               "Crush_attack": 0,
                                               "Magic_attack": -3,
                                               "Ranged_attack": -1,

                                               "Stab_defence": 5,
                                               "Slash_defence": 6,
                                               "Crush_defence": 7,
                                               "Magic_defence": 0,
                                               "Ranged_defence": 0,

                                               "Strength": 0,
                                               "Ranged_strength": 0,
                                               "Magic_damage": 0,
                                               "Prayer": 0},

                                     "Black": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+7	+8	+9	0	0	0	0	0%	0
                                               "Slash_attack": 0,
                                               "Crush_attack": 0,
                                               "Magic_attack": -3,
                                               "Ranged_attack": -1,

                                               "Stab_defence": 7,
                                               "Slash_defence": 8,
                                               "Crush_defence": 9,
                                               "Magic_defence": 0,
                                               "Ranged_defence": 0,

                                               "Strength": 0,
                                               "Ranged_strength": 0,
                                               "Magic_damage": 0,
                                               "Prayer": 0},

                                     "Mithril": {"Stab_attack": 0,                           # 0	0	0	-3	-1	+8	+9	+10	0	0	0	0	0%	0
                                                 "Slash_attack": 0,
                                                 "Crush_attack": 0,
                                                 "Magic_attack": -3,
                                                 "Ranged_attack": -1,

                                                 "Stab_defence": 8,
                                                 "Slash_defence": 9,
                                                 "Crush_defence": 10,
                                                 "Magic_defence": 0,
                                                 "Ranged_defence": 0,

                                                 "Strength": 0,
                                                 "Ranged_strength": 0,
                                                 "Magic_damage": 0,
                                                 "Prayer": 0}},
                           },

                 # ===========================================================================================
                 "Gloves": {# ==========================================================================================
                           "Gloves": {
                                      "Bronze": {"Stab_attack": 2,                          # +2	+2	+2	+1	+2	+2	+2	+2	+1	+2	+2	0	0%	0
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

                                      "Iron": {"Stab_attack": 3,                          # +3	+3	+3	+2	+3	+3	+3	+3	+2	+3	+3	0	0%	0
                                               "Slash_attack": 3,
                                               "Crush_attack": 3,
                                               "Magic_attack": 2,
                                               "Ranged_attack": 3,

                                               "Stab_defence": 3,
                                               "Slash_defence": 3,
                                               "Crush_defence": 3,
                                               "Magic_defence": 2,
                                               "Ranged_defence": 3,

                                               "Strength": 3,
                                               "Ranged_strength": 0,
                                               "Magic_damage": 0,
                                               "Prayer": 0},

                                      "Steel": {"Stab_attack": 4,                          # +4	+4	+4	+2	+4	+4	+4	+4	+2	+4	+4	0	0%	0
                                                "Slash_attack": 4,
                                                "Crush_attack": 4,
                                                "Magic_attack": 2,
                                                "Ranged_attack": 4,

                                                "Stab_defence": 4,
                                                "Slash_defence": 4,
                                                "Crush_defence": 4,
                                                "Magic_defence": 2,
                                                "Ranged_defence": 4,

                                                "Strength": 4,
                                                "Ranged_strength": 0,
                                                "Magic_damage": 0,
                                                "Prayer": 0},

                                      "Black": {"Stab_attack": 5,                          # +5	+5	+5	+3	+5	+5	+5	+5	+3	+5	+5	0	0%	0
                                                "Slash_attack": 5,
                                                "Crush_attack": 5,
                                                "Magic_attack": 3,
                                                "Ranged_attack": 5,

                                                "Stab_defence": 5,
                                                "Slash_defence": 5,
                                                "Crush_defence": 5,
                                                "Magic_defence": 3,
                                                "Ranged_defence": 5,

                                                "Strength": 5,
                                                "Ranged_strength": 0,
                                                "Magic_damage": 0,
                                                "Prayer": 0},

                                      "Mithril": {"Stab_attack": 6,                          # +6	+6	+6	+3	+6	+6	+6	+6	+3	+6	+6	0	0%	0
                                                  "Slash_attack": 6,
                                                  "Crush_attack": 6,
                                                  "Magic_attack": 3,
                                                  "Ranged_attack": 6,

                                                  "Stab_defence": 6,
                                                  "Slash_defence": 6,
                                                  "Crush_defence": 6,
                                                  "Magic_defence": 3,
                                                  "Ranged_defence": 6,

                                                  "Strength": 6,
                                                  "Ranged_strength": 0,
                                                  "Magic_damage": 0,
                                                  "Prayer": 0}}
                           }
                 }

        if type in items.keys():
            properties_dict = items[type][name][material]

        else:
            properties_dict = None

        return properties_dict
