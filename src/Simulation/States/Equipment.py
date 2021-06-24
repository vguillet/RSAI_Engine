
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


class Equipment:
    def __init__(self, start_equipment_dict=None):
        if start_equipment_dict is None:
            self.equipment_dict = self.gen_equipment_dict()

        else:
            self.equipment_dict = start_equipment_dict

    def __call__(self):
        """
        Return equipment_dict when called

        :return: equipment_dict
        """
        return self.equipment_dict

    @staticmethod
    def gen_equipment_dict():
        """
        Create new empty equipment dict

        :return: equipment_dict
        """
        equipment_dict = {"Weapon": None,
                          "Helm": None,
                          "Chest": None,
                          "Legs": None,
                          "Shield": None,
                          "Boots": None,
                          "Gloves": None}

        return equipment_dict

    def equip_item(self, inventory_dict, statistics_dict, item):
        """
        Unequip item
        (Remove from inventory and put in equipment)

        :param inventory_dict: Inventory_dict to be used
        :param statistics_dict: Statistics_dict to adjust
        :param item: Item to be added

        :return: Updated inventory_dict and statistics_dict
        """
        # --> Remove item from inventory (has to be done first to make sure there is space if inventory is full)
        inventory_dict["Content"].remove(item)

        # --> Add item to equipment
        if self.equipment_dict[item.type] is not None:
            # --> Remove current equipped item
            inventory_dict, statistics_dict = self.unequip_item(inventory_dict=inventory_dict,
                                                                statistics_dict=statistics_dict,
                                                                item=self.equipment_dict[item.type])

        # --> Equip item
        self.equipment_dict[item.type] = item

        # --> Adjust statistics with item property
        statistics_dict["Stab_attack"] += item.properties["Stab_attack"]
        statistics_dict["Slash_attack"] += item.properties["Slash_attack"]
        statistics_dict["Crush_attack"] += item.properties["Crush_attack"]
        statistics_dict["Magic_attack"] += item.properties["Magic_attack"]
        statistics_dict["Ranged_attack"] += item.properties["Ranged_attack"]

        statistics_dict["Stab_defence"] += item.properties["Stab_defence"]
        statistics_dict["Slash_defence"] += item.properties["Slash_defence"]
        statistics_dict["Crush_defence"] += item.properties["Crush_defence"]
        statistics_dict["Magic_defence"] += item.properties["Magic_defence"]
        statistics_dict["Ranged_defence"] += item.properties["Ranged_defence"]

        statistics_dict["Strength"] += item.properties["Strength"]
        statistics_dict["Ranged_strength"] += item.properties["Ranged_strength"]
        statistics_dict["Magic_damage"] += item.properties["Magic_damage"]
        statistics_dict["Prayer"] += item.properties["Prayer"]

        return inventory_dict, statistics_dict

    def unequip_item(self, inventory_dict, statistics_dict, item):
        """
        Unequip item
        (Remove from equipment and put in inventory)

        :param inventory_dict: Inventory_dict to be used
        :param statistics_dict: Statistics_dict to adjust
        :param item: Item to be removed

        :return: Updated inventory_dict and statistics_dict
        """
        if len(inventory_dict["Content"]) + 1 > 4*7:
            print("!!!! Inventory is full !!!!")
            return inventory_dict, statistics_dict

        elif self.equipment_dict[item.type] is None or self.equipment_dict[item.type] != item:
            print("!!!! Item is not equipped !!!!")
            return inventory_dict, statistics_dict

        else:
            # --> Add item to inventory
            inventory_dict["Content"].append(item)

            # --> Remove item from equipment
            self.equipment_dict[item.type] = None

            # --> Adjust statistics with item property
            statistics_dict["Stab_attack"] -= item.properties["Stab_attack"]
            statistics_dict["Slash_attack"] -= item.properties["Slash_attack"]
            statistics_dict["Crush_attack"] -= item.properties["Crush_attack"]
            statistics_dict["Magic_attack"] -= item.properties["Magic_attack"]
            statistics_dict["Ranged_attack"] -= item.properties["Ranged_attack"]

            statistics_dict["Stab_defence"] -= item.properties["Stab_defence"]
            statistics_dict["Slash_defence"] -= item.properties["Slash_defence"]
            statistics_dict["Crush_defence"] -= item.properties["Crush_defence"]
            statistics_dict["Magic_defence"] -= item.properties["Magic_defence"]
            statistics_dict["Ranged_defence"] -= item.properties["Ranged_defence"]

            statistics_dict["Strength"] -= item.properties["Strength"]
            statistics_dict["Ranged_strength"] -= item.properties["Ranged_strength"]
            statistics_dict["Magic_damage"] -= item.properties["Magic_damage"]
            statistics_dict["Prayer"] -= item.properties["Prayer"]

            return inventory_dict, statistics_dict
