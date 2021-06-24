
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from RSAI_Engine.Simulation.Environment.POIs.Core.Source import Source
from RSAI_Engine.Simulation.Environment.POIs.Prints.Mine_prints import Mine_prints


# from Ingenium_Engine.States.Inventory_tools import Inventory_tools
# from Ingenium_Engine.States.Characteristics_tools import Characteristics_tools

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class gen_mine(Source):
    def __init__(self,
                 name: "Converter name",
                 ref,
                 simulation_origin,
                 simulation_size,
                 world_pos,

                 inventory: dict = None,
                 characteristics: dict = None):
        # --> Initialising base class (building all ref properties)
        super().__init__(name=name,
                         ref=ref,
                         simulation_origin=simulation_origin,
                         simulation_size=simulation_size,
                         world_pos=world_pos)

        self.label = "Mine"

        # --> Setup inventory/interests/characteristics dicts
        self.gen_dicts(inventory, characteristics)

        # --> Initialising records
        # self.transaction_records = []

        # --> Initialise prints
        self.prints = Mine_prints()

    def mine(self, agent, resource):
        mined_quantity = 1

        # --> Checking if mine is not empty
        if self.inventory["Resources"][resource] > 0:

            # --> Checking if agent tool is sufficient to mine resource
            if agent.characteristics["Tool"] >= self.characteristics["RMD"][resource]:

                # --> Adjusting mined quantity if not available
                if self.inventory["Resources"][resource] < mined_quantity:
                    mined_quantity = self.inventory["Resources"][resource]

                # --> Remove resource from mine inventory
                self.inventory["Resources"][resource] -= mined_quantity

                # --> Adjust gathered quantity to available cargo space
                gathered_quantity = Inventory_tools().get_gathered_quantity(agent, mined_quantity)

                self.prints.mining_recap(resource, mined_quantity)
                self.prints.gathered_resource_recap(resource, gathered_quantity)

                # --> Add resource to agent inventory
                if resource in list(agent.inventory["Resources"].keys()):
                    agent.inventory["Resources"][resource] += gathered_quantity

                else:
                    agent.inventory["Resources"][resource] = gathered_quantity

                # ----- Rate action
                if gathered_quantity == 0:
                    agent.action_success_history.append(-1)     # Error
                else:
                    agent.action_success_history.append(1)      # Success
                return

            else:
                self.prints.failed_mining_recap(agent.characteristics["Tool"], resource, self.characteristics["RMD"][resource])

                # ----- Rate action
                agent.action_success_history.append(-1)     # Error
                return

        else:
            self.prints.mine_empty()

            # ----- Rate action
            agent.action_success_history.append(0)      # Neutral
            return

    def add_to_inventory(self, resource, resource_quantity):
        # --> Checking if item is already in inventory
        if resource in self.inventory["Resources"].keys():
            self.inventory["Resources"][resource] += resource_quantity

        else:
            self.inventory["Resources"][resource] = resource_quantity

        self.characteristics = Characteristics_tools().gen_mine_characteristics_dict(self.inventory)

    def remove_from_inventory(self, resource, resource_quantity):
        # --> Checking if resource is in inventory
        if resource in self.inventory["Resources"].keys():

            # --> Checking if resource quantity to be removed is in the inventory
            if self.inventory["Resources"][resource] >= resource_quantity:
                self.inventory["Resources"][resource] -= resource_quantity

            else:
                self.inventory["Resources"][resource] = 0

            self.characteristics = Characteristics_tools().gen_mine_characteristics_dict(self.inventory)

        else:
            self.prints.print_1()
            return

    def gen_dicts(self,
                  inventory: dict,
                  characteristics: dict):
        # --> Setting up inventory
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = Inventory_tools().gen_mine_inventory_dict()

        # --> Setting up characteristics
        if characteristics is not None:
            self.characteristics = characteristics
        else:
            self.characteristics = Characteristics_tools().gen_mine_characteristics_dict(self.inventory)

    def __str__(self):
        return self.name + " (Mine-type source)"

    def __repr__(self):
        return self.__str__()
