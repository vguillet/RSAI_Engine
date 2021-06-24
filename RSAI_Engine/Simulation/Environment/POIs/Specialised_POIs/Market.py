
################################################################################################################
"""
A converter sub-class specialising in exchanging items for money (agenth selling and buying)
"""

# Built-in/Generic Imports

# Libs

# Own modules
from RSAI_Engine.Simulation.Environment.POIs.POI import POI
from RSAI_Engine.Simulation.Environment.POIs.Converter import Converter
from RSAI_Engine.Simulation.Environment.POIs.Prints.Market_prints import Market_prints

from RSAI_Engine.Simulation.Environment.Tools.Interests_tools import Interests_tools

# from Ingenium_Engine.Tools.Transaction_gen import gen_transaction
# from Ingenium_Engine.Tools.Inventory_tools import Inventory_tools
# from Ingenium_Engine.Tools.Characteristics_tools import Characteristics_tools

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'


################################################################################################################


class gen_market(POI, Converter):
    def __init__(self, name: "Converter name",
                 pos: tuple,
                 traded_item_types: list = "Resources",
                 inventory: dict = None,
                 interests: dict = None,
                 characteristics: dict = None):
        # --> Initialising base class (building all ref properties)
        super().__init__(name, pos)
        self.label = "Market"

        # --> Setup inventory/interests/characteristics dicts
        self.gen_dicts(traded_item_types, inventory, interests, characteristics)

        # --> Initialising records
        self.transaction_records = []

        # --> Initialise prints
        self.prints = Market_prints()

    def evaluate_transaction(self, date, agent: "Agent class instance", transaction_type: "buy or sell", item_type,
                             item, item_quantity):
        interests_tools = Interests_tools()

        self.prints.transaction_recap(agent.name, transaction_type,
                                      item_type, item,
                                      str(item_quantity),
                                      str(agent.interests[item_type][item]["Expectation"]),
                                      str(self.interests[item_type][item]["Expectation"]))

        # ----- Performing buy transaction
        if transaction_type == "buy":

            # --> Checking whether requested item type is in the Market's inventory
            if item_type in self.inventory.keys():

                # --> Checking whether requested item is in the Market's inventory
                if item in self.inventory[item_type].keys():

                    # --> Checking whether the requested item count is available
                    if self.inventory[item_type][item] >= item_quantity:

                        # --> Check whether agent expectation/ market expectation interests match:
                        if agent.interests[item_type][item]["Expectation"] >= self.interests[item_type][item]["Expectation"]:

                            # TODO: Setup price_per_item based on traits (GA upgrade)
                            # --> Computing price per item based on interest (meet in the middle rn)
                            price_per_item = (agent.interests[item_type][item]["Expectation"] -
                                              self.interests[item_type][item]["Expectation"]) / 2 + \
                                             self.interests[item_type][item]["Expectation"]

                            # --> Checking whether bot money matches requested quantity
                            if agent.inventory["Money"] < price_per_item * item_quantity:
                                item_quantity = int(agent.inventory["Money"] / price_per_item)

                                #  -> If bot money is too low
                                if item_quantity == 0:
                                    self.prints.print_1()

                                    # ----- Rate action
                                    agent.action_success_history.append(0)  # Neutral
                                    return

                            # --> Perform transaction
                            self.perform_transaction(date, agent, transaction_type, item_type, item, item_quantity,
                                                     price_per_item)

                            # --> Computing transaction surplus
                            market_surplus = price_per_item - self.interests[item_type][item]["Minimum"]
                            agent_surplus = agent.interests[item_type][item]["Maximum"] - price_per_item

                            # --> Increasing market expectations
                            self.interests[item_type][item] = interests_tools.increase_expectation(
                                self.interests[item_type][item], market_surplus)

                            # --> Decreasing agent expectations
                            agent.interests[item_type][item] = interests_tools.decrease_expectation(
                                agent.interests[item_type][item], agent_surplus)

                            self.prints.successful_buy_transaction_recap(item_quantity, item_type, item, price_per_item)

                            # ----- Rate action
                            agent.action_success_history.append(1)  # Success
                            return

                        else:
                            # --> Computing transaction shortfall
                            market_shortfall = self.interests[item_type][item]["Expectation"] - \
                                               agent.interests[item_type][item]["Expectation"]
                            agent_shortfall = agent.interests[item_type][item]["Expectation"] - \
                                              self.interests[item_type][item]["Expectation"]

                            # --> Decreasing market expectations
                            self.interests[item_type][item] = interests_tools.decrease_expectation(
                                self.interests[item_type][item], market_shortfall)

                            # --> Increasing agent expectations
                            agent.interests[item_type][item] = interests_tools.increase_expectation(
                                agent.interests[item_type][item], agent_shortfall)

                            self.prints.print_2()

                            # ----- Rate action
                            agent.action_success_history.append(0)  # Neutral
                            return

                    # --> If item count is not available
                    else:
                        # Todo: Audo adjust item quantity brought
                        # --> Increasing market expectations
                        self.interests[item_type][item] = interests_tools.increase_expectation(
                            self.interests[item_type][item],
                            setting=1)

                        # --> Increasing agent expectations
                        agent.interests[item_type][item] = interests_tools.increase_expectation(
                            agent.interests[item_type][item],
                            setting=1)

                        self.prints.print_3(item, self.inventory[item_type][item])

                        # ----- Rate action
                        agent.action_success_history.append(0)  # Neutral
                        return

                # --> If item is not available
                else:
                    # --> Increasing market expectations
                    self.interests[item_type][item] = interests_tools.increase_expectation(
                        self.interests[item_type][item],
                        setting=1)

                    # --> Increasing agent expectations
                    agent.interests[item_type][item] = interests_tools.increase_expectation(
                        agent.interests[item_type][item],
                        setting=1)

                    self.prints.print_4(item)

                    # ----- Rate action
                    agent.action_success_history.append(0)  # Neutral
                    return

            # --> If item type is not available
            else:
                self.prints.print_5(item_type)

                # ----- Rate action
                agent.action_success_history.append(-1)  # Error
                return

        # ----- Performing sell transaction
        elif transaction_type == "sell":

            # --> Checking whether item is tradable in this market
            if item_type in self.inventory.keys():

                # --> Checking whether the requested item count is available
                if agent.inventory[item_type][item] >= item_quantity:

                    # --> Check whether agent expectation/ market expectation interests match:
                    if agent.interests[item_type][item]["Expectation"] <= self.interests[item_type][item]["Expectation"]:

                        # TODO: Setup price_per_item based on traits
                        # --> Computing price per item based on interest (meet in the middle rn)
                        price_per_item = (self.interests[item_type][item]["Expectation"] -
                                          agent.interests[item_type][item]["Expectation"]) / 2 + \
                                         agent.interests[item_type][item]["Expectation"]

                        # --> Checking whether Market's Money quantity is available
                        if self.inventory["Money"] >= price_per_item * item_quantity:

                            # --> Perform transaction
                            self.perform_transaction(date, agent, transaction_type, item_type, item, item_quantity,
                                                     price_per_item)

                            # --> Computing transaction surplus
                            market_surplus = self.interests[item_type][item]["Maximum"] - price_per_item
                            agent_surplus = price_per_item - agent.interests[item_type][item]["Minimum"]

                            # --> Decreasing market expectations
                            self.interests[item_type][item] = interests_tools.decrease_expectation(
                                self.interests[item_type][item], market_surplus)

                            # --> Increasing agent expectations
                            agent.interests[item_type][item] = interests_tools.increase_expectation(
                                agent.interests[item_type][item], agent_surplus)

                            self.prints.successful_sell_transaction_recap(item_quantity, item_type, item,
                                                                          price_per_item)

                            # ----- Rate action
                            agent.action_success_history.append(1)  # Success
                            return

                        # --> If market doesn't have enough Money
                        else:
                            self.prints.print_6()

                            # ----- Rate action
                            agent.action_success_history.append(0)  # Neutral
                            return

                    # --> If expectations don't match
                    else:
                        # --> Computing transaction shortfall
                        market_shortfall = agent.interests[item_type][item]["Expectation"] - \
                                           self.interests[item_type][item]["Expectation"]
                        agent_shortfall = self.interests[item_type][item]["Expectation"] - \
                                          agent.interests[item_type][item]["Expectation"]

                        # --> Increasing market expectations
                        self.interests[item_type][item] = interests_tools.increase_expectation(
                            self.interests[item_type][item], market_shortfall)

                        # --> Decreasing agent expectations
                        agent.interests[item_type][item] = interests_tools.decrease_expectation(
                            agent.interests[item_type][item], agent_shortfall)

                        self.prints.print_7()

                        # ----- Rate action
                        agent.action_success_history.append(0)  # Neutral
                        return

                # --> If requested item count is not available
                else:
                    self.prints.print_3(item, agent.inventory[item_type][item])

                    # ----- Rate action
                    agent.action_success_history.append(-1)  # Error
                    return

            # --> If item is not tradable in the market
            else:
                self.prints.print_5(item_type)

                # ----- Rate action
                agent.action_success_history.append(-1)  # Error
                return

        else:
            self.prints.print_8()
            raise

    def perform_transaction(self, date, agent, transaction_type, item_type, item, item_quantity, price_per_item):
        self.transaction_records.append(
            gen_transaction(date, transaction_type, item_type, item, item_quantity, price_per_item))

        # ----- Performing buy transaction
        if transaction_type == "buy":

            # ---> Client account update
            # --> Debiting client
            agent.inventory["Money"] -= price_per_item * item_quantity

            # --> Adding item to client's inventory
            if item_type == "Items":
                Inventory_tools().equip_item(agent, item, item_quantity)

            else:
                agent.inventory[item_type][item] += Inventory_tools().get_gathered_quantity(agent, item_quantity)

            # ---> Market account update
            # --> Crediting Market
            self.inventory["Money"] += price_per_item * item_quantity

            # --> Removing item from Market's inventory
            self.inventory[item_type][item] -= item_quantity

            return

        # ----- Performing sell transaction
        elif transaction_type == "sell":

            # ---> Client account update
            # --> Crediting client
            agent.inventory["Money"] += price_per_item * item_quantity

            # --> removing item to client's inventory
            if item_type == "Items":
                Inventory_tools().unequip_item(agent, item, item_quantity)

            else:
                agent.inventory[item_type][item] -= item_quantity

            # ---> Market account update
            # --> Debiting Market
            self.inventory["Money"] -= price_per_item * item_quantity

            # --> Adding item to Market's inventory
            if item in self.inventory[item_type].keys():
                self.inventory[item_type][item] += item_quantity
            else:
                self.inventory[item_type][item] = item_quantity

        # ----- Clean up inventories
        inventory_tools = Inventory_tools()

        # self.inventory = inventory_tools.clean_inventory(self.inventory)
        # agent.inventory = inventory_tools.clean_inventory(agent.inventory)

        return

    def add_to_inventory(self, item_type, item, item_quantity, force_add=False):
        # --> Checking whether item type is in the Market's inventory
        if item_type in self.inventory.keys() or force_add is True:

            # --> Create item type if force_add is true
            if item_type not in self.inventory.keys():
                self.inventory[item_type] = {}

            # --> Checking if item is already in inventory
            if item in self.inventory[item_type].keys():
                self.inventory[item_type][item] += item_quantity
                return

            else:
                self.inventory[item_type][item] = item_quantity
                return

        else:
            self.prints.print_5(item_type)
            return

    def remove_from_inventory(self, item_type, item, item_quantity):
        # --> Checking if item is in inventory
        if item in self.inventory[item_type].keys():

            # --> Checking if item quantity to be removed is in the inventory
            if self.inventory[item_type][item] >= item_quantity:
                self.inventory[item_type][item] -= item_quantity

            else:
                self.inventory[item_type][item] = 0
                return

        else:
            self.prints.print_9()
            return

    def gen_dicts(self,
                  traded_item_types: list,
                  inventory: dict,
                  interests: dict,
                  characteristics: dict):
        # --> Setting up inventory
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = Inventory_tools().gen_market_inventory_dict(traded_item_types)

        # --> Setting up interest
        if interests is not None:
            self.interests = interests
        else:
            self.interests = Interests_tools().gen_market_interests_dict(traded_item_types)

        # --> Setting up characteristics
        if characteristics is not None:
            self.characteristics = characteristics
        else:
            self.characteristics = Characteristics_tools().gen_market_characteristics_dict()

    def __str__(self):
        return self.name + " (Market-type converter)"

    def __repr__(self):
        return self.__str__()
