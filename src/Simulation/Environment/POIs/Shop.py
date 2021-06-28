
################################################################################################################
"""
A converter sub-class specialising in exchanging items for money (agenth selling and buying)
"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Simulation.Environment.POIs.Core.Converter import Converter
from src.Simulation.Environment.POIs.Prints.Shop_prints import Shop_prints

from src.Simulation.States.Interests import Interests
from src.Simulation.States.Inventory import Inventory

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'


################################################################################################################


class Shop(Converter):
    def __init__(self,
                 name: "Converter name",
                 ref,
                 simulation_origin,
                 simulation_shape,
                 world_pos,

                 traded_item_types: list = [],
                 start_inventory: dict = None,
                 start_interests: dict = None,
                 characteristics: dict = None):
        # --> Initialising base class (building all ref properties)
        super().__init__(name=name,
                         ref=ref,
                         simulation_origin=simulation_origin,
                         simulation_shape=simulation_shape,
                         world_pos=world_pos)

        self.label = "Market"

        # --> Setup states dicts
        self.interests = Interests(start_interests_dict=start_interests)
        self.inventory = Inventory(start_inventory_dict=start_inventory)

        # --> Initialising records
        self.transaction_records = []

        # --> Initialise prints
        self.prints = Shop_prints()

    def evaluate_transaction(self,
                             date,
                             agent: "Agent class instance",
                             transaction_type: "buy or sell",
                             item_type,
                             item,
                             item_quantity):
        self.prints.transaction_recap(name=agent.name,
                                      transaction_type=transaction_type,
                                      item_type=item_type,
                                      item=item,
                                      quantity_requested=str(item_quantity),
                                      agent_expectation=str(agent.interests()[item_type][item]["Expectation"]),
                                      market_expectation=str(self.interests()[item_type][item]["Expectation"]))

        # ----- Performing buy transaction
        if transaction_type == "buy":

            # --> Checking whether requested item type is in the Market's inventory
            if item_type in self.inventory().keys():

                # --> Checking whether requested item is in the Market's inventory
                if item in self.inventory()[item_type].keys():

                    # --> Checking whether the requested item count is available
                    if self.inventory()[item_type][item] >= item_quantity:

                        # --> Check whether agent expectation/ market expectation interests match:
                        if agent.interests()[item_type][item]["Expectation"] >= self.interests()[item_type][item]["Expectation"]:

                            # TODO: Setup price_per_item based on traits (GA upgrade)
                            # --> Computing price per item based on interest (meet in the middle rn)
                            price_per_item = (agent.interests()[item_type][item]["Expectation"] -
                                              self.interests()[item_type][item]["Expectation"]) / 2 + \
                                              self.interests()[item_type][item]["Expectation"]

                            # --> Checking whether bot money matches requested quantity
                            if agent.inventory()["Money"] < price_per_item * item_quantity:
                                item_quantity = int(agent.inventory()["Money"] / price_per_item)

                                #  -> If bot money is too low
                                if item_quantity == 0:
                                    self.prints.print_1()

                                    # ----- Rate action
                                    agent.action_success_history.append(0)  # Neutral
                                    return

                            # --> Perform transaction
                            self.perform_transaction(date=date,
                                                     agent=agent,
                                                     transaction_type=transaction_type,
                                                     item_type=item_type,
                                                     item=item,
                                                     item_quantity=item_quantity,
                                                     price_per_item=price_per_item)

                            # --> Computing transaction surplus
                            market_surplus = price_per_item - self.interests()[item_type][item]["Minimum"]
                            agent_surplus = agent.interests()[item_type][item]["Maximum"] - price_per_item

                            # --> Increasing market expectations
                            self.interests()[item_type][item] = \
                                self.interests.increase_expectation(interests_dict=self.interests()[item_type][item],
                                                                    difference=market_surplus,
                                                                    delta_percent=10,
                                                                    setting=1)

                            # --> Decreasing agent expectations
                            agent.interests()[item_type][item] = \
                                self.interests.decrease_expectation(interests_dict=agent.interests()[item_type][item],
                                                                    difference=agent_surplus,
                                                                    delta_percent=10,
                                                                    setting=1)

                            self.prints.successful_buy_transaction_recap(item_quantity=item_quantity,
                                                                         item_type=item_type,
                                                                         item=item,
                                                                         price_per_item=price_per_item)

                            # ----- Rate action
                            agent.action_success_history.append(1)  # Success
                            return

                        else:
                            # --> Computing transaction shortfall
                            market_shortfall = self.interests()[item_type][item]["Expectation"] - \
                                               agent.interests()[item_type][item]["Expectation"]
                            agent_shortfall = agent.interests()[item_type][item]["Expectation"] - \
                                              self.interests()[item_type][item]["Expectation"]

                            # --> Decreasing market expectations
                            self.interests()[item_type][item] = \
                                self.interests.decrease_expectation(interests_dict=self.interests()[item_type][item],
                                                                    difference=market_shortfall,
                                                                    delta_percent=10,
                                                                    setting=1)

                            # --> Increasing agent expectations
                            agent.interests()[item_type][item] = \
                                self.interests.increase_expectation(interests_dict=agent.interests()[item_type][item],
                                                                    difference=agent_shortfall,
                                                                    delta_percent=10,
                                                                    setting=1)

                            self.prints.print_2()

                            # ----- Rate action
                            agent.action_success_history.append(0)  # Neutral
                            return

                    # --> If item count is not available
                    else:
                        # Todo: Auto adjust item quantity brought
                        # --> Increasing market expectations
                        self.interests()[item_type][item] = \
                            self.interests.increase_expectation(interests_dict=self.interests()[item_type][item],
                                                                setting=0)

                        # --> Increasing agent expectations
                        agent.interests[item_type][item] = \
                            self.interests.increase_expectation(interests_dict=agent.interests()[item_type][item],
                                                                setting=0)

                        self.prints.print_3(item=item,
                                            available_item_count=self.inventory()[item_type][item])

                        # ----- Rate action
                        agent.action_success_history.append(0)  # Neutral
                        return

                # --> If item is not available
                else:
                    # --> Increasing market expectations
                    self.interests()[item_type][item] = \
                        self.interests.increase_expectation(interests_dict=self.interests()[item_type][item],
                                                            setting=0)

                    # --> Increasing agent expectations
                    agent.interests()[item_type][item] = \
                        self.interests.increase_expectation(interests_dict=agent.interests()[item_type][item],
                                                            setting=0)

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
            if item_type in self.inventory().keys():

                # --> Checking whether the requested item count is available
                if agent.inventory()[item_type][item] >= item_quantity:

                    # --> Check whether agent expectation/ market expectation interests match:
                    if agent.interests()[item_type][item]["Expectation"] <= self.interests()[item_type][item]["Expectation"]:

                        # TODO: Setup price_per_item based on traits
                        # --> Computing price per item based on interest (meet in the middle rn)
                        price_per_item = (self.interests()[item_type][item]["Expectation"] -
                                          agent.interests()[item_type][item]["Expectation"]) / 2 + \
                                          agent.interests()[item_type][item]["Expectation"]

                        # --> Checking whether Market's Money quantity is available
                        if self.inventory()["Money"] >= price_per_item * item_quantity:

                            # --> Perform transaction
                            self.perform_transaction(date=date,
                                                     agent=agent,
                                                     transaction_type=transaction_type,
                                                     item_type=item_type,
                                                     item=item,
                                                     item_quantity=item_quantity,
                                                     price_per_item=price_per_item)

                            # --> Computing transaction surplus
                            market_surplus = self.interests()[item_type][item]["Maximum"] - price_per_item
                            agent_surplus = price_per_item - agent.interests()[item_type][item]["Minimum"]

                            # --> Decreasing market expectations
                            self.interests()[item_type][item] = \
                                self.interests.decrease_expectation(interests_dict=self.interests()[item_type][item],
                                                                    difference=market_surplus,
                                                                    delta_percent=10,
                                                                    setting=1)

                            # --> Increasing agent expectations
                            agent.interests()[item_type][item] = \
                                self.interests.increase_expectation(interests_dict=agent.interests()[item_type][item],
                                                                    difference=agent_surplus,
                                                                    delta_percent=10,
                                                                    setting=1)

                            self.prints.successful_sell_transaction_recap(item_quantity=item_quantity,
                                                                          item_type=item_type,
                                                                          item=item,
                                                                          price_per_item=price_per_item)

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
                        market_shortfall = agent.interests()[item_type][item]["Expectation"] - \
                                           self.interests()[item_type][item]["Expectation"]
                        agent_shortfall = self.interests()[item_type][item]["Expectation"] - \
                                          agent.interests()[item_type][item]["Expectation"]

                        # --> Increasing market expectations
                        self.interests()[item_type][item] = \
                            self.interests.increase_expectation(interests_dict=self.interests()[item_type][item],
                                                                difference=market_shortfall,
                                                                delta_percent=10,
                                                                setting=1)

                        # --> Decreasing agent expectations
                        agent.interests()[item_type][item] = \
                            self.interests.decrease_expectation(interests_dict=agent.interests()[item_type][item],
                                                                difference=agent_shortfall,
                                                                delta_percent=10,
                                                                setting=1)

                        self.prints.print_7()

                        # ----- Rate action
                        agent.action_success_history.append(0)  # Neutral
                        return

                # --> If requested item count is not available
                else:
                    self.prints.print_3(item=item,
                                        available_item_count=agent.inventory()[item_type][item])

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
        self.transaction_records.append(Transaction(date=date,
                                                    transaction_type=transaction_type,
                                                    item_type=item_type,
                                                    item=item,
                                                    item_quantity=item_quantity,
                                                    price_per_item=price_per_item))

        # ----- Performing buy transaction
        if transaction_type == "buy":

            # ---> Client account update
            # --> Debiting client
            agent.inventory()["Money"] -= price_per_item * item_quantity

            # --> Adding item to client's inventory
            for _ in range(item_quantity):
                agent.inventory().add_item_to_inventory(item=item)

            # ---> Market account update
            # --> Crediting Market
            self.inventory()["Money"] += price_per_item * item_quantity

            # --> Removing item from Market's inventory
            self.inventory()[item_type][item] -= item_quantity

            return

        # ----- Performing sell transaction
        elif transaction_type == "sell":

            # ---> Client account update
            # --> Crediting client
            agent.inventory()["Money"] += price_per_item * item_quantity

            # --> removing item to client's inventory
            if item_type == "Items":
                agent.inventory().remove_item_from_inventory(item=item)

            else:
                agent.inventory()[item_type][item] -= item_quantity

            # ---> Market account update
            # --> Debiting Market
            self.inventory()["Money"] -= price_per_item * item_quantity

            # --> Adding item to Market's inventory
            if item in self.inventory()[item_type].keys():
                self.inventory()[item_type][item] += item_quantity
            else:
                self.inventory()[item_type][item] = item_quantity
        return

    def __str__(self):
        return self.name + " (Market-type converter)"

    def __repr__(self):
        return self.__str__()


class Transaction:
    def __init__(self, date, transaction_type, item_type, item, item_quantity, price_per_item):
        # --> Record transaction information
        self.date = date
        self.transaction_type = transaction_type

        self.item_type = item_type
        self.item = item
        self.item_quantity = item_quantity
        self.price_per_item = price_per_item

    def __str__(self):
        if self.transaction_type == "buy":
            return f"Transaction --> {self.item_type}: {self.item}, -{self.item_quantity} units at {self.price_per_item}$ (Net: +{self.item_quantity * self.price_per_item}$)    {self.date}"
        else:
            return f"Transaction --> {self.item_type}: {self.item}, +{self.item_quantity} units at {self.price_per_item}$ (Net: -{self.item_quantity * self.price_per_item}$)    {self.date}"

    def __repr__(self):
        return self.__str__()
