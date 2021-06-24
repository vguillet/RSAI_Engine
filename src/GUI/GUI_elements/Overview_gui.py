
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from qimage2ndarray import array2qimage

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################


class Overview_GUI:
    @staticmethod
    def update_overview(gui):
        # --> Set agent overview
        gui.main_window.overview_agent_name.setText(gui.simulation.agent_lst[0].name)
        gui.main_window.state_age.setText(str(gui.simulation.agent_lst[0].age))
        gui.main_window.state_hitpoints.setText(str(gui.simulation.agent_lst[0].states()["Hitpoint"]))

        gui.main_window.level_melee.setText(str(gui.simulation.agent_lst[0].melee_level))
        gui.main_window.level_range.setText(str(gui.simulation.agent_lst[0].range_level))
        gui.main_window.level_mage.setText(str(gui.simulation.agent_lst[0].mage_level))
        gui.main_window.level_combat.setText(str(gui.simulation.agent_lst[0].combat_level))

        # --> Set environment overview
        gui.main_window.source_count.setText(str(len(gui.simulation.environment.source_lst)))
        gui.main_window.converter_count.setText(str(len(gui.simulation.environment.converter_lst)))
        gui.main_window.sink_count.setText(str(len(gui.simulation.environment.sink_lst)))
        gui.main_window.poi_count.setText(str(len(gui.simulation.environment.POI_dict)))

        return

    @staticmethod
    def update_agent_overview_tab(gui):
        # --> Set statistics
        gui.main_window.state_stab_attack.setText(str(gui.simulation.agent_lst[0].statistics()["Stab_attack"]))
        gui.main_window.state_slash_attack.setText(str(gui.simulation.agent_lst[0].statistics()["Slash_attack"]))
        gui.main_window.state_crush_attack.setText(str(gui.simulation.agent_lst[0].statistics()["Crush_attack"]))
        gui.main_window.state_magic_attack.setText(str(gui.simulation.agent_lst[0].statistics()["Magic_attack"]))
        gui.main_window.state_ranged_attack.setText(str(gui.simulation.agent_lst[0].statistics()["Ranged_attack"]))

        gui.main_window.state_stab_defence.setText(str(gui.simulation.agent_lst[0].statistics()["Stab_defence"]))
        gui.main_window.state_slash_defence.setText(str(gui.simulation.agent_lst[0].statistics()["Slash_defence"]))
        gui.main_window.state_crush_defence.setText(str(gui.simulation.agent_lst[0].statistics()["Crush_defence"]))
        gui.main_window.state_magic_defence.setText(str(gui.simulation.agent_lst[0].statistics()["Magic_defence"]))
        gui.main_window.state_ranged_defence.setText(str(gui.simulation.agent_lst[0].statistics()["Ranged_defence"]))

        gui.main_window.state_strength.setText(str(gui.simulation.agent_lst[0].statistics()["Strength"]))
        gui.main_window.state_ranged_strength.setText(str(gui.simulation.agent_lst[0].statistics()["Ranged_strength"]))
        gui.main_window.state_magic_damage.setText(str(gui.simulation.agent_lst[0].statistics()["Magic_damage"]))
        gui.main_window.state_prayer.setText(str(gui.simulation.agent_lst[0].statistics()["Prayer"]))

        # --> Set skills
        gui.main_window.skills_attack.setValue(gui.simulation.agent_lst[0].skills()["Attack"]["Level"])
        gui.main_window.skills_strength.setValue(gui.simulation.agent_lst[0].skills()["Strength"]["Level"])
        gui.main_window.skills_defence.setValue(gui.simulation.agent_lst[0].skills()["Defence"]["Level"])
        gui.main_window.skills_ranged.setValue(gui.simulation.agent_lst[0].skills()["Ranged"]["Level"])
        gui.main_window.skills_prayer.setValue(gui.simulation.agent_lst[0].skills()["Prayer"]["Level"])
        gui.main_window.skills_magic.setValue(gui.simulation.agent_lst[0].skills()["Magic"]["Level"])
        gui.main_window.skills_runecrafting.setValue(gui.simulation.agent_lst[0].skills()["Runecrafting"]["Level"])
        gui.main_window.skills_hitpoint.setValue(gui.simulation.agent_lst[0].skills()["Hitpoint"]["Level"])
        gui.main_window.skills_crafting.setValue(gui.simulation.agent_lst[0].skills()["Crafting"]["Level"])
        gui.main_window.skills_mining.setValue(gui.simulation.agent_lst[0].skills()["Mining"]["Level"])
        gui.main_window.skills_smithing.setValue(gui.simulation.agent_lst[0].skills()["Smithing"]["Level"])
        gui.main_window.skills_fishing.setValue(gui.simulation.agent_lst[0].skills()["Fishing"]["Level"])
        gui.main_window.skills_cooking.setValue(gui.simulation.agent_lst[0].skills()["Cooking"]["Level"])
        gui.main_window.skills_firemaking.setValue(gui.simulation.agent_lst[0].skills()["Firemaking"]["Level"])
        gui.main_window.skills_woodcutting.setValue(gui.simulation.agent_lst[0].skills()["Woodcutting"]["Level"])

        gui.main_window.skills_xp_attack.setText(str(gui.simulation.agent_lst[0].skills()["Attack"]["Experience"]))
        gui.main_window.skills_xp_strength.setText(str(gui.simulation.agent_lst[0].skills()["Strength"]["Experience"]))
        gui.main_window.skills_xp_defence.setText(str(gui.simulation.agent_lst[0].skills()["Defence"]["Experience"]))
        gui.main_window.skills_xp_ranged.setText(str(gui.simulation.agent_lst[0].skills()["Ranged"]["Experience"]))
        gui.main_window.skills_xp_prayer.setText(str(gui.simulation.agent_lst[0].skills()["Prayer"]["Experience"]))
        gui.main_window.skills_xp_magic.setText(str(gui.simulation.agent_lst[0].skills()["Magic"]["Experience"]))
        gui.main_window.skills_xp_runecrafting.setText(str(gui.simulation.agent_lst[0].skills()["Runecrafting"]["Experience"]))
        gui.main_window.skills_xp_hitpoint.setText(str(gui.simulation.agent_lst[0].skills()["Hitpoint"]["Experience"]))
        gui.main_window.skills_xp_crafting.setText(str(gui.simulation.agent_lst[0].skills()["Crafting"]["Experience"]))
        gui.main_window.skills_xp_mining.setText(str(gui.simulation.agent_lst[0].skills()["Mining"]["Experience"]))
        gui.main_window.skills_xp_smithing.setText(str(gui.simulation.agent_lst[0].skills()["Smithing"]["Experience"]))
        gui.main_window.skills_xp_fishing.setText(str(gui.simulation.agent_lst[0].skills()["Fishing"]["Experience"]))
        gui.main_window.skills_xp_cooking.setText(str(gui.simulation.agent_lst[0].skills()["Cooking"]["Experience"]))
        gui.main_window.skills_xp_firemaking.setText(str(gui.simulation.agent_lst[0].skills()["Firemaking"]["Experience"]))
        gui.main_window.skills_xp_woodcutting.setText(str(gui.simulation.agent_lst[0].skills()["Woodcutting"]["Experience"]))

        # --> Set inventory
        # --> Add coins
        gui.main_window.inventory_slot_label_1.setText(str(gui.simulation.agent_lst[0].inventory()["Coins"]))
        pixmap = QPixmap("src/Data/Assets/Items_assets/Coins.png")
        gui.main_window.inventory_slot_asset_1.setPixmap(pixmap)

        # --> Add content
        slot = 1
        if len(gui.simulation.agent_lst[0].inventory()["Content"]) != 0:
            for item in gui.simulation.agent_lst[0].inventory()["Content"]:
                # --> Add to next slot
                slot += 1
                getattr(gui.main_window, "inventory_slot_label_" + str(slot)).setText(str(item))

                pixmap = QPixmap(item.asset_path)
                getattr(gui.main_window, "inventory_slot_asset_" + str(slot)).setPixmap(pixmap)

        # --> Set equipment
        for item in gui.simulation.agent_lst[0].equipment().keys():
            if gui.simulation.agent_lst[0].equipment()[item] is not None:
                if item == "Helm":
                    gui.main_window.equipment_helm_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_helm_asset.setPixmap(pixmap)

                elif item == "Chest":
                    gui.main_window.equipment_chest_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_chest_asset.setPixmap(pixmap)

                elif item == "Legs":
                    gui.main_window.equipment_legs_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_legs_asset.setPixmap(pixmap)

                elif item == "Boots":
                    gui.main_window.equipment_boots_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_boots_asset.setPixmap(pixmap)

                elif item == "Gloves":
                    gui.main_window.equipment_gloves_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_gloves_asset.setPixmap(pixmap)

                elif item == "Weapon":
                    gui.main_window.equipment_weapon_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_weapon_asset.setPixmap(pixmap)

                elif item == "Shield":
                    gui.main_window.equipment_shield_label.setText(str(gui.simulation.agent_lst[0].equipment()[item]))
                    pixmap = QPixmap(gui.simulation.agent_lst[0].equipment()[item].asset_path)
                    gui.main_window.equipment_shield_asset.setPixmap(pixmap)

        return
