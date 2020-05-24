
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


class Equipment_tools:
    @staticmethod
    def gen_equipment_dict():
        equipment_dict = {"Weapon": None,
                          "Helm": None,
                          "Chest": None,
                          "Legs": None,
                          "Shield": None,
                          "Boots": None,
                          "Gloves": None}

        return equipment_dict

    @staticmethod
    def equip_item(equipment_dict, inventory_dict, states_dict, item):
        # --> Remove item from inventory (has to be done first to make sure there is space if inventory is full)
        inventory_dict["Content"].remove(item)

        # --> Add item to equipment
        if equipment_dict[item.type] is None:
            # --> Equip item
            equipment_dict[item.type] = item

        else:
            # --> Remove current equipped item
            equipment_dict, inventory_dict, states_dict = \
                Equipment_tools().unequip_item(equipment_dict, inventory_dict, states_dict, equipment_dict[item.type])

            # --> Equip item
            equipment_dict[item.type] = item

        # --> Adjust states with item property
        states_dict["Stab_attack"] += item.properties["Stab_attack"]
        states_dict["Slash_attack"] += item.properties["Slash_attack"]
        states_dict["Crush_attack"] += item.properties["Crush_attack"]
        states_dict["Magic_attack"] += item.properties["Magic_attack"]
        states_dict["Ranged_attack"] += item.properties["Ranged_attack"]

        states_dict["Stab_defence"] += item.properties["Stab_defence"]
        states_dict["Slash_defence"] += item.properties["Slash_defence"]
        states_dict["Crush_defence"] += item.properties["Crush_defence"]
        states_dict["Magic_defence"] += item.properties["Magic_defence"]
        states_dict["Ranged_defence"] += item.properties["Ranged_defence"]

        states_dict["Strength"] += item.properties["Strength"]
        states_dict["Ranged_strength"] += item.properties["Ranged_strength"]
        states_dict["Magic_damage"] += item.properties["Magic_damage"]
        states_dict["Prayer"] += item.properties["Prayer"]


        return equipment_dict, inventory_dict, states_dict

    @staticmethod
    def unequip_item(equipment_dict, inventory_dict, states_dict, item):
        if len(inventory_dict["Content"]) + 1 > 4*7:
            print("Inventory is full")
            return equipment_dict, inventory_dict, states_dict

        else:
            # --> Add item to inventory
            inventory_dict["Content"].append(item)

            # --> Remove item from equipment
            equipment_dict[item.type] = None
            
            # --> Adjust states with item property
            states_dict["Stab_attack"] -= item.properties["Stab_attack"]
            states_dict["Slash_attack"] -= item.properties["Slash_attack"]
            states_dict["Crush_attack"] -= item.properties["Crush_attack"]
            states_dict["Magic_attack"] -= item.properties["Magic_attack"]
            states_dict["Ranged_attack"] -= item.properties["Ranged_attack"]

            states_dict["Stab_defence"] -= item.properties["Stab_defence"]
            states_dict["Slash_defence"] -= item.properties["Slash_defence"]
            states_dict["Crush_defence"] -= item.properties["Crush_defence"]
            states_dict["Magic_defence"] -= item.properties["Magic_defence"]
            states_dict["Ranged_defence"] -= item.properties["Ranged_defence"]

            states_dict["Strength"] -= item.properties["Strength"]
            states_dict["Ranged_strength"] -= item.properties["Ranged_strength"]
            states_dict["Magic_damage"] -= item.properties["Magic_damage"]
            states_dict["Prayer"] -= item.properties["Prayer"]

            return equipment_dict, inventory_dict, states_dict
